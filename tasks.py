#coding:utf-8
import	sys,os
from datetime import *
from threading import Timer
import time
from tasks.dumpnews import dumpZXGZ
os.environ['DJANGO_SETTINGS_MODULE'] ='scrapy.settings'
from django.conf import settings
#from django.contrib.auth.models import User, check_password
from otc.models import otc_base,otc_new,region


def sync_otc_base():
	otc_base_last = otc_base.objects.order_by('base_date')[:1]
	otc_base_item = otc_base.objects.get(id__exact=otc_base_last[0].id)
	otc_base_item.base_date = date.today()
	print otc_base_item.base_date
	otc_base_item.save()

#抓取新闻 包括中小股转，上海股交，其他股交
def dump_otc_news():
	zxgz = dumpZXGZ()
	for new in zxgz:
		found = otc_new.objects.filter(new_code=new[0],new_title=new[1],new_url=new[2],new_date=new[3])
		if not found:
			n = otc_new(new_region=region.objects.get(reg_name='中小股转'),new_code=new[0],new_title=new[1],new_url=new[2],new_date=new[3])
			n.save()
			print '存储数据',new[0],new[1],new[2],new[3]
		else:
			print '已经存在数据',new[0],new[1],new[2],new[3]

def runTasks():
	sync_otc_base()
	dump_otc_news()
	schedule()

def schedule():
	timer_interval = 1200
	task = Timer(timer_interval,runTasks)
	task.start()

if __name__ == '__main__':
	runTasks()

	