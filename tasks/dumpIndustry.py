#coding:utf-8
import sys,urllib2

import urllib
from unGzip import ContentEncodingProcessor
from bs4 import BeautifulSoup
import simplejson as json
import ast,time

encoding_support = ContentEncodingProcessor()
#中小型挂牌数量
def ZXCOMP():
	
	url='http://www.neeq.cc/listing'


def TJCOMP():
	
	url='http://www.tjsoc.com/web/default.aspx'
	opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc = opener.open(url).read()
	soup = BeautifulSoup(html_doc)
	ul=soup.find('ul',style="text-align:left")
	#div=div.find('div',class="datebase")
	li=ul.find_all('li')[3]
	num=li.find('span').string
	print num+'tianjin'
	return num
def QLCOMP():
	#齐鲁挂牌
	url='http://www.zbotc.com/'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	table=soup.find('table',width="200")
	tr=table.find_all('tr')[1]
	font=tr.find('font')
	#num=font.string
	'''
	br没取到
	'''
	br=font.find_all('br')[0]
	
	print 'haha'
	#print num

def WHCOMP():
	#武汉挂牌
	url='http://www.china-wee.com/'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	#print soup
	div=soup.find('div',"maintop04")
	print div
	div=div.find('div',"shujulist")
	ul=div.find('ul')
	li=ul.find_all('li')[2]
	num=li.find('span').string
	print num+'wuhan'

def AHCOMP():
	#安徽挂牌
	url='http://www.ahsgq.com/aee/index.html'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	ul=soup.find('ul',"right_top")
	#print ul
	li=ul.find_all('li')[0]
	strong=li.find('span').find('strong')
	'''
	strong中没有内容
	'''
	num=strong.string
	print num
def dumpComp():
	TJCOMP()
	#QLCOMP()
	WHCOMP()
	AHCOMP()
if __name__ == '__main__':
	dumpComp()


