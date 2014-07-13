#coding:utf-8
from django.db import models



'''
地区
'''
class region(models.Model):
	reg_name = models.CharField(max_length=50,verbose_name='市场')
	def __unicode__(self):
		return self.reg_name
	class Meta:
		verbose_name = '市场'
		verbose_name_plural = '市场管理'

'''
产品代码
产品名称
地区
时间
成交方式 0 默认 1 买入 2 卖出
成交价     
成交量
成交额
成交总量
成交总额 
'''
class OTC(models.Model):
	otc_code = models.CharField(max_length=20)
	otc_name = models.CharField(max_length=100)
	otc_region = models.CharField(max_length=20)
	otc_date = models.DateField(verbose_name='成交日期')
	otc_type = models.IntegerField(default=0)
	otc_price = models.DecimalField(max_digits=15,decimal_places=5)
	otc_amount = models.DecimalField(max_digits=15,decimal_places=5)
	otc_tot_price = models.DecimalField(max_digits=15,decimal_places=5)
	otc_tot_amount = models.DecimalField(max_digits=15,decimal_places=5)

	def __unicode__(self):
		return self.otc_code

'''
行业方向
公司数量
'''
class industry(models.Model):
	in_region = models.ForeignKey(region,verbose_name='市场')
	in_date = models.DateField(verbose_name="日期")
	in_num = models.IntegerField(default=0,verbose_name='挂牌企业数量')


	#def __unicode__(self):
	#	return self.in_num

	class Meta:
		verbose_name = '市场容量'
		verbose_name_plural = '市场容量'


'''
otc公告
编号  文档名字 URL 市场 公布日期
'''
class otc_new(models.Model):
	new_region = models.ForeignKey(region,verbose_name='市场')
	new_code = models.CharField(max_length = 30,verbose_name='编号')
	new_title = models.CharField(max_length = 100,verbose_name='标题')
	new_url = models.CharField(max_length = 300,verbose_name='URL')
	new_date = models.DateField(verbose_name='公布日期')

	def __unicode__(self):
		return self.new_title

	class Meta:
		verbose_name = 'OTC公告'
		verbose_name_plural = 'OTC公告'
