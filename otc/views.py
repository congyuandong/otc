#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import simplejson as json

from otc.models import industry,otc_new

def index(request):
	otc_new_list = otc_new.objects.all()
	print otc_new_list
	context = {'otc_new_list':otc_new_list}
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