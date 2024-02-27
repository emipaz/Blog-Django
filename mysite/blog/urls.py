from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.lista_post, name='lista_post'),
    path('<int:id>/', views.detalle_post, name='detalle_post'),
]