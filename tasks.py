import	sys,os
from datetime import *
from threading import Timer
import time
os.environ['DJANGO_SETTINGS_MODULE'] ='scrapy.settings'
from django.conf import settings
#from django.contrib.auth.models import User, check_password
from otc.models import otc_base

def sync_otc_base():
	otc_base_last = otc_base.objects.order_by('base_date')[:1]
	otc_base_item = otc_base.objects.get(id__exact=otc_base_last[0].id)
	#print otc_base_item.base_date
	#print date.today()
	otc_base_item.base_date = date.today()
	print otc_base_item.base_date
	otc_base_item.save()
	schedule()

def schedule():
	timer_interval = 600
	task = Timer(timer_interval,sync_otc_base)
	task.start()

if __name__ == '__main__':
	sync_otc_base()

	