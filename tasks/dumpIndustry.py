#coding:utf-8
import sys,urllib2

import urllib
from unGzip import ContentEncodingProcessor
from bs4 import BeautifulSoup
import simplejson as json
import ast,time

encoding_support = ContentEncodingProcessor()

def TJCOMP():
	num=0
	print '天津挂牌抓取'
	url='http://www.tjsoc.com/web/infor.aspx?cid=2&pages=1'
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		print 'haha1'
		div=soup.find('div',"box1").find('div',"page")
		print 'hhaha2'
		print div.text.encode('utf8')[44:46]
		num1=div.text.encode('utf8')[44:46]
	except :
		print '天津挂牌抓取失败'
	try:
		suburl='http://www.tjsoc.com/web/infor.aspx?cid=2&pages='+num1
		req = urllib2.Request(suburl)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"box1")
		trs=div.find_all('tr')
		num2=len(trs)-1
		print num2
		num=(int(num1)-1)*12+int(num2)
		print num
	except :
		print '天津挂牌抓取失败2'
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
		print num
	except :
		print '齐鲁挂牌抓取失败！'
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
		print num
	except :
		print '武汉挂牌抓取失败'
	return num

def AHCOMP():
	#安徽挂牌
	num=''
	print '安徽挂牌抓取'
	try:
		url='http://www.ahsgq.com/aee/hqsj/scsj.jsp?classid=000100060006'
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		div=soup.find('div',"zpyyb")
		tr=div.find_all('tr')[0]
		td=tr.find_all('td')[0]
		num=td.string[0:-1]
		print num
	except :
		print '安徽挂牌抓取失败！'
	return num
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
		num=div.text.encode('utf8')[5:7]
		#num=div.text.encode('utf8')[4:6]
		print num
	except :
		print '江苏挂牌抓取失败'
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
		print num
	except :
		print '广州挂牌抓取失败'
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
		print num
	except :
		print '辽宁挂牌抓取失败'
	return num

def XJCOMP():
	'''
	新疆挂牌
	'''
	print '新疆挂牌抓取'
	num=''
	'''
	要抓取的数据在这个url里没了
	'''
	url='http://www.casdaq.com.cn/'
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"market-data-con")
		#print div
		li=div.find('ul').find_all('li')[4]
		num=li.find('em').string
		print num
	except :
		print '新疆挂牌抓取失败'
	'''
	url='http://www.casdaq.com.cn/display/index.jhtml'
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"pagination").find('div')
		#num=div.text.encode('utf8')[5:8]
		num=div.text.encode('utf8')[4:7]
		#print num
	except :
		print '新疆挂牌抓取失败'
	'''
	return num

def GSCOMP():
	'''
	甘肃挂牌
	'''
	num=''
	print '甘肃挂牌抓取'
	url='http://www.gsotc.com.cn/main/research/scsj/index.shtml'
	
	try:
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"content")
		div=div.find('div',"blueinner")
		li=div.find_all('li')[0]
		em=li.find('em')
		#num=em.string[0:-2]
		num=em.string[0:-1]
		print num
	except :
		print '甘肃挂牌抓取失败'
	return num
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
		print num
	except :
		print '浙江挂牌抓取失败'
	
	return num
def QHCOMP():
	'''
	前海挂牌
	'''
	num=''
	print '前海挂牌抓取'
	try:
		url='https://www.qhee.com/'
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find_all('div',"binder-open-url")[1]
		dl=div.find_all('dl')[2]
		num=dl.find('dd').text.replace(" ","").strip('\n')
		print int(num)
	except :
		print '前海挂牌抓取失败'
	return num
	
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
		print num
	except :
		print '山西挂牌抓取失败'
	return num
def BJCOMP():
	'''
	北京挂牌
	'''
	print '北京挂牌抓取'
	num=''
	url ='http://www.bjotc.cn/tradedComShow.jhtml'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		div=soup.find('div',"fy")
		#num=div.text.encode('utf8')[4:7]
		num=div.text.encode('utf8')[5:8]
		print num
	except :
		print '北京挂牌抓取失败'
	
	return num
def HXCOMP():
	'''
	海峡挂牌
	'''
	print '海峡挂牌抓取'
	num=''
	url ='http://www.hxee.com.cn/Html/gbqyzq/'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		div=soup.find('div',"pageList_nav")
		b=div.find_all('b')[2]
		num=b.text
	except :
		print '海峡挂牌抓取失败'
	print num
	return num
def CQCOMP():
	'''
	重庆挂牌
	'''
	print '重庆挂牌抓取'
	num=0
	try:
		url1 ='http://www.chn-cstc.com/信息披露/分市场披露/tabid/136/language/zh-CN/Default.aspx'
		url1=url1.decode('utf8').encode('gb2312')
		req = urllib2.Request(url1)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		table=soup.find('table',"PagingTable")
		num1=table.text.encode('utf8')[21:22]
		print num1
		url2='http://www.chn-cstc.com/%E4%BF%A1%E6%81%AF%E6%8A%AB%E9%9C%B2/%E5%88%86%E5%B8%82%E5%9C%BA%E6%8A%AB%E9%9C%B2/tabid/136/currentpage/'+num1+'/language/zh-CN/Default.aspx'
		req = urllib2.Request(url2)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		div=soup.find('div',"NewsArticles")
		tables=div.find_all('table')
		num2=len(tables)-1
		print num2
		num=(int(num1)-1)*20+num2
	except :
		print '重庆挂牌抓取失败'
	print num
	return num
def SHCOMP():
	'''
	上海挂牌
	'''
	print '上海挂牌抓取'
	num=0
	url ='http://www.china-see.com/index.do'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		div=soup.find('div',"DWrapConRSub1")
		dd1=div.find_all('dl')[0].find('dd')
		dd2=div.find_all('dl')[1].find('dd')
		num1=dd1.text[0:-1]
		num2=dd2.text[0:-1]
		
	except :
		print '上海挂牌抓取失败'
	print num1
	print num2
	num=int(num1)+int(num2)
	print num
	return num
def ZXCOMP():
	'''
	中小型企业挂牌
	'''
	print '中小型企业挂牌抓取'
	num=''
	url ='http://www.neeq.cc/listingNew'
	try:
		opener=urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
		html_doc=opener.open(url).read()
		soup=BeautifulSoup(html_doc)
		
	except :
		print '中小型企业挂牌抓取失败'
	print num
	return num
def dumpComp():
	'''
	JSCOMP()
	GZCOMP()
	LNCOMP()
	ZJCOMP()
	SXCOMP()
	QLCOMP()
	WHCOMP()
	BJCOMP()
	HXCOMP()
	SHCOMP()
	ZXCOMP()
	TJCOMP()
	XJCOMP()
	AHCOMP()
	CQCOMP()
	GSCOMP()
	'''
	
	QHCOMP()
	
	
if __name__ == '__main__':
	dumpComp()


