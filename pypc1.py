
import requests
import re 
import time 
import threading
import random
import datetime

all_urls = []  #我们拼接好的图片集和列表路径
all_img_urls = []
lock = threading.Lock()


class Spider():
    #构造函数，初始化数据使用
    def __init__(self,target_url,headers):
        self.target_url = target_url
        self.headers = headers

    #获取所有的想要抓取的URL
    def getUrls(self,start_page,page_num):
        global all_urls
        #循环得到URL
        for i in range(start_page,page_num+1):
            url = self.target_url  % i
            all_urls.append(url)

class Producer(threading.Thread):
    def run(self):
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        #     'HOST':'www.meizitu.com'
        # }
        global all_urls
        listall = []
        while len(all_urls) > 0:
            lock.acquire()      #加锁（多线程操作的时候，防止对于同一网址多次读取）
            page_url = all_urls.pop()   #弹出元素，获取弹出的值
            lock.release()      #解锁
            respose = requests.get(page_url)
            respose.encoding = "UTF-8"
            listall += re.findall(r'[a-zA-z]+://[^\s]*.jpg',respose.text)
        # 删除重复数据
        lists = []
        for l in listall:
            if not l in lists:
                lists.append(l)
        #写数据
        file = open('pypc2'+str(random.random())+'.txt',"w+")
        file.write(str(datetime.datetime.now())+'\n')
        for i in lists:
            file.write(i+'\n')
        file.close()
        print(len(listall))
        print(len(lists))

if __name__ == "__main__":
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST':'www.meizitu.com'
    }
    target_url = 'http://www.moko.cc/moko/post/%d.html' #图片集和列表规则
    
    spider = Spider(target_url,headers)
    spider.getUrls(1,20)
    # print(all_urls)
    product = Producer()
    # print("________________________")
    product.run()
        
