#coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
import re


def search(ques,keywords):
    length =5
    request = urllib2.Request(
        'http://www.baidu.com/s?wd=' + urllib.quote((ques).strip().decode(sys.stdin.encoding).encode('gbk')))
    response = urllib2.urlopen(request)

    soup = BeautifulSoup(response.read(), 'html5lib')
    # rr1 =soup.select('div.result h3.t > a')  #标题
    data = soup.select('div.c-abstract')

    for index in range(len(data)):
        if index<length:
            item = data[index]
            # 处理<em></em>
            data1 = re.sub('<em>', '\033[32;0m', str(item))
            data2 = re.sub('</em>', '\033[0m', data1)
            # 保留内容
            data3 = re.sub(u'<[\d\D]*?>', '', data2)
            for key in keywords:
                data3 = re.sub(key, '\033[0;35m'+key+'\033[0m', data3)
            print data3 + '\n\n'
        else:
            break
