#创建自定义过滤器
from django.template import Library
from index.models import PythonProduct
from django.utils.safestring import mark_safe
register = Library()

@register.simple_tag()
def title_deal(id):
	deal_id = PythonProduct.objects.get(id=int(id))
	title = deal_id.title
	return title

@register.simple_tag()
def body_deal(id):
	deal_id = PythonProduct.objects.get(id=int(id))
	body = deal_id.content
	return body
