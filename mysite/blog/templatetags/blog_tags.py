from django import template
from ..models import Post
from  datetime import datetime
from django.db.models import Count

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

@register.simple_tag()
def mas_comentados(count=5):
    return Post.publicados.annotate(
        total_comentarios = Count('comentarios')
    ).order_by('-total_comentarios')[:count]