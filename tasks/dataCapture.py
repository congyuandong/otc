#coding:utf-8

"""

data_dict  = 
{

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


import urllib2
import json
from bs4 import BeautifulSoup

chinaSee_url = ["100053", "100028", "100048", "100015", "100055", "100018", "100009", "100042", "100017", "100032", "100049", "100037", "100005", "100003", "100031", "100007", "100021", "100076", "100012", "100063", "100052", "100038", "100066", "100045", "100026", "100025", "100156", "100035"]
neeq_url_2 = ["430002", "430663", "430097", "430073", "430493", "430542", "430022", "430081", "430145", "831039", "430036", "430132", "430506", "830798", "430396", "830859", "430141", "430060", "430746", "430254", "831020", "430164", "430570", "430095", "430696", "430044", "430040", "430207", "430723", "430602", "430099", "830802", "430306", "430372"]
neeq_url_3 = ["430357", "430263", "430225", "430130", "430243", "430515", "830818", "430505", "830879", "830983"]
data_dict = {}

# 上海 日期+今日最近成交价+今日成交量
def china_see():
	global data_dict
	for url in chinaSee_url:
		full_Url = "http://www.china-see.com/hqsj-9.jsp?rightType=9&cid=&fid=&gqdm={}".format(url)
		req = urllib2.Request(full_Url)
		resp = urllib2.urlopen(req)
		respHtml = resp.read()
		soup = BeautifulSoup(respHtml, from_encoding='utf-8')

		s = soup.find_all('tr', bgcolor='#BAEADE')
		li =  s[0].text.encode('utf-8').split('\n')

		data_dict[url] = {
			'date':li[1],
			'latest_price':li[3],
			'volume':li[10]
		}
		if data_dict[url]['latest_price'] == 0.0:
			data_dict[url]['latest_price'] = li[2]

def remoteData(url):
	req = urllib2.Request(url)
	resp = urllib2.urlopen(req)
	json_json = resp.read()
	json_dict = json.loads(json_json)
	remoteData_json = json_dict['remoteData']
	remoteData_dict = json.loads(remoteData_json)
	return remoteData_dict

def neeq():
	global data_dict

	# 新三版 协议 日期+今日最近成交价
	for url in neeq_url_2:
		full_url = "http://www.neeq.cc/ajax/QTHangQinByzqdm?zqdm={}".format(url)

		remoteData_dict = remoteData(full_url)

		data_dict[url] = {
			'date':remoteData_dict['date'], 
			'latest_price':remoteData_dict['ZJCJ'], 
			'volume': 0
			}
		if data_dict[url]['latest_price'] == 0.0:
			data_dict[url]['latest_price'] = remoteData_dict['ZRSP']

	# 新三版 协议 今日成交量
	for url in neeq_url_2:
		full_url = "http://www.neeq.cc/ajax/QTXieYi?zqdm={}".format(url)

		remoteData_dict = remoteData(full_url)

		tag = remoteData_dict['status']
		if(tag == 0):
			data_dict_url = data_dict[url]
			deals_json = remoteData_dict['deals'][0]
			data_dict_url['volume'] = deals_json['CJSL']

	#新三版 做市 日期+今日最近成交价+今日成交量
	for url in neeq_url_3:
		full_url = "http://www.neeq.cc/ajax/QTHangQinByzqdm?zqdm={}".format(url)

		remoteData_dict = remoteData(full_url)

		data_dict[url] = {
			'date' : remoteData_dict['date'], 
			'latest_price' : remoteData_dict['ZJCJ'], 
			'volume' : remoteData_dict['CJSL']
			}
		if data_dict[url]['latest_price'] == 0.0:
			data_dict[url]['latest_price'] = remoteData_dict['ZRSP']

def dumpotc():
	neeq()
	china_see()
	return data_dict

if __name__ == "__main__":
	
	#neeq()
	#china_see()
	#print 'data_dict =\n', data_dict
	print dumpotc()