from QHTZ import settings
from celery import Celery
from index.models import *
from django_redis import get_redis_connection
from django.shortcuts import render,redirect
from django.template import loader,RequestContext
import os
app = Celery('celery_tasks.tasks',broker='redis://:nihao@127.0.0.1:6379/9')


@app.task
def index_html_static(self,request):
	#获取所有商品种类
	types = GoodsType.objects.all()
	#获取首页轮播图
	banners = IndexGoodsBanner.objects.all().order_by('index')
	#获取首页促销活动信息
	cuxiao = IndexPromotionBanner.objects.all().order_by('index')
	for type in types:
		image_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=1).order_by('index')
		title_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=2).order_by('index')
		#动态给type添加属性，分别保存首页商品的图片和文字信息
		type.image_banners = image_banners
		type.title_banners = title_banners
	#获取购物车中的商品数量
	user = request.user
	car_count = 0
	context = {'type':types,
				'goods_banners':banners,
				'promotion_banners':cuxiao,
				'cart_count':cart_count}
	temp = loader.get_template('index_static.html')
	index_static_html = temp.render(context)
	save_path = os.path.join(settings.BASE_DIR,'static/index.html')
	with open(r(save_path),'w') as f:
		f.write(index_static_html)
