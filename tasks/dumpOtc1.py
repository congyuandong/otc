#coding:utf-8

"""
新三版（全国中小企业股份转让系统）
主网站：http://www.neeq.cc/
	http://www.china-see.com/
提供网站例子：http://www.neeq.cc/detailcompany?DM=430011&type=0
		http://www.china-see.com/stockInfo.do?pro=&industry=&stockCode=100053

URL数量：72

所有所需数据：data_dict  = {

							证券代码1: {
										'date':最近一个交易日,
										'latest_price':最新价,
										'volume':成交数量,
									}, 

							证券代码2: {
										'date':最近一个交易日,
										'latest_price':最新价,
										'volume':成交数量, 
									}, 

							…共72个证券… 

							}
"""


#http://www.neeq.cc/detailcompany?DM=430011&type=0	#新版网址2014-12-28
#http://www.china-see.com/stockInfo.do?pro=&industry=&stockCode=100053	#新版网址2014-12-28

import urllib2
import json
from bs4 import BeautifulSoup
import time
data_dict={}

neeq_url = ["430719", "430011", "430002", "430009", "430073", "430037", "430015", "430357", "430021", "430065", "430004", "430005", "430074", "430022", "430051", "430088", "430014", "430033", "430010", "430084", "430003", "430130", "430041", "430018", "430339", "430043", "430536", "430057", "430143", "430098", "430064", "430081", "430029", "430382", "830837", "430183", "430618", "430225", "430607", "430092", "430610", "430318", "430085","430359",  "430028", "430253", "831028", "430141", "430017", "430062", "430174", "430105", "430116", "430024", "430103", "430243", "430066", "430432", "830810", "830978", "430089", "430027", "430036", "430078", "430083","430075","430208","430362","430366","430394","430493","430620","430662","830772","830850","830933","830968","831030","831061","831087"]
chinasee_url = ["100053", "100028", "100048", "100015", "100055", "100018", "100042","100117"]
#上海股权交易
def china_see():
	global data_dict
	for url in chinasee_url:
		# 以下为新地址2014-12-28
		full_url = "http://www.china-see.com/stockCodeDealInfo.do?stockCode="+url
		#print full_url
		req = urllib2.Request(full_url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		# print "respHtml=", respHtml
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')

		s = soup.find_all('tr')
		li =  s[1].text.encode('utf-8').split('\n')
		#print li
		#print li[1] + ' ' + li[3] + ' ' + li[10]
		data_dict[url] = {
			#'date':"".join(li[1].split('-')),
			#'date':li[1].string,
			#'date':time.strptime(li[1][4:],'%Y-%m-%d'),
			#'date':"".join(li[1][4:].split('-')),
			'date':"".join(li[1].split('-')),
			'latest_price':float(li[3]),
			'volume':int(li[10])
		}
	#print data_dict

def remoteData(url):
	req = urllib2.Request(url)
	resp = urllib2.urlopen(req)
	json_json = resp.read()
	# print "data_json = \n", data_json
	json_dict = json.loads(json_json)
	# print data_dict
	remoteData_json = json_dict['remoteData']
	remoteData_dict = json.loads(remoteData_json)
	#print remoteData_dict
	return remoteData_dict

#中小型企业交易
def neeq():
	global data_dict
	for url in neeq_url:

		full_url = "http://www.neeq.cc/ajax/QTHangQinByzqdm?zqdm="+url
		#print full_url
		# www.neeq.cc/ajax/QTHangQinByzqdm?zqdm=430357
		#print full_url
		remoteData_dict = remoteData(full_url)
		#print remoteData_dict
		
		tag = remoteData_dict['status']
		
		#print tag
		if(tag == 0):
			if remoteData_dict['ZJCJ'] == 0.0:
				data_dict[url] = {
	                                 'date' : remoteData_dict['date'], 
        	                         'latest_price' : remoteData_dict['ZRSP'],
                	                 'volume' : remoteData_dict['CJSL']
                        	         }
			else:
				data_dict[url] = {
					'date' : remoteData_dict['date'], 
					'latest_price' : remoteData_dict['ZJCJ'], 
					'volume' : remoteData_dict['CJSL']
					}
		else:
			print "********************************************"
			print "Can't get data from The " + full_url
			print "The " + url + " has no data!!!"
			pass
			
			#data_dict[url] = { 'date' : "None", 'latest_price' : "None", 'volume' : "None" }

def dumpotc1():
	#global data_dict
	neeq()
	china_see()
	#print data_dict
	return data_dict
if __name__ == "__main__":
	#global data_dict
	dumpotc1()
	#print data_dict
	'''
	data_dict = {}
	neeq(data_dict)
	print data_dict
	china_see(data_dict)
	print "*********************************************"
	print data_dict
	print "*********************************************"
	'''


