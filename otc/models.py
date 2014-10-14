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

'''
OTC表
用于存储交易总数据
字段	挂牌市场 外键
	产品代码
	公司名称
	总交易数量(股)
	交易比例
	日均交易量（股）
	已挂牌天数
	总股本(股)
'''
class OTC(models.Model):
	otc_region = models.ForeignKey(region,verbose_name='挂牌市场')
	otc_code = models.CharField(max_length=20,verbose_name='代码')
	otc_name = models.CharField(max_length=100,verbose_name='名称')
	otc_amount = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='总成交数量(股)')
	otc_per = models.DecimalField(max_digits=10,decimal_places=5,verbose_name='交易比例')
	otc_amount_per = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='日均交数量(股)')
	otc_days = models.IntegerField(verbose_name='已挂牌天数',default=0)
	otc_date = models.DateField(verbose_name='挂牌日期')
	otc_tot_amount = models.DecimalField(max_digits=15,decimal_places=5,verbose_name='总股本(股)')




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

'''
otc研告
编号  文档名字 URL 市场 公布日期
'''
class otc_study(models.Model):
	stu_code = models.CharField(max_length = 30,verbose_name='编号')
	stu_title = models.CharField(max_length = 100,verbose_name='标题')
	stu_url = models.FileField(verbose_name='文件',upload_to='pdf')
	stu_date = models.DateField(verbose_name='日期')

	def __unicode__(self):
		return self.stu_title

	class Meta:
		verbose_name = 'OTC研告'
		verbose_name_plural = 'OTC研告'

'''
近期热门证券
公司名称 最新成交价 累计成交量
'''
class otc_hot(models.Model):
	hot_sort = models.IntegerField(default=0,verbose_name="热度")
	hot_company = models.CharField(max_length=30,verbose_name="公司简称")
	hot_trans = models.DecimalField(max_digits=15,decimal_places=5,verbose_name="最新成交价")
	hot_sum_trans = models.DecimalField(max_digits=15,decimal_places=5,verbose_name="累计成交量")

	def __unicode__(self):
		return self.hot_company

	class Meta:
		verbose_name = '近期热门证券'
		verbose_name_plural = '热门证券'

'''
基础数据
成分指数 市场容量指数 最新市值 总挂牌企业数量
'''
class otc_base(models.Model):
	base_date = models.DateField(verbose_name='日期')
	base_index = models.DecimalField(max_digits=15,decimal_places=5,verbose_name="成分指数")
	base_company_index =models.DecimalField(max_digits=15,decimal_places=5,verbose_name="市场容量指数")
	base_trans = models.DecimalField(max_digits=15,decimal_places=5,verbose_name="最新市值")
	base_company = models.DecimalField(max_digits=15,decimal_places=5,verbose_name="总挂牌企业数量")

	class Meta:
		verbose_name = "基础数据"
		verbose_name_plural = "基础数据"



