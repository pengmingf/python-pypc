import re
import os
import random
import datetime
import requests
import json
from bs4 import BeautifulSoup
import execjs

#需要翻译的值
inputData = input("请输入需要翻译的内容：")

headers = {
    "cookie":"BIDUPSID=77E3EC3770F41906FDA2B5EAFC026792; PSTM=1543484367; BAIDUID=C0787910F0441F50E7CEDEC24AE51BDB:FG=1; __cfduid=d3e798618490a053045a202cd1084bd0c1545719605; BDUSS=9rOX5MakRIYn44NFdsTDdLUzVFbE9jVTdSU0xQZjhPS0NOMlNMakdUdWRFb3RjQVFBQUFBJCQAAAAAAAAAAAEAAABDrL12AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ2FY1ydhWNcR0; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; delPer=0; ZD_ENTRY=baidu; H_PS_PSSID=26522_1460_21121_29522_29520_29099_29567_28835_29221; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1564544171,1565687940; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1565687940; yjs_js_security_passport=542d375e00ccc8017732ede8382e3e1d04ea24e8_1565687944_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D",
    # "cookie":"BIDUPSID=77E3EC3770F41906FDA2B5EAFC026792; PSTM=1543484367; BAIDUID=C0787910F0441F50E7CEDEC24AE51BDB:FG=1; __cfduid=d3e798618490a053045a202cd1084bd0c1545719605; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=WlXMGd3SzlaUTU2aElGbEdxM2R0cGVQVHh-SmVMWlo0WHNXQU52MEwwVUdSSjFkSVFBQUFBJCQAAAAAAAAAAAEAAABDrL12AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa3dV0Gt3VdY; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; H_PS_PSSID=1460_21121_29522_29720_29567_29221; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=5; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1569218869,1569463265,1569463274; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1569463274; __yjsv5_shitong=1.0_7_7800caa513c5491afc3e5dfb29ac158bc030_300_1569463275962_47.99.212.193_6c54f49b; yjs_js_security_passport=64b451f1563b586c12d466901248ffc0e06fe81f_1569463276_js; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    "origin" : "https://fanyi.baidu.com"
}

#核心代码，破解sign的值
with open("baidujs.js") as f:
    jsData = f.read()
sign = execjs.compile(jsData).call("e",inputData)
# print(sign)

#抓取百度翻译首页，获取token和systime和verify的值
url = "https://fanyi.baidu.com/"
data = {"aldtype":"16047"}
res = requests.get(url,data,headers =headers)
token = re.findall(r"token: '(.*)'",res.text)
systime = re.findall(r"systime: '(.*)'",res.text)
verify = re.findall(r"'yjs_js_challenge_token.*=(.*)'",res.text)

# url2 = "https://fanyi.baidu.com/pcnewcollection"
# data2 = {"req":"check","fanyi_src":"需要翻译的词","direction":"zh2en","_":systime}
# res2 = requests.get(url2,data2,headers =headers)  #返回{"errno":4005}   

# url3 = "https://fanyi.baidu.com/yjs-cgi/security/js_challenge/verify"
# data3 = {"token":verify}
# res3 = requests.get(url3,data3,headers =headers)  #返回js auth failed

url4 = "https://fanyi.baidu.com/v2transapi"
data4 = {"from":"zh","to":"en","query":inputData,"simple_means_flag":"3","sign":sign,"token":token}
res4 = requests.post(url4,data4,headers =headers)
res4 = json.loads(res4.text)
print(res4["trans_result"]["data"][0]['dst'])