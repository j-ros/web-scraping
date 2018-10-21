#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tornado Database web-scraper

Main script to execute the web-scraping task.

Scraps tabular data from all years in Alabama Tornado Database
( https://www.weather.gov/bmx/tornadodb_main ) and returns a csv file
with the output.
"""

import scraper

scraper = scraper.Scraper()
scraper.run()
scraper.output_csv('../data/dataset.csv')
