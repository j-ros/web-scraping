# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:02:46 2018

@author: Jesus
"""

import requests
from bs4 import BeautifulSoup

def get_page(url):
    return requests.get(url)

def parse_html(page):
    return BeautifulSoup(page, features="lxml")

def parse_table_registry(registry):
    parsed_line = []
    for td in registry.find_all('td'):
        value = None
        #Only get the first not empty value
        for text in td.text.split('\n'):
            if text:
                value = text.strip() #Remove leading and trailing space
                break
        if not value: #If there are none, insert NA
            value = 'NA'
        parsed_line.append(value)
    return parsed_line

def get_title_index(tags):
    for i, tag in enumerate(tags):
        for td in tag.find_all('td'):
            if 'Tornado Occurrences' in td.text:
                return i
    return None
