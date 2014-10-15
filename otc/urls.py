from django.conf.urls import patterns, url
from otc import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^industry_pie/$', views.industry_pie, name='industry_pie'),
	url(r'^industry_column/$', views.industry_column, name='industry_column'),
	url(r'^industry_line_chart/$', views.industry_line_chart, name='industry_line_chart'),
	)