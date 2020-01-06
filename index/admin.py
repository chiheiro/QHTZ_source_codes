'''后台中注册模型类,其中的删除操作只能删除数据库记录，无法真正删除图片'''
from django.contrib import admin
from django.utils.safestring import mark_safe #将字符串标记为安全进行输出
from .models import *
import sys
sys.path.append("../")
from imagestorage.storage import ImageStorage

#自定义后台只读类
class ReadOnlyModelAdmin(admin.ModelAdmin):
    actions = None
    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]
    def has_add_permission(self, request):
        return False
    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)
    def has_delete_permission(self, request, obj=None):
        return False

#自定义登陆后台时的页面显示
admin.site.site_header = "清花天藏后台管理系统"
admin.site.site_title = "清花天藏"

#用户信息记录(暂未启用)
class UserList(admin.ModelAdmin):
	list_per_page = 10
	list_display = ["name",'phonenumber','time']
	#将操作栏放在列表下方
	actions_on_bottom = True
	actions_on_top = False
	#以时间过滤
	list_filter = ["time"]
	search_fields = ["name"]

#首页图片轮播图
class IndexImageList(admin.ModelAdmin):
	def showimage(self,IndexImages):
		image = mark_safe('<img src="http://www.lixuejie.cn/static/{}" height="50px";length="50px">'.format(IndexImages.image))
		return image
	list_per_page = 10
	list_display = ["imagename",'upldtime','chatime','showimage','show']
	actions_on_bottom = True
	actions_on_top = False
	list_filter = ["chatime"]
	search_fields = ["imagename"]
	showimage.allow_tags = True
	showimage.short_description = "图片"

#UI设计的图片
class ProductImageList(admin.ModelAdmin):
	def showimage(self,ProductImages):
		#后台显示上传图片的略缩图
		try:
			image = mark_safe('<img src="http://www.lixuejie.cn/static/{}" height="50px";length="50px">'.format(ProductImages.image))
		except EXCEPTION as f:
			image = ""
		return image
	showimage.allow_tags = True
	showimage.short_description = "图片"
	list_per_page = 10
	list_display = ["imagename",'upldtime','chatime','showimage']
	actions_on_bottom = True
	actions_on_top = False
	list_filter = ["chatime"]
	search_fields = ["imagename"]

#Python文章的信息
class PythonEditor(admin.ModelAdmin):
	list_per_page = 20
	list_display = ['title','id','mktime','edittime']
	actions_on_bottom = True
	actions_on_top = False
	list_filter = ["edittime"]
	search_fields = ['title']

#查看简历者的信息
class CheckJianliDetail(ReadOnlyModelAdmin):
	list_per_page = 20
	list_display = ['usertype','ex_time','ipaddr','area']
	actions_on_bottom = True
	actions_on_top = False
	list_filter = ["ex_time"]
	search_fields = ['area']
	
class TrafficAdmin(ReadOnlyModelAdmin):
	list_per_page = 20
	list_display = ['traffic_ip','view_time','view_times']
	actions_on_bottom = True
	actions_on_top = False
	list_filter = ["view_time"]

admin.site.register(UserMessages,UserList)
admin.site.register(IndexImages,IndexImageList)
admin.site.register(IndexAboutMe)
admin.site.register(ProductImages,ProductImageList)
admin.site.register(PythonProduct,PythonEditor)
admin.site.register(Traffic,TrafficAdmin)
admin.site.register(CheckJianli,CheckJianliDetail)
