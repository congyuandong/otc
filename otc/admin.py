#coding:utf-8
from django.contrib import admin
from otc.models import OTC,industry,region,otc_new

class IndustryAdmin(admin.ModelAdmin):
	fields = ['in_region','in_date','in_num']
	list_display = ['in_region','in_date','in_num']
	list_filter = ['in_region','in_date']
	search_fields = ['in_date']

class OTCNewAdmin(admin.ModelAdmin):
	fields = ['new_region','new_code','new_title','new_url','new_date']
	list_display = ['new_region','new_code','new_title','new_date']
	list_filter = ['new_region','new_date']
	search_fields = ['new_code','new_title']

# Register your models here.
admin.site.register(industry,IndustryAdmin)
admin.site.register(region)
admin.site.register(otc_new,OTCNewAdmin)