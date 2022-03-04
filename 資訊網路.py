
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


for i in range(0,100):
    url="http://140.125.95.10/term1102/network/homework/doc/p"+str(i)+".docx"
    #requests.get(url)
    browser.get(url)


