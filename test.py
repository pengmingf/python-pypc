'''
    读取爬取图片地址，将图片加载到本地
    注意事项：
        1.需要提供文件名
        2.需要再当前目录下建立一个名叫pypc1-image文件夹用于存放图片
    本次开启4个线程，同时进行文件的下载，根据实验，下载724张图片用时大约在30秒
'''
import requests
import os
import threading
import time
import re
import random

lock = threading.Lock()
file = open('pypc20.3549869849010472.txt','r+')
urls = []
urls = file.readlines()

def run(th): 
    while len(urls)>0:
        lock.acquire()
        url = urls.pop()[:-1]
        lock.release()
        saveurl = str(random.random())[2:]
        r = requests.get(url)
        with open("pypc1-image/image-"+saveurl+".jpg","wb+") as image:
            image.write(r.content)
    print("task", th,threading.current_thread())

# def num(n):
#     lock.acquire()
#     url = urls.pop()[:-1]
#     lock.release()
#     print(n, url)
        
if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=("t1 over",))
    t2 = threading.Thread(target=run, args=("t2 over",))
    t3 = threading.Thread(target=run, args=("t3 over",))
    t4 = threading.Thread(target=run, args=("t4 over",))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    