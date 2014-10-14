#coding:utf-8
import	sys,os
from datetime import *
from threading import Timer
import time
from tasks.dumpnews import *
os.environ['DJANGO_SETTINGS_MODULE'] ='scrapy.settings'
from django.conf import settings
#from django.contrib.auth.models import User, check_password
from otc.models import otc_base,otc_new,region,industry,industry_index


def sync_otc_base():
	otc_base_last = otc_base.objects.order_by('base_date')[:1]
	otc_base_item = otc_base.objects.get(id__exact=otc_base_last[0].id)
	otc_base_item.base_date = date.today()
	print otc_base_item.base_date
	otc_base_item.save()

#抓取新闻 包括中小股转，上海股交，其他股交
#code title url 日期
def dump_otc_news():
	zxgzNews = dumpZXGZ()
	for new in zxgzNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='中小股转'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]

	shgqNews = dumpSHGQ()
	for new in shgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='上海'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]

	tjgqNews = dumpTJGQ()
	for new in tjgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='天津'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]

#计算市场容量指数
def anaIndustryIndex():
	#假定2013年1月16日公司总数为651家
	base_comp = 651.0
	tot_comp = 0.0

	industry_objs = industry.objects.all()
	for industry_obj in industry_objs:
		tot_comp += industry_obj.in_num
	#计算指数
	index = round(tot_comp/base_comp*100,2)
	
	ii_objs = industry_index.objects.filter(ii_date=date.today())
	if ii_objs:
		ii_objs[0].ii_index = str(index)
		ii_objs[0].ii_company = tot_comp
		ii_objs[0].save()

		otc_base_last = otc_base.objects.order_by('base_date')
		if otc_base_last:
			otc_base_last[0].base_company_index = str(index)
			otc_base_last[0].base_company = tot_comp
			otc_base_last[0].base_date = date.today()
			otc_base_last[0].save()

		print '更新市场指数'
	else:
		ii_obj_new = industry_index(ii_date=date.today(),ii_index=str(index),ii_company=tot_comp)
		ii_obj_new.save()

		otc_base_last = otc_base.objects.order_by('base_date')
		if otc_base_last:
			otc_base_last[0].base_company_index = str(index)
			otc_base_last[0].base_company = tot_comp
			otc_base_last[0].base_date = date.today()
			otc_base_last[0].save()

		print '插入市场指数'


def runTasks():
	dump_otc_news()
	anaIndustryIndex()
	#sync_otc_base()
	schedule()

def schedule():
	timer_interval = 1200
	task = Timer(timer_interval,runTasks)
	task.start()

if __name__ == '__main__':
	runTasks()

	
