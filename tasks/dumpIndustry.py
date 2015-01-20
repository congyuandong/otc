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
	print 'anhui'
def JSCOMP():
	'''
	江苏挂牌
	'''
	url='http://www.jseec.com.cn/display/index.jhtml'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	div=soup.find('div',"pagination").find('div')
	num=div.text.encode('utf8')[4:6]
	print num+'jiangsu'
	return num

def GZCOMP():
	'''
	广州挂牌
	'''
	url='http://www.china-gee.com/frontpage/index.jsp'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	div=soup.find('div',"box")
	li=div.find_all('li')[0]
	num=li.string.encode('utf8')[15:19]
	print num+'guangzhou'
	return num
def LNCOMP():
	'''
	辽宁挂牌
	'''
	url='http://www.clnee.com/center/index.jhtml?locale=zh_CN'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	div=soup.find('div',"market")
	tr=div.find_all('tr')[0]
	num=tr.find_all('td')[1].find('span').string
	print num+'liaoning'
	return num

def XJCOMP():
	'''
	新疆挂牌
	'''
	url='http://www.casdaq.com.cn/'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	div=soup.find('div',"market-data-con")
	li=div.find('ul').find_all('li')[4]
	num=li.find('em').string
	print num+'xinjiang'
	return num

def GSCOMP():
	'''
	甘肃挂牌
	'''
	url='http://www.gsotc.com.cn/main/home/index.shtml'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	div=soup.find('div',"index_right").find('div',"tablebox")
	print div
	tr=div.find('table').find_all('tr')[0]
	print tr
	num=tr.find('td').string
	print num+'gansu'
def ZJCOMP():
	'''
	浙江挂牌
	'''
	url='http://www.zjex.com.cn/'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	div=soup.find('div',"contbox")
	div=div.find('div',"datamap")
	ul=div.find('ul',"fr")
	li=ul.find_all('li')[0]
	num=li.find_all('span')[1].string
	print num+'zhejiang'
	return num
def QHCOMP():
	'''
	前海挂牌
	'''
	url='https://www.qhee.com/'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	div=soup.find_all('div',"binder-open-url")[0]
	div=div.find('div')
	num=div.string
	print num
def SXCOMP():
	'''
	山西挂牌
	'''
	url ='http://www.sxgq.net/GQJYPT/index/gpqy_list.jsp'
	opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
	html_doc=opener.open(url).read()
	soup=BeautifulSoup(html_doc)
	table=soup.find('table',height="94")
	span=table.find_all('span')[0]
	num=span.string
	print num+'shanxi'
	return num
def dumpComp():
	
	TJCOMP()
	AHCOMP()
	JSCOMP()
	GZCOMP()
	LNCOMP()
	XJCOMP()
	ZJCOMP()
	#QHCOMP()
	SXCOMP()

	#GSCOMP()
	#QLCOMP()
	#WHCOMP()
if __name__ == '__main__':
	dumpComp()


