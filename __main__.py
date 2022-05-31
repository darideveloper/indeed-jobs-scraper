import os
import csv
import bs4
import requests
from logs import logger
from config import Config
# from scraping_manager.automate import Web_scraping

jobs_ids = []

def main (): 

    # Read categories, keywords and locations from json
    credentials = Config()
    indeed_page = credentials.get("indeed")
    keywords = credentials.get("keywords")
    locations = credentials.get("locations")

    # Create and open csv / database file
    csv_path = os.path.join (os.path.dirname(__file__), f"data.csv")
    csv_file = open(csv_path, "a", encoding="utf-8", newline="")
    csv_writter = csv.writer(csv_file)

    # Write colum titles 
    headers = ["keyword", "location", "title", "company", "salary", "details", "date", "link"]
    csv_writter.writerow (headers)

    # Search each keyword
    for keyword in keywords:

        # Search location
        for location in locations:

            # Loop fopr extract all pages
            start_job = 0
            page = 1
            selector_next_page = 'ul.pagination-list > li:last-child a svg'
            while True:

                # Print status
                logger.info (f"Scraping data of {keyword} in {location}, page: {page}")

                # generate url with keyword and location
                location_formated = location.lower().replace(' ', '%20')
                keyword_formated = keyword.lower().replace(' ', '%20')
                url = f"https://{indeed_page}/jobs?q=&l={location_formated}&q={keyword_formated}&start={start_job}"
                
                # Get page data page
                res = requests.get (url)
                
                # Generate css selectors for get data
                selector_article = "ul.jobsearch-ResultsList li .job_seen_beacon"
                selector_title = f"h2"
                selector_company = f".companyName"
                selector_salary = f".salary-snippet-container"
                selector_details = f".job-snippet"
                selector_date = f".date"
                selector_link = f"h2 a"

                # Get number of articles in the current page
                soup = bs4.BeautifulSoup (res.text, "html.parser")
                articles = soup.select (selector_article)
                
                # Get data from each article
                for article in articles:

                    # Skeip duplicated jobs
                    link_elem = article.select (selector_link)[0]
                    id = link_elem.get ("id")
                    if id in jobs_ids:
                        continue
                    else:
                        jobs_ids.append (id)

                    # Get job data
                    title = article.select (selector_title)[0].getText()
                    try:
                        company = article.select (selector_company)[0].getText()
                    except:
                        company = ""
                    try:
                        salary = article.select (selector_salary)[0].getText()
                    except:
                        salary = ""
                    details = article.select (selector_details)[0].getText()
                    date = article.select (selector_date)[0].getText()
                    link =  indeed_page + link_elem.attrs ["href"]

                    
                    # Clean data
                    title = title.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    company = company.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    salary =  salary.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    details = details.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    date = date.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")

                    # Add data to csv
                    row_data = [keyword, location, title, company, salary, details, date, link]
                    csv_writter.writerow (row_data)

                # Load more pages
                next_button = soup.select (selector_next_page)
                if next_button:
                    start_job+=15
                    page+=1
                else:
                    break

        # Debug lines
        # break

    # Close and save data in csv file
    csv_file.close ()


if __name__ == "__main__":

    main()