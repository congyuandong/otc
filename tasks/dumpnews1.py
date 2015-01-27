#coding:utf-8
import sys,urllib2

import urllib
from unGzip import ContentEncodingProcessor
from bs4 import BeautifulSoup
from datetime import *
import simplejson as json
import ast,time

IOSTIMEFORMAT = '%Y-%m-%d'
nowDay = time.strftime(IOSTIMEFORMAT,time.gmtime(time.time()))

encoding_support = ContentEncodingProcessor()


#抓取中小股转
#主URL http://www.neeq.cc/disclosure
#最新公告URL http://bjzr.gfzr.com.cn/bjzr/zxggnew.js
def dumpZXGQ():
  result=[]
  surl='http://file.neeq.com.cn/upload'
  url='http://www.neeq.com.cn/controller/GetDisclosureannouncementPage?type=1&company_cd=&key=&subType=0&startDate=2014-12-22&endDate='+str(date.today())+'&queryParams=0&page=1&_=1421744596585'
  try:
    req=urllib2.Request(url)
    resp=urllib2.urlopen(req)
    json_json=resp.read()
    json_dict=json.loads(json_json)
    disclosureInfos_json=json_dict['disclosureInfos']
    for i in range(len(disclosureInfos_json)):
      result.append([disclosureInfos_json[i]['companyCode'],surl+disclosureInfos_json[i]['filePath'],disclosureInfos_json[i]['title'],disclosureInfos_json[i]['publishDateString']])
  except :
    print '中小型新闻抓取失败1'
  '''
  req=urllib2.Request(url)
  resp=urllib2.urlopen(req)
  json_json=resp.read()
  json_dict=json.loads(json_json)
  #print json_dict
  disclosureInfos_json=json_dict['disclosureInfos']
  #print disclosureInfos_json
  for i in range(len(disclosureInfos_json)):
    result.append([disclosureInfos_json[i]['companyCode'],surl+disclosureInfos_json[i]['filePath'],disclosureInfos_json[i]['title'],disclosureInfos_json[i]['publishDateString']])
  #print result
  '''
  #print result
  return result

#抓取上海股权
#主要URL http://www.china-see.com
#抓取URL http://www.china-see.com/my_xxpl.jsp?cid=148&fid=135
def dumpSHGQ():
  print '进入上海股权抓取新闻'
  result = []
  url = 'http://www.china-see.com/disclosure.do?articleType=pre_company'
  topUrl = 'http://www.china-see.com/'
  try:
    opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
    html_doc = opener.open(url).read()
    soup = BeautifulSoup(html_doc)
    div = soup.find('div',"wrap1Rsub1")
    dls = div.find_all('dl')
    for dl in dls:
      a = dl.find('dt').find('a')
      title = a.string
      title = title.split(' ')
      result.append([title[0],topUrl+a.get('href'),title[1].encode('utf8'),dl.find('dd').string])
  except :
    print '上海股权抓取失败1'
  '''
  opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
  html_doc = opener.open(url).read()
  soup = BeautifulSoup(html_doc)
  div = soup.find('div',"wrap1Rsub1")
  dls = div.find_all('dl')
  for dl in dls:
    a = dl.find('dt').find('a')
    title = a.string
    title = title.split(' ')
    result.append([title[0],topUrl+a.get('href'),title[1].encode('utf8'),dl.find('dd').string])
  '''
  return result

#抓取天津股权
#主要URL http://www.tjsoc.com
#抓取URL http://www.tjsoc.com/web/infor.aspx?cid=3
def dumpTJGQ():
  print '进入天津股权抓取新闻'
  result = []
  url = 'http://www.tjsoc.com/web/infor.aspx?cid=3'
  subUrl = 'http://www.tjsoc.com/web/'
  try:
    opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
    html_doc = opener.open(url).read()
    soup = BeautifulSoup(html_doc)
    ul = soup.find('ul',"newslist")
    lis = ul.find_all('li')
    for li in lis:
      result.append(['',subUrl+li.find('a').get('href').encode('utf8'),li.find('a').string.encode('utf8').strip(),li.find('span').string])
  #print result
  except :
    print '天津新闻抓取失败1'
  '''
  opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
  html_doc = opener.open(url).read()
  soup = BeautifulSoup(html_doc)

  ul = soup.find('ul',"newslist")
  lis = ul.find_all('li')
  for li in lis:
    result.append(['',subUrl+li.find('a').get('href').encode('utf8'),li.find('a').string.encode('utf8').strip(),li.find('span').string])
  '''
  #print result
  return result


#抓取齐鲁股权
#主要URL http://www.zbotc.com
#抓取http://www.zbotc.com/article-exp.php?category=2&classB=2

