# Alabama Tornado Dataset
### Author: Jesús Ros Solé

## Objective

The objective of this project is to obtain a dataset using web scraping techniques on the [Alabama Tornado Dataset](https://www.weather.gov/bmx/tornadodb_main)
webpage.

The project is developed in Python3 and uses the following external libraries:
- BeautifulSoup, from bs4
- requests
- SequenceMatcher, from difflib

## Content

- data
	- dataset.csv: output dataset.
- doc
	- img: folder containing images used in documentation.
	- doc.Rmd: R script to generate documentation.
	- doc.pdf: pdf output of the documentation.
- src
	- main.py: Python script that executes the web scraping pipeline.
	- scraper.py: Python script with the definition of the Scraper class, containing the structures to store the scraped data and methods to manipulate it.
	- utils.py: Python script with functions used by the Scraper class that perform some stand-alone tasks.
- LICENCE: license file under which this work is released.
- README.md: this file.



