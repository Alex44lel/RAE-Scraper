# All Spanish Words - RAE SCRAPER

[![Badge Status](https://img.shields.io/badge/status-active-green.svg)](https://github.com/tu-usuario/tu-repositorio)
![GitHub last commit](https://img.shields.io/github/last-commit/alex44lel/RAE-Scraper)

Scrapy crawler to collect all Spanish words in the dictionary.


## Run scrapy crawler

Install all requirements from requirements.txt

``` 
pip install requirements.txt
```

Go to scrapy/rae folder

```
cd scrapy/rae
```
Execute the crawler and save result to json
```
scrapy crawl raespiderwords  -o words.json
scrapy crawl raespiderdefinitions   -o words.json
```
### Considerations
The scrappy crawler will take approximately 4 hours to get all words from RAE. There is no proxy middleware implemented on the crawler,  but this has not posed any problems in previous use cases.

## Aditional crawler
There is also a selenium bot that does the same as the scrapy crawler. To execute it go to selenium folder
```
cd selenium
```
Execute the crawler and save result to json
```
python scrapper.py
```
### Considerations
Selenium crawler is just for demonstration purposes, do not try to obtain all words with it

By [Alejandro](https://github.com/alex44lel) 
