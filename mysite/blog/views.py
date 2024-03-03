from django.shortcuts import render
from django.http import Http404 
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .models import Post , Comentarios
from .forms import EmailPostForm , ComentariosForm , SearchForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector , SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
# Create your views here.

def lista_post(request, tag_slug=None):
    lista_de_posts = Post.publicados.all()
    # tags
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        lista_de_posts = lista_de_posts.filter(tags__in = [tag])
         
    
    # paginacion
    paginator     = Paginator(lista_de_posts, 3)
    pagina_numero = request.GET.get('page', 1)
    
    try:
        posts     = paginator.get_page(pagina_numero)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    
    
    return render (request, "blog/post/lista_post.html", 
                   {"posts": posts,
                    "tag"  : tag})


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
    
    comentarios = post.comentarios.filter(activo=True)
    formulario  = ComentariosForm()

    post_tags_ids  = post.tags.values_list('id', flat = True)
    post_similares = Post.publicados.filter(tags__in = post_tags_ids)\
                                    .exclude(id = post.id)
    post_similares = post_similares.annotate(tags_iguales = Count('tags'))\
                                   .order_by('-tags_iguales','-publicado')[:4] 
    
    return render(request, 
                  template_name ="blog/post/detalle_post.html", 
                  context = {"post": post,
                             "comentarios"    : comentarios,
                             "formulario"     : formulario,
                             "post_similares" : post_similares}
                  )
    
def compartir_post(request, post_id):
    
    post = get_object_or_404(Post, id = post_id,
                             estado = Post.Status.PUBLICADO)
    enviado = False
    
    if request.method == 'POST':
        
        formulario = EmailPostForm(request.POST)
        
        if formulario.is_valid():

            cd           = formulario.cleaned_data
            post_url     = request.build_absolute_uri(post.get_url_absoluta())
            asunto       = f"{cd['nombre']} recomienda que leas {post.titulo}"
            mensaje      = f"Lea este artículo {post_url}\n\n" \
                           f"{cd['nombre']} a comentado:\n\n\t {cd['comentario']}"
            send_mail(asunto,mensaje,"emipaz1975@gmail.com",[cd['para']], fail_silently=False)
            enviado = True             
    else:
        
        formulario = EmailPostForm()
    
    return render(request, 
                  template_name ="blog/post/compartir_post.html", 
                  context = {"post": post, 
                             "form": formulario,
                             "enviado": enviado}
                  )

@require_POST
def comentar_post(request, post_id):
    post         = get_object_or_404(Post, id = post_id, estado = Post.Status.PUBLICADO)
    comentario   = None
    formulario   = ComentariosForm(data = request.POST)
    
    if formulario.is_valid():
        comentario      = formulario.save(commit = False)
        comentario.post = post
        comentario.save()
    
    return render(request,
                  template_name ="blog/post/comentar.html",
                  context = {"post": post,
                             "comentario": comentario,
                             "formulario": formulario}
                  )
    
def buscar_post(request):
    
    formulario = SearchForm()
    consulta   = None
    resultados = []
    
    if 'consulta' in request.GET:
        formulario = SearchForm(request.GET)
        
        if formulario.is_valid():
            consulta = formulario.cleaned_data['consulta']
            #busca_vector   = SearchVector('titulo',weight='A' , config = 'spanish') + \
            #                 SearchVector("cuerpo",weight='B' , config = 'spanish')
            #busca_consulta = SearchQuery(consulta,              config = 'spanish') 
            
            resultados = Post.publicados.annotate(
                        similitud = TrigramSimilarity('titulo',consulta),
                    ).filter(similitud__gt = 0.1
                    ).order_by("-similitud")
            
    return render(request, 
                  template_name ="blog/post/buscar.html",
                  context = { 'form': formulario,
                              'query': consulta,
                              'results': resultados}) 