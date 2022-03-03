
# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests 
from bs4 import BeautifulSoup
import io
import time
from dotenv import load_dotenv
# drivePath="C:\\Users\cxz12\Downloads\chromedriver.exe"#chromedriver path

browser=webdriver.Chrome()#open browser


for i in range(0,1000):
    if(i<100):
        if(i<10):
            i=("00"+str(i))
        else:
            i=("0"+str(i))
    url="http://140.125.95.10/term1102/network/practice/doc/p14"+str(i)+".doc"
    #url="http://140.125.95.10/term1101/phpdb/practice/doc/p14hw5.doc"
    #requests.get(url)
    browser.get(url)


