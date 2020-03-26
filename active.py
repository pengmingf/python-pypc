#重新上报脚本
import requests
import time

file = open(r'C:\Users\Administrator\Desktop\remake\active.txt','r')
backdate = open(r'C:\Users\Administrator\Desktop\remake\py_backdate.txt','a+')
backdate.truncate()
url = file.readlines()

i=0
while len(url)>0:
    urls = url.pop()
    i=i+1
    res = requests.get(urls)
    #https时使用
    # res = requests.get(urls, verify=False)
    # print(str(i)+res.text)
    
    backdate.write(str(i)+res.text+'\n')
backdate.close()



