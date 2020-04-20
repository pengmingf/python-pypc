import requests
from bs4 import BeautifulSoup
import os
import time

url='http://wmtp.net/'
path = r'C:\Users\Administrator\Desktop\wmtp.net'
time = 0.1
download_urls = {}
#筛选结果，将图片筛选出来
def replace(url):
    res = requests.get(url)
    re_url = 'div#mainbox li div.post a img'
    res.coding = 'gbk'
    soup = BeautifulSoup(res.text, 'lxml')
    return soup.select(re_url)[0]['src']

def name(url):
    res = requests.get(url)
    re_url = 'div#mainbox li div.post a img'
    res.coding = 'gbk'
    soup = BeautifulSoup(res.text, 'lxml')
    return soup.select(re_url)[0]['src']


def detail(urls):
    # for url in urls:
    #     image = url.get('href')
    print(urls)

def start():
    res = replace(url)
    detail(res)

def main():
    if(not os.path.exists(path)):
        os.mkdir(path)
        print('文件创建成功')
    start()
    
if __name__ == "__main__":
    main()