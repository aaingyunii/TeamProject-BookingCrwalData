#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 22:26:59 2019

@author: heejinson
"""

#%%
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import json
from selenium.webdriver.common.keys import Keys 


path = "C:/Users/chuns/Downloads/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(path)
#%%
comment={}
for a in range(40,202):
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
    
    commentDate=[]
    #도시별 상위 1개 숙소
    time.sleep(2)
    
    if(len(driver.find_elements_by_xpath('//*[@id="hotellist_inner"]/div[2]/div[2]/div[1]/div[1]/h3/a'))==0):
        driver.find_element_by_xpath('//*[@id="hotellist_inner"]/div[5]/div[2]/div[1]/div[1]/h3/a').click()
    else:
        driver.find_element_by_xpath('//*[@id="hotellist_inner"]/div[2]/div[2]/div[1]/div[1]/h3/a').click()  #숙소 선택        time.sleep(1)
    time.sleep(2)
    driver.switch_to_window(driver.window_handles[1])   #윈도우 전환
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="show_reviews_tab"]/span').click()    #고객후기
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="hp-reviews-sliding"]/div[1]/div[2]').click() #고객후기창 한번 클릭
    time.sleep(0.3)
    for pagedown in range(1,10):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(0.3)
    if(len(driver.find_elements_by_class_name('pagenext'))==0): #스크롤뷰인지 페이지인지
        #스크롤뷰 또는 단일 페이지
        print('스크롤!')
        c_num = int(driver.find_element_by_class_name('review-score-widget__subtext').get_attribute('innerHTML').split('\n')[1].split('개')[0])
        if(len(driver.find_elements_by_class_name('c-review-block__date'))==c_num*2):   #단일 페이지
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for c in range(1,len(driver.find_elements_by_class_name('c-review-block__date')),2):
                commentDate.append(soup.select('span.c-review-block__date')[c].text.split("\n")[1])
        else:
            ## scroll view 
            ##for i in range(0,c_num):    #댓글수 만큼 일단 스크롤 다운
            for i in range(0,40):    #댓글수 만큼 일단 스크롤 다운
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(1.5)
            ##if(len(driver.find_elements_by_class_name('c-review-block__date'))==c_num*2):   #댓글수랑 ul갯수 같은지 확인
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for c in range(1,len(driver.find_elements_by_class_name('c-review-block__date')),2):
                commentDate.append(soup.select('span.c-review-block__date')[c].text.split("\n")[1])
#                else:
#                    while(len(driver.find_elements_by_class_name('c-review-block__date'))!=c_num*2):
#                        driver.find_element_by_tag_name('body').send_keys(Keys.END)
#                        time.sleep(1)
#                    html=driver.page_source
#                    soup=BeautifulSoup(html,'html.parser')
#                    for c in range(1,len(driver.find_elements_by_class_name('c-review-block__date')),2):
#                        commentDate.append(soup.select('span.c-review-block__date')[c].text)
    else:
        #페이지
        print('페이지!')
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        if(len(driver.find_elements_by_xpath('//*[@id="review_list_page_container"]/div[4]/div/div[1]/div/div[2]/div/div[7]/a/span[1]'))!=0):
            i = driver.find_element_by_xpath('//*[@id="review_list_page_container"]/div[4]/div/div[1]/div/div[2]/div/div[7]/a/span[1]').get_attribute('innerHTML')  #페이지 갯수
            if(int(i)>9):
                i=9
        else:
            i=len(driver.find_element_by_xpath('//*[@id="review_list_page_container"]/div[4]/div/div[1]/div/div[2]/div').find_elements_by_tag_name('div'))
        for c in range(1,int(i)+1):
            print(c)    #현재 페이지
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for d in range(1,len(driver.find_elements_by_class_name('c-review-block__date')),2):
                commentDate.append(soup.select('span.c-review-block__date')[d].text.split("\n")[1])
            driver.find_element_by_xpath('//*[@id="review_list_page_container"]/div[4]/div/div[1]/div/div[3]').click()  
            time.sleep(3)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    comment[str(city)] = commentDate


#%%
BASE_DIR = 'C:/Users/chuns/Desktop/DBWP_cralwer'
with open(os.path.join(BASE_DIR, 'comment.json'), 'w', encoding='utf-8') as json_file :
        json.dump(comment, json_file, ensure_ascii=False, indent='\t')

driver.close()
                                            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
