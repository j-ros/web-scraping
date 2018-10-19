# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:46:45 2018

@author: Jesus
"""

from difflib import SequenceMatcher
import utils

class Scraper():
    def __init__(self):
        self.base_url = 'https://www.weather.gov/bmx'
        self.main_page = '/tornadodb_main'
        #List of lists with each row values
        self.header = []
        self.data = []

    def __get_year_links(self, html):
        year_links = []
        for td in html.find_all('td'): #find td nodes
            children = td.contents
            for child in children:
                if child.name == 'a': #with a child a
                    year_links.append(self.base_url +
                                      '/'+ child['href']) #and extract the href
        return year_links

    def __get_header_index(self, header):
        order = []
        for item in self.header[0]:
            max_sim = 0
            idx = None
            for i, item2 in enumerate(header):
                sim = SequenceMatcher(None, item, item2).ratio()
                if sim > max_sim:
                    max_sim = sim
                    idx = i
            order.append(idx)

        return order

    def __fill_data(self, html):
        trs = html.find('table').find_all('tr')

        title_idx = utils.get_title_index(trs)
        header = utils.parse_table_registry(trs[title_idx+1])
        if not self.data: #First data appended, get header
            self.header.append(header)

        for tr in trs[title_idx+2:]: #Loop all registries
            data = utils.parse_table_registry(tr)
            if len(data) == 12: #Do not add incorrent entries
                ordered_data = []
                for idx in self.__get_header_index(header):
                    ordered_data.append(data[idx])
                self.data.append(ordered_data)

    def run(self):
        page = utils.get_page(self.base_url + self.main_page)
        html = utils.parse_html(page.text)
        year_links = self.__get_year_links(html)
        for year_link in year_links:
            year_page = utils.get_page(year_link)
            year_html = utils.parse_html(year_page.text)
            self.__fill_data(year_html) #comment for debug
            #return self.__fill_data(year_html) #uncomment for debug

    def output_csv(self, file='output.csv'):
        file = open(file, "w+")
        #Print header
        for header in self.header[0]:
            file.write(header+';')
        file.write('\n')
        #Print data
        for row in self.data:
            for item in row:
                file.write(item+';')
            file.write('\n')
        file.close()
