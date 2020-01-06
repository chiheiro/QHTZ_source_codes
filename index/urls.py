from django.urls import path,re_path,include
from .views import *
from django.conf.urls.static import static
import sys
sys.path.append("../")
import mdeditor
from QHTZ import settings

urlpatterns = [ 
	re_path(r"^static/+",StaticView.as_view(),name="图片略缩图"),
	re_path(r"^index/+$",IndexView.as_view(),name="主页"),
	re_path(r"^UIproduct/+",UIProductImagesView.as_view(),name="UI作品"),
	re_path(r"^Pythonproduct/+$",PythonProductView.as_view(),name="作品"),
	re_path(r"^Pythonproduct/[0-9]+/+",PythonDetail.as_view(),name="作品"),
	re_path(r"^choose_product/+",ChooseProductView.as_view(),name="作品选择"),
	re_path(r"^check_jianli/+",CheckJianliView.as_view(),name="简历检查"),
	re_path(r"^connect/+",ConnectView.as_view(),name="联系我们"),
	re_path(r"check_cooperation/+",CheckCooperationView.as_view(),name="合作"),
	re_path(r'^mdeditor/+',include('mdeditor.urls')),
	re_path(r"^$",IndexView.as_view(),name="主页"),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL)
