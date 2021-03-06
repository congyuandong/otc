#coding:utf-8
import	sys,os
from datetime import *
from threading import Timer
import time
from tasks.dumpnews1 import *
from tasks.dumpOtc import *
from tasks.dumpOtc1 import *
from tasks.dumpIndustry import *
from tasks.dumpTotamount import *
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
	print '抓取中小型企业新闻'
	
	zxgzNews = dumpZXGQ()
	if zxgzNews:
		for new in zxgzNews:
			found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
			if not found:
				n = otc_new(new_region=region.objects.get(reg_name='中小股转'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
				n.save()
				print '存储数据',new[0],new[1]
			
	else:
		print '中小型抓取新闻失败2'
	
	
	print '抓取上海新闻'
	shgqNews = dumpSHGQ()
	if shgqNews:
		for new in shgqNews:
			found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
			if not found:
				n = otc_new(new_region=region.objects.get(reg_name='上海'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
				n.save()
				print '存储数据',new[0],new[1],new[2]
	else:
		print '上海新闻抓取失败2'
		#else:
		#	print '已经存在数据',new[0],new[1],new[2]
	
	print'抓取天津新闻'
	tjgqNews = dumpTJGQ()
	if tjgqNews:
		for new in tjgqNews:
			found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
			if not found:
				n = otc_new(new_region=region.objects.get(reg_name='天津'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
				n.save()
				print '存储数据',new[0],new[1],new[2]
	else:
		print '天津新闻抓取失败'
		#else:
		#	print '已经存在数据',new[0],new[1],new[2]
	print'抓取齐鲁新闻'
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
	print '抓取重庆新闻'
	cqgqNews = dumpCQGQ()
	if cqgqNews:
		for new in cqgqNews:
			found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
			if not found:
				n = otc_new(new_region=region.objects.get(reg_name='重庆'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
				n.save()
				print '存储数据',new[0],new[1],new[2]
	else:
		print '重庆新闻抓取失败2'
		#else:
		#	print '已经存在数据',new[0],new[1],new[2]
	
	print '抓取浙江新闻'
	
	zjgqNews = dumpZJGQ()
	if zjgqNews:
		for new in zjgqNews:
			found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
			if not found:
				n=otc_new(new_region=region.objects.get(reg_name='浙江'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
				n.save()
				print '存储数据',new[0],new[1],new[2]
	else:
		print '浙江新闻抓取失败2'
		#else:
		#	print '已经存在数据',new[0],new[1],new[2]
	
	print '抓取广州新闻'
	gzgqNews = dumpGZGQ()
	if gzgqNews:
		for new in gzgqNews:
			found = otc_new.objects.filter(new_code=new[0],new_url=new[1],new_title=new[2])
			if not found:
				n = otc_new(new_region=region.objects.get(reg_name='广州'),new_code=new[0],new_title=new[2],new_url=new[1],new_date=new[3])
				n.save()
				print '存储数据',new[0],new[1],new[2]
	else:
		print '广州新闻抓取失败2'
		#else:
			#print '已经存在数据',new[0],new[1],new[2]

def dump_industry():
	'''
	tjcomp=TJCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='天津'))
	if tjcomp:
		if str(comp.in_num)!=str(tjcomp):
			print '更新天津挂牌'
			comp.in_num=tjcomp
			comp.in_date=date.today()
			comp.save()
			print comp.in_num
	
	xjcomp=XJCOMP()
	#print int(xjcomp)
	comp=industry.objects.get(in_region=region.objects.get(reg_name='新疆'))
	if xjcomp:
		if str(comp.in_num)!=str(xjcomp):
			print '更新新疆挂牌'
			print comp.in_num
			comp.in_num=int(xjcomp)
			print int(xjcomp)
			print comp.in_num
			comp.in_date=date.today()
			comp.save()
			print comp.in_num
	'''
	jscomp=JSCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='江苏'))
	if jscomp: 
		if str(comp.in_num)!=jscomp:
			print '更新江苏挂牌'
			print str(comp.in_num)
			comp.in_num=jscomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '江苏挂牌更新成功！'
	

	
	

	
	gzcomp=GZCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='广州'))
	if gzcomp:
		if str(comp.in_num)!=gzcomp:
			print '更新广州挂牌'
			print str(comp.in_num)
			comp.in_num=gzcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '广州挂牌更新成功！'

	whcomp=WHCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='武汉'))
	if whcomp:
		if str(comp.in_num)!=whcomp:
			print '更新武汉挂牌'
			print str(comp.in_num)
			comp.in_num=whcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '武汉挂牌更新成功！'
	
	sxcomp=SXCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='山西'))
	if sxcomp:
		if str(comp.in_num)!=sxcomp:
			print '更新山西挂牌'
			print str(comp.in_num)
			comp.in_num=sxcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '山西挂牌更新成功'
	
	qlcomp=QLCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='齐鲁'))
	if qlcomp:
		if str(comp.in_num)!=qlcomp:
			print '更新齐鲁挂牌'
			print str(comp.in_num)
			comp.in_num=qlcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '齐鲁挂牌更新成功'

	lncomp=LNCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='辽宁'))
	if lncomp:
		if str(comp.in_num)!=lncomp:
			print '更新辽宁挂牌'
			print str(comp.in_num)
			comp.in_num=lncomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '辽宁挂牌更新成功！'

	zjcomp=ZJCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='浙江'))
	if zjcomp:
		if str(comp.in_num)!=zjcomp:
			print '更新浙江挂牌'
			print str(comp.in_num)
			comp.in_num=zjcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '浙江挂牌更新成功！'
	bjcomp=BJCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='北京'))
	if bjcomp:
		if str(comp.in_num)!=bjcomp:
			print '更新北京挂牌'
			print str(comp.in_num)
			comp.in_num=bjcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '北京挂牌更新成功！'
	
	hxcomp=HXCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='海峡'))
	if bjcomp:
		if str(comp.in_num)!=hxcomp:
			print '更新海峡挂牌'
			print str(comp.in_num)
			comp.in_num=hxcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '海峡挂牌更新成功！'
	shcomp=SHCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='上海'))
	if shcomp:
		if str(comp.in_num)!=str(shcomp):
			print '更新上海挂牌'
			print str(comp.in_num)
			comp.in_num=shcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '上海挂牌更新成功！'
	'''
	ahcomp=AHCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='安徽'))
	if ahcomp:
		if str(comp.in_num)!=ahcomp:
			print '更新安徽挂牌'
			print str(comp.in_num)
			comp.in_num=ahcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '安徽挂牌更新成功！'
	'''
	cqcomp=CQCOMP()
	comp=industry.objects.get(in_region=region.objects.get(reg_name='重庆'))
	if cqcomp:
		if str(comp.in_num)!=str(cqcomp):
			print '更新重庆挂牌'
			print str(comp.in_num)
			comp.in_num=cqcomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '重庆挂牌更新成功！'
	
	gscomp=GSCOMP()
	print gscomp
	comp=industry.objects.get(in_region=region.objects.get(reg_name='甘肃'))
	if gscomp:
		if str(comp.in_num)!=gscomp:
			print '更新甘肃挂牌'
			print str(comp.in_num)
			comp.in_num=gscomp
			print str(comp.in_num)
			comp.in_date=date.today()
			comp.save()
			print '甘肃挂牌更新成功！'

	qhcomp=QHCOMP()
	f=open('num.txt')
	qhcompold=f.readline()
	print qhcompold
	comp=industry.objects.get(in_region=region.objects.get(reg_name='前海'))
	if qhcomp:
		if int(qhcompold)<int(qhcomp):
			print '更新前海挂牌'
			print str(comp.in_num)
			comp.in_num=comp.in_num+int(qhcomp)-int(qhcompold)
			f=file('num.txt','w')
			f.write(qhcomp)
			comp.in_date=date.today()
			comp.save()
			print '前海挂牌更新成功！'
		if int(qhcompold)>int(qhcomp):
			comp.in_num=comp.in_num+int(qhcomp)
			f=file('num.txt','w')
			f.write(qhcomp)
			comp.in_date=date.today()
			comp.save()


