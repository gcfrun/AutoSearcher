#coding=utf-8
import watermelon_ocr
import watermelon_search
from PIL import Image

import wda
# DEVICE_URL
# url = 'http://192.168.2.100:8100'
url = 'http://localhost:8100'

def test():
    # image = Image.open('/Users/gcf/Desktop/答题/西瓜视频/1.png')
    # question, keywords = watermelon_ocr.get_matter(image)
    # a = raw_input("Please input a string:\n")
    # # 单搜问题
    # if a == '1':
    #     print '\033[0;31m' + question + '\033[0m\n'
    #     watermelon_search.search(question, keywords)
    # # 搜问题与答案
    # if a == '2':
    #     for key in keywords:
    #         question = question + ' ' + key
    #     print '\033[0;31m' + question + '\033[0m\n'
    #     watermelon_search.search(question, keywords)
    tag = 1
    while (tag):
        a = raw_input("Please input a string:\n")
        if (a == 'end'):
            break
        else:
            print '**********************************************************************************************************\n'
            image = Image.open('/Users/gcf/Desktop//答题/西瓜视频/%s.png' % (a))
            question, keywords = watermelon_ocr.get_matter(image)
            for key in keywords:
                question = question + ' ' + key
            print '\033[0;31m' + question + '\033[0m\n'
            watermelon_search.search(question, keywords)

def actual():
    c = wda.Client(url)  # DEVICE_URL
    tag = 1
    while (tag):
        a = raw_input("Please input a string:\n")
        if (a == 'end'):
            break
        else:
            c.screenshot('/Users/gcf/Desktop/shotImg/%dscreen.png' % (tag))
            print '**********************************************************************************************************\n'
            image = Image.open('/Users/gcf/Desktop/shotImg/%dscreen.png' % (tag))
            question, keywords = watermelon_ocr.get_matter(image)
            # 单搜问题
            if a == '1':
                print '\033[0;31m' + question + '\033[0m\n'
                watermelon_search.search(question, keywords)
            # 搜问题与答案
            if a == '2':
                for key in keywords:
                    question = question + ' ' + key
                print '\033[0;31m' + question + '\033[0m\n'
                watermelon_search.search(question, keywords)

if __name__ == '__main__':
    # test()
    actual()