<div><a href='https://github.com/darideveloper/indeed-jobs-scraper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/indeed-jobs-scraper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/indeed-jobs-scraper/blob/master/logo.png?raw=true' alt='Indeed Jobs Scraper' height='80px'/>

# Indeed Jobs Scraper

Extract general jobs data from computrabajo.com in specific location and searching a list of keywords.

Start date: **2022-05-31**

Last update: **2023-04-13**

Project type: **personal's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://requests.readthedocs.io/en/latest/' target='_blank'> <img src='https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png' alt='Requests' title='Requests' height='50px'/> </a><a href='https://www.crummy.com/software/BeautifulSoup/' target='_blank'> <img src='https://github.com/darideveloper/darideveloper/blob/main/imgs/logo%20bs4.png?raw=true' alt='BeautifulSoup4' title='BeautifulSoup4' height='50px'/> </a></div>

# Details

The oputput data is saved in the "data.csv" file.
You can setup the project with the config.json file.

## Output data
Sample:
|keyword|location|title|company|details|date|link|
|---|---|---|---|---|---|---|
|frontend|Aguascalientes|Desarrollador web / Analista de IT|Scanner Forms S.A...|-Sexo indistinto -Escolaridad: Ingeniero en TIC´s titulado #javascript #frontend #php...|Hace 4 días|mx.indeed.com/rc/clk?jk=49c2b625...|
|frontend|Aguascalientes|React Developer|bebo Technologies Mx Aguascalientes ...|bebo MX is a leading IT software solution provider and IT services company. bebo MX is...|Hace 6 días|mx.indeed.com/rc/clk?jk=49c2b625...|
|frontend|Aguascalientes|Programador/a|Clubmaple Aguascalientes Aguascaliente...|Integración de innovación tecnológica en CRM de Laravel/Jquery SE REQUIERE FACTURA de ...|Más de 30 días|mx.indeed.com/rc/clk?jk=49c2b625...|

# Install

## Third party modules

Open Terminal in project folder and install all modules from pip:
(here a tutorial about [how to open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)) 

``` bash
$ pip install -r requirements.txt
```

# Settings

In the config.json file, there are the locations and keywords for search in the page

## Structure

```json
{
    "indeed": "mx.indeed.com",
    "keywords":  [
        "web developer", 
        "frontend", 
    ],
    "locations": [
        "Aguascalientes",
        "Baja California",
        "Baja California Sur",
        "Campeche",
        "Chiapas",
        "Chihuahua",
        "Ciudad de Mexico",
    ]
}
```

### indeed
Url of the specific page where do you can to extract data
### keywords
List of word to search in the page
### locations
Countries, states or cities where do you want to extract data

# Run

Run the **__main __.py** or the **project folder** with your python 3.10 interpreter.

You can do it from terminal or by **double clicking the file**

## Run sample from terminal:

Before, [open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)

After, type: 

``` bash
$ py __main__.py
```

or

``` bash
$ py .
```


