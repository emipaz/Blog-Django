from django import template
from ..models import Post
from  datetime import datetime

register = template.Library()

@register.simple_tag()
def total_de_posts():
    return Post.objects.count()

@register.simple_tag()
def hora():
    return datetime.now().strftime("%d/%m/%Y")
