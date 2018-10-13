# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:46:45 2018

@author: Jesus
"""


import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

class scraper():
    def __init__(self):
        self.base_url = 'https://www.weather.gov/bmx'
        self.main_page = '/tornadodb_main'
        #List of lists with each row values
        self.data = []
        self.header = []
        
    def __get_page(self, url):
        return requests.get(url)
    
    def __parse_html(self, page):
        return BeautifulSoup(page, features="lxml")
    
    def __get_year_links(self,html):
        year_links = []
        for td in html.find_all('td'): #find td nodes
            children = td.contents
            for child in children:
                if child.name == 'a': #with a child a
                    year_links.append(self.base_url + 
                                      '/'+ child['href']) #and extract the href
        return year_links
    
    def __parse_table_registry(self,registry):
        parsed_line = []
        for td in registry.find_all('td'):
            value = None
            #Only get the first not empty value
            for text in td.text.split('\n'): 
                if len(text) > 0:
                    value = text.strip() #Remove leading and trailing space
                    break
            if not value: #If there are none, insert NA
                value = 'NA'
            parsed_line.append(value)
                    
        return parsed_line
    
    def __get_title_index(self,tags):
        for i,tag in enumerate(tags):
            for td in tag.find_all('td'):
                if 'Tornado Occurrences' in td.text:
                    return i
            
    def __get_header_index(self,header):
        order = []
        for item in self.header[0]:
            max_sim = 0
            idx = None
            for i,item2 in enumerate(header):
                sim = SequenceMatcher(None, item, item2).ratio()
                if sim > max_sim:
                    max_sim = sim
                    idx = i
            order.append(idx)
            
        return order
    
    def __fill_data(self,html):
        trs = html.find('table').find_all('tr')
        
        title_idx = self.__get_title_index(trs)
        header = self.__parse_table_registry(trs[title_idx+1])
        if len(self.data) == 0: #First data appended, get header
            self.header.append(header)
            
        for tr in trs[title_idx+2:]: #Loop all registries
            data = self.__parse_table_registry(tr)
            if len(data)==12: #Do not add incorrent entries
                ordered_data = []
                for idx in self.__get_header_index(header):
                    ordered_data.append(data[idx])
                self.data.append(ordered_data)  
    
    def run(self):
           page = self.__get_page(self.base_url + self.main_page)
           html = self.__parse_html(page.text)
           year_links = self.__get_year_links(html)
           for year_link in year_links: 
               year_page = self.__get_page(year_link)
               year_html = self.__parse_html(year_page.text)
               self.__fill_data(year_html) #add return for debug
               
    def output_csv(self,file='output.csv'):
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
    
scraper = scraper()
scraper.run()
#print(scraper.data) #Uncomment in debug
scraper.output_csv('test.csv') #Comment in debug