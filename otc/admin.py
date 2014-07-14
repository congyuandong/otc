#coding:utf-8
from django.contrib import admin
from otc.models import OTC,industry,region,otc_new,otc_hot,otc_study,otc_base

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

class OTCStudyAdmin(admin.ModelAdmin):
	fields = ['stu_code','stu_title','stu_url','stu_date']
	list_display = ['stu_code','stu_title','stu_date']
	list_filter = ['stu_date']
	search_fields = ['stu_title']

class OTCHotAdmin(admin.ModelAdmin):
	fields = ['hot_sort','hot_company','hot_trans','hot_sum_trans']
	list_display = ['hot_sort','hot_company','hot_trans','hot_sum_trans']

class OTCBaseAdmin(admin.ModelAdmin):
	fields = ['base_date','base_index','base_company_index','base_trans','base_company']
	list_display = ['base_date','base_index','base_company_index','base_trans','base_company']

# Register your models here.
admin.site.register(industry,IndustryAdmin)
admin.site.register(region)
admin.site.register(otc_new,OTCNewAdmin)
admin.site.register(otc_hot,OTCHotAdmin)
admin.site.register(otc_study,OTCStudyAdmin)
admin.site.register(otc_base,OTCBaseAdmin)