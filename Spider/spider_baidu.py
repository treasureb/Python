#!/usr/bin/env python
# coding=utf-8

from urllib import request

url = "https://baidu.com"

#urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False,context=None)
#page_info = urllib.request.urlopen(url).read();
#page_info = page_info.decode('utf-8')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

#构造的请求头
#urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,method=None)
page = request.Request(url,headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
print(page_info)
