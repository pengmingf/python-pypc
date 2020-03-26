import os 
import requests
import re 
from bs4 import BeautifulSoup
import execjs
import datetime
import json 
import random

url4 = "https://www.quanjing.com/"
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Cookie":"BIGipServerpool_web_ssl=2974525632.47873.0000; Hm_lvt_c01558ab05fd344e898880e9fc1b65c4=1569493122; Hm_lpvt_c01558ab05fd344e898880e9fc1b65c4=1569493122",
    "Host":"www.quanjing.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36"
}
# data4 = {"PGTID":"0d200001-0002-591d-1769-47c7dffb6e41","ClickID":"1"}
res4 = requests.get(url4,headers=headers)

# res4 = json.loads(res4.text)
# print(res4.text)

aaa = re.findall(r'[a-zA-z]+://[^\s]*.jpg"',res4.text)
print(aaa)


