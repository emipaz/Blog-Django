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


@register.inclusion_tag('blog/post/ultimos_post.html')
def mostrar_ultimos_posts(count=5):
    ultimos_post = Post.publicados.order_by('-publicado')[:count]
    return {"ultimos_post": ultimos_post}
