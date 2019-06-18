#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:13:44 2019

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
bestTravelType={}

for a in range(1, 202):
    #현재 도시
    driver.get("https://www.booking.com/city.ko.html?label=gen173nr-1FCAEoggI46AdIM1gEaH2IAQGYARe4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AuHuvOcFwAIB;sid=bb7eb44eca8abdfd9459162e315c39ad")
    city=driver.find_element_by_xpath('//*[@id="cityTmpl"]/div['+str(a)+']/div[1]/h2/a').get_attribute('innerHTML')
    driver.find_element_by_xpath('//*[@id="cityTmpl"]/div['+str(a)+']/div[1]/h2/a').click()
    
    time.sleep(1)
    
    driver.find_element_by_xpath('//*[@id="frm"]/div[1]/div[4]/div[2]/button').click()  #검색
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="filter_review"]/div[2]/a[1]/div/span[1]').click()    #후기 9점이상
    time.sleep(2.5)
    if(len(driver.find_elements_by_xpath('//*[@id="sortbar_dropdown_button"]'))==1):
        driver.find_element_by_xpath('//*[@id="sortbar_dropdown_button"]').click()
    time.sleep(1)
    driver.find_element_by_class_name('sort_bayesian_review_score').click()     #고평점후기 
    
    family=0
    couple=0
    friends=0
    solo=0
    business=0
    #도시별 상위 1개 숙소
    time.sleep(2)
    
    if(len(driver.find_elements_by_xpath('//*[@id="hotellist_inner"]/div[2]/div[2]/div[1]/div[1]/h3/a'))==0):
        driver.find_element_by_xpath('//*[@id="hotellist_inner"]/div[5]/div[2]/div[1]/div[1]/h3/a').click()
    else:
        driver.find_element_by_xpath('//*[@id="hotellist_inner"]/div[2]/div[2]/div[1]/div[1]/h3/a').click()  #숙소 선택
    time.sleep(2)
    driver.switch_to_window(driver.window_handles[1])   #윈도우 전환
    driver.find_element_by_xpath('//*[@id="show_reviews_tab"]/span').click()    #고객후기
    driver.find_element_by_xpath('//*[@id="hp-reviews-sliding"]/div[1]/div[2]').click() #고객후기창 한번 클릭
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    i=len(driver.find_elements_by_xpath('//*[@id="reviewer_type_filter"]/option'))
    for d in range(1,i):

        t=driver.find_element_by_xpath('//*[@id="reviewer_type_filter"]/option['+str(d+1)+']').get_attribute('value')

        if(t=='review_category_group_of_friends'):
            friends=friends + int(soup.select('#reviewer_type_filter > option')[d]['data-quantity']) 
        if(t=='family_with_children'):
            family=family + int(soup.select('#reviewer_type_filter > option')[d]['data-quantity'])
        if(t=='couple'):
            couple=couple + int(soup.select('#reviewer_type_filter > option')[d]['data-quantity'])
        if(t=='solo_traveller'):
            solo=solo + int(soup.select('#reviewer_type_filter > option')[d]['data-quantity'])
        if(t=='business_traveller'):
            business=business + int(soup.select('#reviewer_type_filter > option')[d]['data-quantity'])

    driver.close()
    driver.switch_to_window(driver.window_handles[0])
                                        
    bestTravelType[str(city)] = {'family' : family, 'couple' : couple, 'friends' : friends, 'solo':solo, 'business':business }
    



    
#%%
BASE_DIR = 'C:/Users/chuns/Desktop/DBWP_cralwer'
with open(os.path.join(BASE_DIR, 'travelType.json'), 'w', encoding='utf-8') as json_file :
        json.dump(bestTravelType, json_file, ensure_ascii=False, indent='\t')

driver.close()