def dump_totamount():
	otcs=dump_chinasee()
	OTC_objs = OTC.objects.all()
	for OTC_obj in OTC_objs:
		if otcs.has_key(OTC_obj.otc_code):
			if str(round(OTC_obj.otc_tot_amount,1))!=str(float(otcs[OTC_obj.otc_code])*10000):
				print str(round(OTC_obj.otc_tot_amount,1))
				OTC_obj.otc_tot_amount=str(float(otcs[OTC_obj.otc_code])*10000)
				OTC_obj.save()
				#print '更新成功'
				print OTC_obj.otc_name.encode('utf8')+'更新成功'
				print str(float(otcs[OTC_obj.otc_code])*10000)
				print str(OTC_obj.otc_tot_amount)


	#print otcs

#计算市场容量指数
def anaIndustryIndex():
	#假定2013年1月16日公司总数为3189家
	base_comp = 3189.0
	tot_comp = 0.0

	industry_objs = industry.objects.all()
	for industry_obj in industry_objs:
		tot_comp += industry_obj.in_num

	#计算指数
	index = round(tot_comp/base_comp*100,2)
	print str(index)
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
	#print otcs
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
					#OTC_obj.otc_tot_price = str(float(otcs[OTC_obj.otc_code]['latest_price']) * (float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume'])))
					OTC_obj.otc_tot_price=str(float(otcs[OTC_obj.otc_code]['latest_price'])*float(OTC_obj.otc_tot_amount)/1000000)
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
					#OTC_obj.otc_tot_price = str(float(otcs[OTC_obj.otc_code]['latest_price']) * (float(OTC_obj.otc_amount) + float(otcs[OTC_obj.otc_code]['volume']) - float(otc_deal_objs[0].od_volume)))
					#tot_price=float(otcs[OTC_obj.otc_code]['latest_price'])*float(OTC_obj.otc_tot_amount)
					OTC_obj.otc_tot_price = str(float(otcs[OTC_obj.otc_code]['latest_price']) * float(OTC_obj.otc_tot_amount)/1000000)
					#print OTC_obj.otc_tot_price
					#OTC_obj.otc_tot_price=str(float(otcs[OTC_obj.otc_code]['latest_price'])*float(OTC_obj.otc_tot_amount))
					
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
	#假定2014年1月1日市场总值为10041.7065M
	baseOtcIndex = 10041.7065
	totOTCIndex = 0

	OTC_objs = OTC.objects.all()

	for OTC_obj in OTC_objs:
		totOTCIndex += OTC_obj.otc_tot_price

	#计算市场指数	
	OTCindex = round(float(totOTCIndex)/baseOtcIndex*100,2)
	print str(totOTCIndex)
	oi_objs = otc_index.objects.filter(oi_date=date.today())
	if oi_objs:
		oi_objs[0].oi_index = str(OTCindex)
		oi_objs[0].oi_amount = totOTCIndex
		oi_objs[0].save()

		otc_base_last = otc_base.objects.order_by('base_date')
		if otc_base_last:
			otc_base_last[0].base_index = str(OTCindex)
			otc_base_last[0].base_trans = totOTCIndex
			otc_base_last[0].base_date = date.today()
			otc_base_last[0].save()

		print '更新市场指数'
	else:
		oi_obj_new = otc_index(oi_date=date.today(),oi_index=str(OTCindex),oi_amount=totOTCIndex)
		oi_obj_new.save()

		otc_base_last = otc_base.objects.order_by('base_date')
		if otc_base_last:
			otc_base_last[0].base_index = str(OTCindex)
			otc_base_last[0].base_trans = totOTCIndex
			otc_base_last[0].base_date = date.today()
			otc_base_last[0].save()

		print '插入市场指数'

def runTasks():
	print '开始抓取新闻'
	dump_otc_news()
	
	print '开始更新市场容量'
	dump_industry()
	#print '开始更新总股本'
	dump_totamount()
	print '开始抓取交易数据'
	dump_otc()
	print '开始计算市场容量指数'
	anaIndustryIndex()
	#sync_otc_base()
	print '开始计算市场指数'
	anaOtcIndex()
	schedule()

def schedule():
	print time.strftime('%H:%M:%S',time.localtime(time.time()))
	timer_interval = 1200
	task = Timer(timer_interval,runTasks)
	print '开始再次抓取'
	task.start()

if __name__ == '__main__':
	
	runTasks()
	#dump_otc()
	#anaOtcIndex()

	
