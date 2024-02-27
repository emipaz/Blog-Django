from django.shortcuts import render
from django.http import Http404 
from django.core.paginator import Paginator
from .models import Post
# Create your views here.

def lista_post(request):
    lista_de_posts = Post.publicados.all()
    # paginacion
    paginator     = Paginator(lista_de_posts, 3)
    pagina_numero = request.GET.get('page', 1)
    posts         = paginator.get_page(pagina_numero)
    
    return render (request, "blog/post/lista_post.html", {"posts": posts})


# def detalle_post(request, id):
    
#     try:
#         post = Post.objects.get(id = id)
#     except Exception as e:
#         print(e)
#         raise Http404 (f"No Existe el post con id:{id}")
    
#     return render(request, 
#                   template_name ="blog/post/detalle_post.html", 
#                   context = {"post": post})

### ALternativa al Try Except 
from django.shortcuts import render, get_object_or_404

def detalle_post(request, año, mes, dia, post):
    post = get_object_or_404(Post, 
                             estado = Post.Status.PUBLICADO,
                             slug=post,
                             publicado__year  = año,
                             publicado__month = mes,
                             publicado__day   = dia)

    return render(request, 
                  template_name ="blog/post/detalle_post.html", 
                  context = {"post": post})
