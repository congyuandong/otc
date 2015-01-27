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
	num=''
	print '天津挂牌抓取'
	url='http://www.tjsoc.com/web/default.aspx'
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		ul=soup.find('ul',style="text-align:left")
		li=ul.find_all('li')[3]
		num=li.find('span').string
	except :
		print '天津挂牌抓取失败'
	
	print num
	return num
def QLCOMP():
	#齐鲁挂牌
	num=''
	print '齐鲁挂牌抓取'
	try:
		url='http://www.zbotc.com/'
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		table=soup.find('table',width="200")
		tr=table.find_all('tr')[1]
		font=tr.find('font')
		br=font.find_all('br')
		num=font.text.encode('utf8')[19:22]
	except :
		print '齐鲁挂牌抓取失败！'
	print num
	return num

def WHCOMP():
	#武汉挂牌
	num=''
	print '武汉挂牌抓取'
	url='http://www.china-wee.com/'
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"maintop04")
		div=div.find('div',"shujulist")
		ul=div.find('ul')
		li=ul.find_all('li')[2]
		num=li.find('span').string[0:-1]
	except :
		print '武汉挂牌抓取失败'
	print num
	return num

def AHCOMP():
	#安徽挂牌
	num=''
	print '安徽挂牌抓取'
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
def JSCOMP():
	'''
	江苏挂牌
	'''
	print '江苏挂牌抓取'
	num=''
	url='http://www.jseec.com.cn/display/index.jhtml'
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"pagination").find('div')
		num=div.text.encode('utf8')[0:7]
	except :
		print '江苏挂牌抓取失败'
	print num
	return num

def GZCOMP():
	'''
	广州挂牌
	'''
	print '广州挂牌抓取'
	num=''
	url='http://www.china-gee.com/frontpage/index.jsp'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		div=soup.find('div',"box")
		li=div.find_all('li')[0]
		num=li.string.encode('utf8')[15:19]
	except :
		print '广州挂牌抓取失败'
	print num
	return num
def LNCOMP():
	'''
	辽宁挂牌
	'''
	print '辽宁挂牌抓取'
	num=''
	url='http://www.clnee.com/center/index.jhtml?locale=zh_CN'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		div=soup.find('div',"market")
		tr=div.find_all('tr')[0]
		num=tr.find_all('td')[1].find('span').string
	except :
		print '辽宁挂牌抓取失败'
	print num
	return num

def XJCOMP():
	'''
	新疆挂牌
	'''
	print '新疆挂牌抓取'
	num=''
	url='http://www.casdaq.com.cn/'
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"market-data-con")
		li=div.find('ul').find_all('li')[4]
		num=li.find('em').string
	except :
		print '新疆挂牌抓取失败'
	print num
	return num

def GSCOMP():
	'''
	甘肃挂牌
	'''
	num=''
	print '甘肃挂牌抓取'
	url='http://www.gsotc.com.cn/main/home/index.shtml'
	'''
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"index_right").find('div',"tablebox")
		tr=div.find('table').find_all('tr')[0]
		print tr
		num=tr.find('td').string
	except :
		print '甘肃挂牌抓取失败'
	'''
	req = urllib2.Request(url)
	resp = urllib2.urlopen(req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml, from_encoding='utf-8')
	#print soup.encode('utf8')
	div=soup.find('table')[0]
	print div
	#div=div1.find('div',"index_right")
	#print div
	tr=div.find('table').find_all('tr')[0]
	print tr
	num=tr.find('td').string
	print num
def ZJCOMP():
	'''
	浙江挂牌
	'''
	print '浙江挂牌抓取'
	num=''
	url='http://www.zjex.com.cn/'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		div=soup.find('div',"contbox")
		div=div.find('div',"datamap")
		ul=div.find('ul',"fr")
		li=ul.find_all('li')[0]
		num=li.find_all('span')[1].string
	except :
		print '浙江挂牌抓取失败'
	print num
	return num
def QHCOMP():
	'''
	前海挂牌
	'''
	print '前海挂牌抓取'
	url='https://www.qhee.com/'
	req = urllib2.Request(url)
	resp = urllib2.urlopen(req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml, from_encoding='utf-8')
	div=soup.find_all('div',"binder-open-url")[0]
	div=div.find('div')
	num=div.string
	print num
def SXCOMP():
	'''
	山西挂牌
	'''
	print '山西挂牌抓取'
	num=''
	url ='http://www.sxgq.net/GQJYPT/index/gpqy_list.jsp'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		table=soup.find('table',height="94")
		span=table.find_all('span')[0]
		num=span.string
	except :
		print '山西挂牌抓取失败'
	print num
	return num
def dumpComp():
	
	TJCOMP()
	AHCOMP()
	JSCOMP()
	GZCOMP()
	LNCOMP()
	XJCOMP()
	ZJCOMP()
	QHCOMP()
	SXCOMP()
	

	#GSCOMP()
	QLCOMP()
	WHCOMP()
if __name__ == '__main__':
	dumpComp()