def dumpQLGQ():
  print '进入齐鲁股权抓取新闻'
  result = []
  url = 'http://www.zbotc.com/article-exp.php?category=2&classB=2'
  subUrl = 'http://www.zbotc.com'
  qulr='http://172.16.158.3/files/6108000000B62C5D/'
  opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
  html_doc = opener.open(url).read()
  soup = BeautifulSoup(html_doc)
  table = soup.find('table',width="98%")
  tr = table.find_all('tr')[1]
  td = tr.find('td',height="600")
  table = td.find('table')
  trs = table.find_all('tr',height="30")
  for tr in trs:
    tds = tr.find_all('td')
    title = tds[0].find('a').string
    urlin = subUrl+tds[0].find('a').get('href')[1:]
    opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
    try:
      html_docin=opener.open(urlin).read()
    except:
      print 'false'
      break
    soupin = BeautifulSoup(html_docin)
    div=soupin.find('div',"standw bc")
    div=div.find('div',"contxt")
    dl=div.find('dl')
    result.append([title[0:6],subUrl+dl.find('a').get('href')[8:],title[7:].encode('utf8'),tds[1].string])
  if result:
    print '齐鲁股权抓取成功'
    #print result
  else:
    print '齐鲁股权抓取失败'
  return result
  
#抓取重庆股权
#主要URL  http://www.chn-cstc.com/
#抓取http://www.chn-cstc.com/tabid/70/language/zh-CN/Default.aspx

def dumpCQGQ():
  print '进入重庆股权抓取新闻'
  result=[]
  url = 'http://www.chn-cstc.com/tabid/70/language/zh-CN/Default.aspx'
  try:
    opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
    html_doc = opener.open(url).read()
    soup = BeautifulSoup(html_doc)
    table=soup.find('table',width="709")
    table=table.find_all('table')[1]
    td=table.find('tr').find('td',colspan="2")
    td=td.find('tr').find('td')
    table=td.find_all('table')[0]
    trs=table.find_all('tr')
    for tr in trs:
      tds=tr.find_all('td')
      title=tds[0].find('a').string
      result.append([title[1:7],tds[0].find('a').get('href').encode('utf8'),title[7:].encode('utf8'),tds[1].string[0:10]])
  
  except :
    print '重庆新闻抓取失败1'
  return result
#抓取安徽股权
#主要URL  http://www.ahsgq.com/
#抓取
def dumpAHGQ():
  result=[]
  
  return result

#抓取浙江股权
#主要URL http://zjex.com.cn
#抓取http://zjex.com.cn/view/news.php?func=listAll&catalog=0501
#http://zjex.com.cn/view/news.php?func=listAll&catalog=0501
def dumpZJGQ():
  print '进入浙江股权抓取新闻'
  result=[]
  url='http://zjex.com.cn/view/news.php?func=listAll&catalog=0501'
  subUrl='http://zjex.com.cn'
  try:
    opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
    html_doc = opener.open(url).read()
    soup = BeautifulSoup(html_doc)
    div=soup.find('div',"subnews")
    div=div.find('div',"news_list")
    lis=div.find('ul').find_all('li')
    for li in lis:
      result.append(['',subUrl+li.find('a').get('href').encode('utf8'),li.find('a').string.encode('utf8'),li.find('span').string[1:11]])
  except :
    print '浙江新闻抓取失败1'
  #print result
  return result
    
  '''
  opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
  html_doc = opener.open(url).read()
  soup = BeautifulSoup(html_doc)
  div=soup.find('div',"subnews")
  div=div.find('div',"news_list")
  lis=div.find('ul').find_all('li')
  for li in lis:
    result.append(['',subUrl+li.find('a').get('href').encode('utf8'),li.find('a').string.encode('utf8'),li.find('span').string[1:11]])
  #print result
  
  #print result
  return result
  '''  


#抓取广州股权
#主要URL http://www.china-gee.com
#抓取  http://www.china-gee.com/frontpage/list.jsp?menuPath=LSGG
def dumpGZGQ():
  print '进入广州股权抓取新闻'
  result=[]
  url = 'http://www.china-gee.com/frontpage/list.jsp?menuPath=LSGG'
  subUrl = 'http://www.china-gee.com'
  try:
    opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
    html_doc = opener.open(url).read()
    soup = BeautifulSoup(html_doc)
    div=soup.find('div',"list")
    lis=div.find('ul').find_all('li')
    for li in lis:
      title=li.find('a').string
      title=title.split(' ')
      result.append([title[0],subUrl+li.find('a').get('href'),title[1].encode('utf8'),li.find('span').string[1:11]])
  #print result
  except :
    print '广州新闻抓取失败'
  '''
  opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
  html_doc = opener.open(url).read()
  soup = BeautifulSoup(html_doc)

  div=soup.find('div',"list")
  lis=div.find('ul').find_all('li')
  for li in lis:
    title=li.find('a').string
    title=title.split(' ')
    result.append([title[0],subUrl+li.find('a').get('href'),title[1].encode('utf8'),li.find('span').string[1:11]])
  '''
  #print result
  return result






#抓取新闻
def dumpNews():
  dumpZXGQ()
  dumpSHGQ()
  dumpTJGQ()
  #print '开始抓取齐鲁'
  #dumpQLGQ()
  #print '开始抓取重庆'
  dumpCQGQ()
  dumpGZGQ()
  dumpZJGQ()

if __name__ == '__main__':
  dumpNews()
 # dumpQLGQ()