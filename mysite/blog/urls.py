from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.lista_post, 
         name='lista_post'),
    path('<int:año>/<int:mes>/<int:dia>/<slug:post>', 
            views.detalle_post, 
            name='detalle_post'),
    path("<int:post_id>/compartir/", 
            views.compartir_post, 
            name="compartir_post"),
    path("<int:post_id>/comentar/", 
            views.comentar_post, 
            name="comentar_post"),
]