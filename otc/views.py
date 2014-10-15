#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import simplejson as json

from otc.models import industry,otc_new,otc_hot,otc_study,otc_base,OTC,industry_index

def index(request):
	otc_new_list_sanban = otc_new.objects.filter(new_region__reg_name__exact='中小股转').order_by('-id')[:7]
	otc_new_list_shanghai = otc_new.objects.filter(new_region__reg_name__exact='上海').order_by('-id')[:7]
	otc_new_list_other = otc_new.objects.exclude(new_region__reg_name__exact='上海').exclude(new_region__reg_name__exact='中小股转').order_by('-id')[:7]
	#otc_hot_list = otc_hot.objects.order_by('-hot_sum_trans')[:10]
	otc_hot_list = OTC.objects.order_by('-otc_amount')[:10]
	otc_study_list = otc_study.objects.order_by('stu_date')[:8]
	otc_base_last = otc_base.objects.order_by('base_date')[:1]
	context = {'otc_base_last':otc_base_last[0],'otc_new_list_sanban':otc_new_list_sanban,'otc_new_list_shanghai':otc_new_list_shanghai,'otc_new_list_other':otc_new_list_other,'otc_hot_list':otc_hot_list,'otc_study_list':otc_study_list}
	return render(request,'otc/index.html',context)

def industry_pie(request):
	#print 'industry_pie'
	industry_list = industry.objects.order_by('-in_num')
	#print industry_list
	response_data = []
	index = 1
	sumOfOth = 0
	for ind in industry_list:
		if index <= 5:
			per_ind = [ind.in_region.reg_name,ind.in_num]
			response_data.append(per_ind)
			#print	per_ind
			index = index + 1
		else:
			sumOfOth = sumOfOth + ind.in_num
	if sumOfOth != 0:
		response_data.append(['其他',sumOfOth])
	#print response_data
	return HttpResponse(json.dumps(response_data),content_type="application/json")

def industry_column(request):
	#print 'industry_column'
	industry_list = industry.objects.order_by('-in_num')
	response_data = []
	for ind in industry_list:
		per_ind = [ind.in_region.reg_name,ind.in_num]
		#print per_ind
		response_data.append(per_ind)
	return HttpResponse(json.dumps(response_data),content_type="application/json")

#市场容量指数图表
def industry_line_chart(request):
	
	response = {}
	scale_counts = {}
	scale_y = []
	scale_dates = []
	industry_index_objs = industry_index.objects.order_by('ii_date')

	for industry_index_obj in industry_index_objs:
		scale_y.append(float(industry_index_obj.ii_index))
		scale_dates.append((industry_index_obj.ii_date).strftime('%Y-%m-%d'))
		scale_counts[(industry_index_obj.ii_date).strftime('%Y-%m-%d')] = industry_index_obj.ii_company

	#print scale_y
	response['scale_counts'] = scale_counts
	response['scale_y'] = scale_y
	response['scale_dates'] = scale_dates
	response['scale_min_y'] = scale_y[0]
	response['scale_max_y'] = scale_y[-1]

	return HttpResponse(json.dumps(response),content_type="application/json")

