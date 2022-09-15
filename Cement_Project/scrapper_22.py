# -*- coding: utf-8 -*-
from functions import * # importing functions from file function.py
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import re

data=[]
# in this range we can specify the number of pages to be scrapped
for page in range(0,18):
    url="https://www.magicbricks.com/mbsearch/propertySearch.html?editSearch=Y&category=S&propertyType=10002,10003,10021,10022,10001,10017,10000&city=3327&alliance=&banks=&searchType=1&page="+str(page)+"&tab1=&sortBy=premiumRecent&alliance=&banks="
    response=get(url)
    html_soup=BeautifulSoup(response.text,'html.parser')
    link_containers=html_soup.find_all('h3')
    # range 30 means there are 30 properties in a page
    for items in range(30):
        link_item=str(link_containers[items].a)
        link_item=link_item.split('"')
        link_item=re.sub('amp;','',link_item[3])
        url=link_item
        response=get(url)
        html_soup=BeautifulSoup(response.text,'html.parser')
        values=(headline_f(html_soup),price_f(html_soup),p_addrs(html_soup),bedroom_f(html_soup),bathroom_f(html_soup),balcony_f(html_soup),super_a(html_soup),p_p_sqft(html_soup),p_status_f(html_soup),trans_f(html_soup),n_floor(html_soup),c_parking(html_soup),furnish_s(html_soup),lift_f(html_soup),desc(html_soup),p_breakup(html_soup),land_m(html_soup),age_c(html_soup),price_c(html_soup),e_rent(html_soup),m_emi_f(html_soup),owner_agent_f(html_soup))
        data.append(values)
 

from pandas import DataFrame
column=['Headline','Price','Address','Bedrooms','Bathrooms','Balcony','Super Area','Price per sqft','Status','Transaction Type','Floor','Car parking','Furnished status','Lifts','Description','Price breakup','Landmarks','Age of construction','Price comparison','Expected rent','Monthly EMI','Owner/Builder']
final_data=pd.DataFrame(data,columns=column)
final_data.to_csv('property.csv',sep=',',index=False,encoding='utf-8-sig')