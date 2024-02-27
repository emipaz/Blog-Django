from django.shortcuts import render
from django.http import Http404 

from .models import Post
# Create your views here.

def lista_post(request):
    posts = Post.publicados.all()
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

def detalle_post(request, id):
    post = get_object_or_404(Post, 
                             id = id,
                             estado = Post.Status.PUBLICADO)

    return render(request, 
                  template_name ="blog/post/detalle_post.html", 
                  context = {"post": post})
