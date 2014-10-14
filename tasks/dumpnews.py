#coding:utf-8
import sys,urllib2

import urllib
from unGzip import ContentEncodingProcessor
from bs4 import BeautifulSoup
import simplejson as json
import ast,time

IOSTIMEFORMAT = '%Y-%m-%d'
nowDay = time.strftime(IOSTIMEFORMAT,time.gmtime(time.time()))

encoding_support = ContentEncodingProcessor()


#抓取中小股转
#主URL http://www.neeq.cc/disclosure
#最新公告URL http://bjzr.gfzr.com.cn/bjzr/zxggnew.js
def dumpZXGZ():
  result = []
  url = 'http://bjzr.gfzr.com.cn/bjzr/zxggnew.js'
  news = urllib2.urlopen(url).read().decode('gbk').encode('utf8')
  news = news[17:len(news)-1]
  #print json.dumps(result)
  news = ast.literal_eval(news)
  for new in news:
    if new[5] ==  nowDay and new[3] == 'PDF':
      #print new[0],'http://bjzr.gfzr.com.cn/'+new[1],new[2]
      result.append([new[0],'http://bjzr.gfzr.com.cn/'+new[1],new[2],new[5]])
  return result

#抓取上海股权
#主要URL http://www.china-see.com
#抓取URL http://www.china-see.com/my_xxpl.jsp?cid=148&fid=135
def dumpSHGQ():
  result = []
  url = 'http://www.china-see.com/my_xxpl.jsp?cid=148&fid=135'
  topUrl = 'http://www.china-see.com'
  opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
  html_doc = opener.open(url).read().decode('gb2312').encode('utf8')
  soup = BeautifulSoup(html_doc)

  table = soup.find('table',width="706")
  trs = table.find_all('tr')
  trs = trs[5:-4]
  for tr in trs:
    td = tr.find('td',background="myimages/xxpl_r19_c11.jpg")
    #print td
    if td is not None:
      table = td.find('table')
      tds = table.find('tr').find_all('td')
      #根据时间进行筛选
      #if tds[1].find('div').string == nowDay:
      title = tds[0].find('a').string
      title = title.split(' ')
      result.append([title[0],topUrl+tds[0].find('a').get('href')[2:],title[1].encode('utf8'),tds[1].find('div').string])
  return result

#抓取天津股权
#主要URL http://www.tjsoc.com
#抓取URL http://www.tjsoc.com/web/infor.aspx?cid=3
def dumpTJGQ():
  result = []
  url = 'http://www.tjsoc.com/web/infor.aspx?cid=3'
  subUrl = 'http://www.tjsoc.com/web/'
  opener = urllib2.build_opener(encoding_support,urllib2.HTTPHandler)
  html_doc = opener.open(url).read()
  soup = BeautifulSoup(html_doc)

  ul = soup.find('ul',"newslist")
  lis = ul.find_all('li')
  for li in lis:
    #print li
    #print subUrl+li.find('a').get('href').encode('utf8')
    #print li.find('a').string.encode('utf8').strip()
    #print li.find('span').string
    result.append(['',subUrl+li.find('a').get('href').encode('utf8'),li.find('a').string.encode('utf8').strip(),li.find('span').string])
  return result



#抓取新闻
def dumpNews():
  #dumpZXGZ()
  #dumpSHGQ()
  dumpTJGQ()

if __name__ == '__main__':
  dumpNews()