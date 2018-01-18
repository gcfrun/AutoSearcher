#coding=utf-8
import pytesseract
import numpy as np
from PIL import Image
import re

#return str  list(str)
def get_matter(image):
    #1.选择区域
    question = ''
    keywords = []
    crop_image = image.crop((60, 180, 700, 830))
    #2.二值化
    gray = crop_image.convert('L')
    table = []
    for i in range(256):
        if i < 230 :#233-234
            table.append(0)
        else:
            table.append(1)

    bim = gray.point(table, '1')

    #3.OCR识别
    code = pytesseract.image_to_string(bim, lang='chi_sim')
    u = code.encode('utf-8')

    #4.拼接问题与选择项
    arr = u.split('\n')
    length = len(arr)
    for index in range(length):
        data = arr[length - 1 - index]
        if data != '':
            if len(keywords) < 3:
                keywords.append(data)
            else:
                question = data + question
    removeQues = question
    for index in range(len(removeQues)):
        if index < 3:
            ch = removeQues[index]
            if ch.isdigit() or ch == '.':
                question = question.strip(ch)
        else:
            break
    return question, keywords
