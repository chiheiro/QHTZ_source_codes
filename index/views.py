from django.shortcuts import render,redirect
from time import time
from functools import wraps
from django.http import HttpRequest
from django.urls import reverse
from django.views.generic import View
import markdown
import re
from .models import *
from django.utils.safestring import mark_safe
import requests


#从接口中获得IP地址的所在地区的装饰器
def Ip_deal(func):
	@wraps(func)
	def deal(self,request):
		if 'HTTP_X_FORWARDED_FOR' in request.META:
			ip = request.META['HTTP_X_FORWARDED_FOR']
		else:
			ip = request.META['REMOTE_ADDR']
		try:
			r=requests.post(url='http://ip.taobao.com/service/getIpInfo2.php', data={'ip': ip})
			alldata = r.json()
			data = alldata['data']
		except Exception as f:
			data = "暂未获取到地区"
		if func.__name__ == "get":
			return func(self,request,ip)
		elif func.__name__ == "post":
			return func(self,request,ip,data)
	return deal

#从数据库获取数据进行处理的装饰器，返回值的列表
def python_deal(func):
	@wraps(func)
	def python(self,request):
		values_list = list()
		py_list = PythonProduct.objects.all().values_list()
		for i in py_list:
		#创建列表，字典存储值
			values_list.append(i)
		return func(self,request,values_list)
	return python
	
		
#首页
class IndexView(View):
	@Ip_deal
	def get(self,request,ip):
		#ip地址访问次数
		try:
			traffic = Traffic.objects.get(traffic_ip=ip)
		except Exception as f:
			Traffic.objects.create(traffic_ip=ip,view_times=1)
			view_list = None
			web_load = 'preloader'
		else:
			try:
				request.session['username']
			except Exception as f:
				web_load = "preloader"
				request.session.set_expiry(60)
				request.session['username'] = 'QHTZ'
				traffic.view_times += 1
				traffic.save()
				view_list = None
			else:
				web_load = ''
		count = 0
		view_list = Traffic.objects.all().values_list()
		for i in view_list:
			count += int(i[3])
		#session判断网页加载动画
		#首页关于我
		try:
			aboutme = IndexAboutMe.objects.get(show=True)
		except Exception as f:
			aboutme = "内容获取出错，请联系网站管理员修复"
		#创建存储图片名的列表
		image_list = []
		try:
			images = IndexImages.objects.all()
		except Exception as f:
			raise IndexImages.DoesNotExist("数据不存在")
		for image in images.values_list():
			if image[5]:
				image_list.append(image[1])
		context = {	'aboutme':aboutme,
					'images':image_list,
					'view_times':count,
					'web_load':web_load,
				}
		return render(request,'index.html',context)


class StaticView(View):
	def get(self,request):
		return render(request,'smellimage.html')


#UI作品页面
class UIProductImagesView(View):
	def get(self,request):
		try:
			UI = ProductImages.objects.all()
		except Exception as f:
			raise ValueError("please connect admin")
		image_list = []
		for i in UI.values_list():
			image = i[1]
			statue = i[5]
			if image and statue:
				image_list.append(image)
			else:
				raise ValueError("值错误")
		context = {"image":image_list}
		return render(request,"UIproduct.html",context)


class PythonDetail(View):
	def get(self,request):
		#获取url
		full_url = request.get_full_path()
		urls_list = re.findall(r"[0-9]+",full_url)
		if int(len(urls_list)) != 1:
			return render(request,'404.html')
		content_id = int(urls_list[0])
		#获取标题和内容
		try:
			contents = PythonProduct.objects.get(id=content_id)
		except Exception as f:
			return render(request,'404.html')
		else:
			contents.content = markdown.markdown(contents.content,
										extensions=[
										'markdown.extensions.extra',
										'markdown.extensions.codehilite',
										'markdown.extensions.toc',
										])
			return render(request, 'detail.html', context={'content': contents})

	
#python文章详情页面
class PythonProductView(View):
	@python_deal
	def get(self,request,values_list):
		id_list = []
		for i in values_list:
			id = i[0]
			id_list.append(id)
		id_list.reverse()
		#print(id_list,title_list,body_list)
		context = {
					"id_list":id_list,
				}
		return render(request,'pythonproduct.html',context)


#选择作品页面
class ChooseProductView(View):
	def get(self,request):
		return render(request,'choose_product.html')


#简历访问信息记录
class CheckJianliView(View):
	def get(self,request):
		return render(request,'check_jianli.html')
	@Ip_deal
	def post(self,request,ip,data):
		check = request.POST.get('check')
		try:
			country,regionname,city,isp = data['country'],data['region'],data['city'],data['isp']
			regionname += '省'
			city += '市'
			region = country + '，' + regionname + '，' + city + ' ' + isp
		except Exception as f:
			region = '从接口获取ip地址失败'
		if check == 'jianli1':
			try:
				CheckJianli.objects.create(usertype='公司',ipaddr=ip,area=region)
			except Exception as f:
				return render(request,'404.html')
			html_a = mark_safe("/static/images/jianli1.pdf")
			context = {"words":html_a}
			return render(request,'jianli.html',context)
		elif check == 'jianli2':
			try:
				CheckJianli.objects.create(usertype='个人',ipaddr=ip,area=region)
			except Exception as f:
				return render(request,'404.html')
			html_a = mark_safe("/static/images/jianli2.pdf")
			context = {"words":html_a}
			return render(request,'jianli.html',context)


#联系我
class ConnectView(View):
	def get(self,request):
		return render(request,'connect.html')


#合作检查
class CheckCooperationView(View):
	def get(self,request):
		return render(request,'check_cooperation.html')


#合作
class CooperationView(View):
	def get(self,request):
		return render(request,'cooperation.html')
