#重写图片类的保存方法
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
import sys
sys.path.append("/root/virtualenvs/QHTZ/index/")
from index.models import *
class ImageStorage(FileSystemStorage):
	from django.conf import settings
	def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
		# 初始化
		super(ImageStorage, self).__init__(location, base_url)

	# 重写 _save方法        
	def _save(self, name, content):
		import os, time, random
		# 文件扩展名
		ext = os.path.splitext(name)[1]
		# 文件目录
		d = os.path.dirname(name)
		# 定义文件名，年月日时分秒随机数
		fn = time.strftime('%Y%m%d%H%M%S')
		fn = fn + '_%d' % random.randint(0,100)
		# 重写合成文件名
		name = os.path.join(d, fn + ext)
		# 调用父类方法
		return super(ImageStorage, self)._save(name, content)

#markdown显示的帮助信息
class HelpInfo():
	def info(self):
		with open(r'/root/virtualenvs/QHTZ/imagestorage/helpinfo.txt','r+') as f:
			helpinfo = f.read()
			self.helpinfo = helpinfo
			f.close()
		return self.helpinfo

#首页个人介绍
class Self_int():
	def info(self):
		with open(r'/root/virtualenvs/QHTZ/imagestorage/self_introduction.txt','r+') as f:
			helpinfo = f.read()
			self.helpinfo = helpinfo
			f.close()
		return self.helpinfo
