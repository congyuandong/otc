#coding:utf-8
import	sys,os
from datetime import *
from threading import Timer
import time
from tasks.dumpnews import *
from tasks.dumpOtc import *
from tasks.dumpOtc1 import *
os.environ['DJANGO_SETTINGS_MODULE'] ='scrapy.settings'
from django.conf import settings
#from django.contrib.auth.models import User, check_password
from otc.models import otc_base,otc_new,region,industry,industry_index,OTC,otc_deal,otc_index


def sync_otc_base():
	otc_base_last = otc_base.objects.order_by('base_date')[:1]
	otc_base_item = otc_base.objects.get(id__exact=otc_base_last[0].id)
	otc_base_item.base_date = date.today()
	print otc_base_item.base_date
	otc_base_item.save()

#抓取新闻 包括中小股转，上海股交，其他股交
#code title url 日期
def dump_otc_news():
	print '中小型企业新闻抓取'
	'''
	zxgzNews = dumpZXGZ()
	for new in zxgzNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='中小股转'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]
	'''
	'''
	shgqNews = dumpSHGQ()
	for new in shgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='上海'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]
	'''

	tjgqNews = dumpTJGQ()
	print '天津新闻抓取'
	for new in tjgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='天津'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]
	
	'''
	qlgqNews = dumpQLGQ()
	for new in qlgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='齐鲁'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]
	'''
	cqgqNews = dumpCQGQ()
	print '重庆新闻抓取'
	for new in cqgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='重庆'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]
	'''
	zjgqNews = dumpZJGQ()
	for new in zjgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n=otc_new(new_region=region.objects.get(reg_name='浙江'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2]
		else:
			print '已经存在数据',new[0],new[1],new[2]
	'''
	gzgqNews = dumpGZGQ()
	print '广州新闻抓取'
	for new in gzgqNews:
		found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='广州'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
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
		#市场挂牌企业数
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

		print '更新市场容量指数'
	else:
		ii_obj_new = industry_index(ii_date=date.today(),ii_index=str(index),ii_company=tot_comp)
		ii_obj_new.save()

		otc_base_last = otc_base.objects.order_by('base_date')
		if otc_base_last:
			otc_base_last[0].base_company_index = str(index)
			otc_base_last[0].base_company = tot_comp
			otc_base_last[0].base_date = date.today()
			otc_base_last[0].save()

		print '插入市场容量指数'

#抓取场外市场数据
def dump_otc():
	otcs = dumpotc1()
	#print type(otcs)
	OTC_objs = OTC.objects.all()
	for OTC_obj in OTC_objs:
		#如果有该公司的交易数据
		if otcs.has_key(OTC_obj.otc_code):
			#判断是否已经计算该记录数据，如果计算了就更新，如果是新的就插入
			#print otcs[OTC_obj.otc_code]['date']
			od_date = datetime.strptime(otcs[OTC_obj.otc_code]['date'], "%Y%m%d")
			otc_deal_objs = otc_deal.objects.filter(od_OTC = OTC_obj,od_date = od_date)
			if not otc_deal_objs:
				otc_deal_new = otc_deal(od_OTC = OTC_obj,od_date = od_date,od_volume = str(otcs[OTC_obj.otc_code]['volume']),od_price = str(otcs[OTC_obj.otc_code]['latest_price']))
				otc_deal_new.save()

				OTC_obj.otc_per = str((float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']))/float(OTC_obj.otc_tot_amount))
				OTC_obj.otc_amount_per = str((float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']))/(OTC_obj.otc_days+1))
				if otcs[OTC_obj.otc_code]['latest_price'] != 0:
					OTC_obj.otc_tot_price = str(float(otcs[OTC_obj.otc_code]['latest_price']) * (float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume'])))
				OTC_obj.otc_days += 1
				OTC_obj.otc_amount = str(float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']))
				if otcs[OTC_obj.otc_code]['latest_price'] != 0:
					OTC_obj.otc_last_price = str(otcs[OTC_obj.otc_code]['latest_price'])
				OTC_obj.save()

				print '增加市场容量'
			else:
				
				OTC_obj.otc_per = str((float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']) - float(otc_deal_objs[0].od_volume))/float(OTC_obj.otc_tot_amount))
				OTC_obj.otc_amount_per = str((float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']) - float(otc_deal_objs[0].od_volume))/OTC_obj.otc_days)
				if otcs[OTC_obj.otc_code]['latest_price'] != 0:
					OTC_obj.otc_tot_price = str(float(otcs[OTC_obj.otc_code]['latest_price']) * (float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']) - float(otc_deal_objs[0].od_volume)))
				OTC_obj.otc_amount = str(float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']) - float(otc_deal_objs[0].od_volume))
				if otcs[OTC_obj.otc_code]['latest_price'] != 0:
					OTC_obj.otc_last_price = str(otcs[OTC_obj.otc_code]['latest_price'])
				OTC_obj.save()
				
				otc_deal_objs[0].od_volume = str(otcs[OTC_obj.otc_code]['volume'])
				if otcs[OTC_obj.otc_code]['latest_price'] != 0:
					otc_deal_objs[0].od_price = str(otcs[OTC_obj.otc_code]['latest_price'])
				otc_deal_objs[0].save()

				print '更新市场容量'

#计算市场的交易指数
def anaOtcIndex():
	#假定2014年1月1日市场总值为1041.7065M
	baseOtcIndex = 1041.7065
	totOTCIndex = 0

	OTC_objs = OTC.objects.all()

	for OTC_obj in OTC_objs:
		#总市场交易值
		totOTCIndex += OTC_obj.otc_tot_price

	#计算市场指数	
	OTCindex = round(float(totOTCIndex)/100000/baseOtcIndex*100,2)
	#otc_index
	oi_objs = otc_index.objects.filter(oi_date=date.today())
	if oi_objs:
		#otc_index改变
		oi_objs[0].oi_index = str(OTCindex)
		oi_objs[0].oi_amount = totOTCIndex/100000
		oi_objs[0].save()
		#otc_base基础数据改变
		otc_base_last = otc_base.objects.order_by('base_date')
		if otc_base_last:
			otc_base_last[0].base_index = str(OTCindex)
			otc_base_last[0].base_trans = totOTCIndex/100000
			otc_base_last[0].base_date = date.today()
			otc_base_last[0].save()

		print '更新市场指数'
	else:
		oi_obj_new = otc_index(oi_date=date.today(),oi_index=str(OTCindex),oi_amount=totOTCIndex/100000)
		oi_obj_new.save()

		otc_base_last = otc_base.objects.order_by('base_date')
		if otc_base_last:
			otc_base_last[0].base_index = str(OTCindex)
			otc_base_last[0].base_trans = totOTCIndex/100000
			otc_base_last[0].base_date = date.today()
			otc_base_last[0].save()

		print '插入市场指数'

def runTasks():
	print '开始抓取新闻'
	dump_otc_news()
	print '开始抓取交易数据'
	dump_otc()
	print '开始计算市场容量指数'
	anaIndustryIndex()
	#sync_otc_base()
	print '开始计算市场指数'
	anaOtcIndex()
	schedule()

def schedule():
	timer_interval = 1200
	task = Timer(timer_interval,runTasks)
	task.start()

if __name__ == '__main__':
	runTasks()
	#dump_otc()
	#anaOtcIndex()

	
