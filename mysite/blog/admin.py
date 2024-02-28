from django.contrib import admin

# Register your models here.
from .models import Post , Comentarios


# agregar el modelo Post a admin de manera automatica
# admin.site.register(Post)

# manera personalizada

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'slug', 'autor', 'publicado')
    list_filter         = ("estado","creado",'publicado', 'autor')
    search_fields       = ('titulo', 'cuerpo')
    prepopulated_fields = {'slug':('titulo',)}
    raw_id_fields       = ('autor',)
    date_hierarchy      = 'publicado'
    ordering            = ('publicado',"estado")
    
@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display        = ('nombre', 'email', "post", "creado", "activo")
    list_filter         = ("creado","activo","actualizado")
    search_fields       = ('nombre', 'email', "cuerpo")
