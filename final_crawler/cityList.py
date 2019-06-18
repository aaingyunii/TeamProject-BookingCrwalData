#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:28:51 2019

@author: heejinson
"""



#%%
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import json

path = "C:/Users/chuns/Downloads/chromedriver_win32/chromedriver.exe"


driver=webdriver.Chrome(path)
driver.get("https://www.booking.com/")
driver.find_element_by_xpath('//*[@id="footer_links"]/div[1]/ul/li[3]/a').click()

html = driver.page_source
soup=BeautifulSoup(html, 'html.parser')
#%%
cityDict={}
i=0
for city in soup.select('div[class=block_header] > h2 > a'):
    cityText = city.text
    cityDict[str(i)]={'cityName' : cityText}
    i=i+1

#%%
BASE_DIR = 'C:/Users/chuns/Desktop/DBWP_cralwer'

with open(os.path.join(BASE_DIR, 'city.json'), 'w', encoding='utf-8') as json_file :
        json.dump(cityDict, json_file, ensure_ascii=False, indent='\t')

driver.close()
