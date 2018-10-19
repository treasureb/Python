#! /usr/bin/env
#coding=utf-8

import os
import os.path
import requests

def download(url):
    """
    从指定的URL中下载文件并存储到当前目录
    """

    req = requests.get(url)
    #首先检查是否存在文件
    if req.status_code == 404:
        print('No such file found at %s' %url)
        return

    filename = url.split('/')[-1]
    with open(filename,'wb') as fobj:
        fobj.write(req.content)

    print("Download over")

if __name__ == '__main__':
    url = input("Enter a URL:")
    download(url)
