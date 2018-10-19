# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:46:45 2018

@author: Jesus
"""

import scraper

scraper = scraper.Scraper()
scraper.run()
#print(scraper.data) #Uncomment in debug
scraper.output_csv('test.csv') #Comment in debug
