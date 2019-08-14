from urllib import request
import chardet

if __name__ == "__main__":
    url = 'https://jobs.zhaopin.com/CC375882789J00033399409.htm'
    rsp = request.urlopen(url)
    print("rsp的类型：{0}".format(type(rsp)))
    print("rsp的内容：{0}".format(rsp))
    print("url为：{0}".format(rsp.geturl()))
    print("Info为：{0}".format(rsp.info()))
    print("Code为：{0}".format(rsp.getcode()))
