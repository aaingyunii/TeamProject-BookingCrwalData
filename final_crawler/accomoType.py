#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:01:42 2019

@author: heejinson
"""
#%%
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import json


path = "C:/Users/chuns/Downloads/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(path)

#%%
bestAccomoType={}
for a in range(1, 202):
    #현재 도시
    driver.get("https://www.booking.com/city.ko.html?label=gen173nr-1FCAEoggI46AdIM1gEaH2IAQGYARe4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AuHuvOcFwAIB;sid=bb7eb44eca8abdfd9459162e315c39ad")
    city=driver.find_element_by_xpath('//*[@id="cityTmpl"]/div['+str(a)+']/div[1]/h2/a').get_attribute('innerHTML')
    driver.find_element_by_xpath('//*[@id="cityTmpl"]/div['+str(a)+']/div[1]/h2/a').click()
    
    time.sleep(0.3)
    
    driver.find_element_by_xpath('//*[@id="frm"]/div[1]/div[4]/div[2]/button').click()  #검색
    time.sleep(0.3)
    if(driver.find_elements_by_xpath('//*[@id="filter_review"]/div[2]/a[1]/div/span[1]')!=0):
        driver.find_element_by_xpath('//*[@id="filter_review"]/div[2]/a[1]/div/span[1]').click()    #후기 9점이상
    time.sleep(0.3)
        

    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    accomo=[[0]*2 for i in range(0,3)]
    #인기 숙소 형태
    if(len(soup.select('div[id=filter_hoteltype] > div > a > div > span'))<6):
        for b in range(0,len(soup.select('div[id=filter_hoteltype] > div > a > div > span')),2):
            accomo[int(b/2)][0] = soup.select('div[id=filter_hoteltype] > div > a > div > span')[b].text.split('\n')[1]
            accomo[int(b/2)][1] = soup.select('div[id=filter_hoteltype] > div > a > div > span')[b+1].text.split('\n')[1]
    else:
        for b in range(0,5,2):
            accomo[int(b/2)][0] = soup.select('div[id=filter_hoteltype] > div > a > div > span')[b].text.split('\n')[1]
            accomo[int(b/2)][1] = soup.select('div[id=filter_hoteltype] > div > a > div > span')[b+1].text.split('\n')[1]
    bestAccomoType[str(city)] = accomo

        
#%%
BASE_DIR = 'C:/Users/chuns/Desktop/DBWP_cralwer'
with open(os.path.join(BASE_DIR, 'accomoType.json'), 'w', encoding='utf-8') as json_file :
        json.dump(bestAccomoType, json_file, ensure_ascii=False, indent='\t')

driver.close()
