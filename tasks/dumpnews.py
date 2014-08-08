#coding:utf-8
import sys,urllib2
from HTMLParser import HTMLParser

import urllib
from unGzip import ContentEncodingProcessor
from bs4 import BeautifulSoup
import re
import os
import time

def dumpZXGZ(): 
  os.system('python tasks/dumpHtml.py')
  a=open('test.html','r')
  html_doc=a.read()
  soup = BeautifulSoup(html_doc)
  #page_num = soup.find_all(text=re.compile("(\d+)\/(\d+)"))[0]
  #print page_num
  table = soup.find(id='afficheDiv')
  #print table

  trs = table.find_all('tr')
  res = []
  for tr in trs:
    tds = tr.find_all('td')
    #print tds[0].text
    tag_a = tds[1].find('a')
    #print tag_a.text.replace(' ','').encode('utf-8')
    #print tag_a.get('href')
    #print tds[2].text
    res.append([tds[0].text,tag_a.text.replace(' ','').encode('utf-8'),tag_a.get('href'),tds[2].text])

  if os.path.isfile('test.html'):
    os.remove('test.html')

  #print res
  return res

if __name__ == '__main__':
  dumpZXGZ()