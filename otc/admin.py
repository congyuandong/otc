#coding:utf-8
from django.contrib import admin
from otc.models import OTC,industry,region,otc_new,otc_hot,otc_study,otc_base,industry_index,otc_deal

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

class IndustryIndexAdmin(admin.ModelAdmin):
	list_display = ['ii_date','ii_index','ii_company']

class OtcDealAdmin(admin.ModelAdmin):
	list_display = ['od_OTC','od_date','od_volume','od_price']
	list_filter = ['od_date']
	search_fields = ['od_date']

class OTCAdmin(admin.ModelAdmin):
	list_display = ['otc_name','otc_code','otc_amount','otc_per','otc_amount_per','otc_days','otc_date','otc_tot_amount','otc_last_price','otc_tot_price']


# Register your models here.
admin.site.register(industry,IndustryAdmin)
admin.site.register(region)
admin.site.register(otc_new,OTCNewAdmin)
admin.site.register(otc_hot,OTCHotAdmin)
admin.site.register(otc_study,OTCStudyAdmin)
admin.site.register(otc_base,OTCBaseAdmin)
admin.site.register(industry_index,IndustryIndexAdmin)
admin.site.register(otc_deal,OtcDealAdmin)
admin.site.register(OTC,OTCAdmin)