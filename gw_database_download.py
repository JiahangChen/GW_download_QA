# coding:utf-8
import requests, time, urllib.request, re
from moviepy.editor import *
import os, sys

import imageio
imageio.plugins.ffmpeg.download()

url = ['http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?keys2=Q&equal1=&up1=&down1=&keys3%2C4=&IDv001=&IDn001=and&word=0&print=100',
    
    'http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?word=0&data=682h26839%100%100&print=100&keys2=Q&data=682%682%36839%100%100',

'http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?word=0&data=682h26839%100%100&keys2=Q&print=100&data=682%682%75169%200%200',

'http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?word=0&data=682h26839%100%100&print=100&keys2=Q&data=682%682%108905%300%300',

'http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?word=0&data=682h26839%100%100&keys2=Q&print=100&data=682%682%145609%400%400',

'http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?word=0&data=682h26839%100%100&print=100&keys2=Q&data=682%682%188954%500%500',

'http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?word=0&data=682h26839%100%100&keys2=Q&print=100&data=682%682%232539%600%600',]

headers = {
    'Postman-Token': '75827aca-a77e-4abc-a147-98ce92504200',
    'Host': 'relena.sakura.ne.jp',
}

url_test = 'http://relena.sakura.ne.jp/gundamwar/qadb/qadb.cgi?word=0&print=100&keys2=Q&data=682%682%36839%100%100'
html = requests.get(url_test, headers=headers)
html.encoding = "Shift_JIS"
f = open("model_Weight.txt",'a', encoding='utf-8')
f.write(html.text)

for i in url:
    html = requests.get(i, headers=headers)
    html.encoding = "Shift_JIS"
    f = open("model_Weight.txt",'a', encoding='utf-8')
    f.write(html.text)
    f.write("\n") 