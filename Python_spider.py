'''
Created on 2017年9月5日

@author: xp
'''
import urllib.error
import urllib.parse
import urllib.request
import http.cookiejar

# 首先定义下边可能需要的变量
url = "https://www.baidu.com"
headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}

# 最简单的网页抓取方式
response = urllib.request.urlopen(url, timeout=10)
html = response.read().decode("utf-8")
# print(html)

# 使用request实例代替url
request = urllib.request.Request(url, data=None, headers={});
request.add_header("Referer", "http://www.baidu.com")
response = urllib.request.urlopen(request, timeout=10)
html = response.read().decode("utf-8")
# print(html)

# 发送数据，即在Request()中添加data参数
data = urllib.parse.urlencode({'act':'login', 'email':'664221812@qq.com', 'password':'123456'})
request = urllib.request.Request(url, data=data)
response = urllib.request.urlopen(request, timeout=10)
















