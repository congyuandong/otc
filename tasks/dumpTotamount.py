#coding:utf-8
import urllib2
import json
from bs4 import BeautifulSoup
import time

tot_amount={}
china_url = ["100053", "100028", "100048", "100015", "100055", "100018", "100042","100117"]
def dump_chinasee():
	global tot_amount
	for url in china_url:
		full_url='http://www.china-see.com/f10.do?stockCode='+url
		req = urllib2.Request(full_url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		# print "respHtml=", respHtml
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')
		#print url
		div=soup.find('div',"tabcon")
		tr=div.find_all('tr')[4]
		tot_amount[url]=tr.find('td').string[0:-2]
		tot_amount[url]=''.join(tot_amount[url].split(','))
		
	#print tot_amount	
	return tot_amount

if __name__=='__main__':
	dump_chinasee()

