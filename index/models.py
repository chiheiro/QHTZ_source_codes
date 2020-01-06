from django.db import models
from QHTZ.settings import MEDIA_URL
from imagestorage.storage import ImageStorage,HelpInfo,Self_int
from mdeditor.fields import MDTextField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver



#创建网页提交用户的信息表
class UserMessages(models.Model):
	name = models.CharField(max_length=4,verbose_name="名字",null=False)
	phonenumber = models.CharField(max_length=11,verbose_name="手机号码",null=False)
	time = models.DateField(auto_now=True,verbose_name="创建时间")
	#定义后台更改页面显示内容
	def __str__(self):
		return self.name
	#定义后台页面的排序方式
	def title(self):
		return self.time
		title.admin_order_field = "time"
	#定义数据库表名称以及后台查询页显示内容
	class Meta():
		db_table = 'QHTZ_user_input'
		verbose_name = '用户信息'
		verbose_name_plural = verbose_name

#首页轮播图
class IndexImages(models.Model):
	image = models.ImageField(upload_to=MEDIA_URL,storage=ImageStorage(),null=False,blank=True,verbose_name="选择要上传的图片")
	imagename = models.CharField(max_length=20,null=False,default="未命名图片",verbose_name="首页图片名")
	upldtime = models.DateField(auto_now=True,verbose_name="上传时间")
	chatime = models.DateField(auto_now=True,verbose_name="最后更改时间")
	show = models.BooleanField(default=True,verbose_name="是否展示")
	def __str__(self):
		return self.imagename
		return self.show
	def title(self):
		return self.upltime
		title.admin_order_field = "upltime"
	class Meta():
		db_table = "QHTZ_index_images"
		verbose_name = "首页轮播图"
		verbose_name_plural = verbose_name


#创建作品页轮播图上传图片的存储表
class ProductImages(models.Model):
	image = models.ImageField(upload_to=MEDIA_URL,storage=ImageStorage(),null=False,blank=True,verbose_name="选择图片")
	imagename = models.CharField(max_length=20,null=False,default="未命名图片",verbose_name="图片名")
	upldtime = models.DateField(auto_now=True,verbose_name="上传时间")
	chatime = models.DateField(auto_now=True,verbose_name="最后更改时间")
	show = models.BooleanField(default=True,verbose_name="是否展示")
	def __str__(self):
		return self.imagename
		return self.show

	def title(self):
		return self.upldtime
		title.admin_order_field = "upltime"

	class Meta():
		db_table = "QHTZ_product_images"
		verbose_name = "UI作品展示"
		verbose_name_plural = verbose_name

class BackstageRecord(models.Model):
	pass
	#登陆时间
	#登录IP
	#是否成功


#创建python作品中文章模型
class PythonProduct(models.Model):
	#标题
	title = models.CharField(max_length=130,null=False,default="未命名文章",verbose_name="标题")
	#正文使用markdown的文本类型
	content = MDTextField(default=HelpInfo().info(),verbose_name="内容")
	mktime = models.DateField(auto_now_add=True,verbose_name="创建时间")
	edittime  = models.DateField(auto_now=True,verbose_name="最后修改时间")
	def __str__(self):
		return self.title
		return self.content
	class Meta():
		db_table = "QHTZ_Python_contents"
		verbose_name = "python文章"
		verbose_name_plural = verbose_name

#首页关于我
class IndexAboutMe(models.Model):
	self_int_now= models.CharField(max_length=100,verbose_name="首页关于我:",null=False,default=Self_int().info())
	show = models.BooleanField(default=False,verbose_name="是否首页显示")
	def __str__(self):
		return self.self_int_now
		return self.show
	class Meta():
		db_table = "QHTZ_index_about_me"
		verbose_name = '首页关于我'
		verbose_name_plural = verbose_name

#简历信息记录
class CheckJianli(models.Model):
	usertype = models.CharField(max_length=20,verbose_name="访问者类型")
	ex_time = models.DateTimeField(auto_now_add=True,verbose_name="访问时间")
	area = models.CharField(max_length=30,default='中国,北京(默认地址)',verbose_name="访问者所在地区")
	ipaddr = models.CharField(max_length=15,default='127.0.0.1',verbose_name="访问者IP")
	tips = models.CharField(max_length=35,default='注意：此项所有内容仅供查看,不可更改')
	def __str__(self):
		return self.usertype
		return self.ex_time
		return self.ipaddr
		return self.tops
		return self.area
	class Meta():
		db_table = "QHTZ_checkjianli"
		verbose_name = "简历访问记录"
		verbose_name_plural = verbose_name

@receiver(pre_delete, sender=IndexImages)
def mymodel_delete(sender, instance, **kwargs):
    # 删除数据库数据时，文件目录中的文件也删除
    instance.image.delete(False)

#网站访问量统计
class Traffic(models.Model):
	traffic_ip = models.CharField(max_length=15,verbose_name='访问IP')
	view_time = models.DateTimeField(auto_now=True,verbose_name='访问时间')
	view_times = models.IntegerField(default=0,verbose_name='访问次数')
	def __str__(self):
		return self.traffic_ip
		return view_time
		return view_times
	class Meta():
		db_table= "QHTZ_traffic"
		verbose_name = "网站访问记录"
		verbose_name_plural = verbose_name
