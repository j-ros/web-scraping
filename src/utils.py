#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
utils module

Contains functions used by the scraper that perform some stand-alone tasks.

Required modules
- requests
- BeautifulSoup (from bs4)
"""

import requests
from bs4 import BeautifulSoup

def get_page(url):
    """
    Performs a http GET request to an url.

    @param url: target url.

    @output: Response object.
    """
    return requests.get(url)

def parse_html(page):
    """
    Parse html content from page.

    @param page: html document to parse.

    @output: BeautifulSoup object with document as a nested data structure.
    """
    return BeautifulSoup(page, features="lxml")

def parse_table_registry(registry):
    """
    Parse a table registry given its html tag.

    @param registry: table registry to parse.

    @output parsed_line: list with all registry elements parsed.
    """
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
    """
    Get the index of the table title tag from a list of html tags.

    @param tags: list of tags to search.

    @output i: index of table title tag. None if not found.
    """
    for i, tag in enumerate(tags):
        for td in tag.find_all('td'):
            if 'Tornado Occurrences' in td.text:
                return i
    return None
