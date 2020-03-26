# 案例v7百度翻译
from urllib import request,parse
# 导入json包，负责处理json格式的模块
import json

'''
大致流程：
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是服务器返回的释义
'''

baseurl = 'http://fanyi.baidu.com/sug'
# 存放用来模拟form的数据，一定是dict格式
keyword = input("请输入需要翻译的内容：")
data = {
    'kw': keyword
}
# print(data)

# 需要使用parse模块对data进行编码
data = parse.urlencode(data)
data = data.encode('utf-8')
# print("编码后的data：",data)
# print("编码后的data类型：",type(data))
# 当需要类型为bytes时：在数据的后面加上: data = data.encode('utf-8')

# 构造请求头，请求头部至少包含：
# 1.传入数据的长度
# 2.request要求传入的请求是一个dict格式

# 有了headers，data，url就可以尝试发出请求
rsp = request.urlopen(baseurl,data=data)

json_data = rsp.read().decode()

# 把json字符串转换为字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    if item['k'] == keyword:
        print(item['k'], ": ", item['v'])
