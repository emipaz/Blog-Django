from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class PublicadoManager(models.Manager):
    
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter( estado = Post.Status.PUBLICADO )


class Post(models.Model):
    
    class Meta:
        ordering = ('-publicado',)
        indexes = [
            models.Index(fields=['-publicado']),
        ]
    class Status(models.TextChoices):
        BORRADOR  = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'
    
    titulo      = models.CharField(max_length = 250)
    slug        = models.SlugField(max_length = 250, unique_for_date = 'publicado')
    cuerpo      = models.TextField()
    publicado   = models.DateTimeField(default = timezone.now )
    creado      = models.DateTimeField(auto_now_add = True)
    actualizado = models.DateTimeField(auto_now = True)
    estado      = models.CharField(max_length = 1, 
                                   choices = Status.choices, 
                                   default = Status.BORRADOR)
    autor       = models.ForeignKey(User, 
                                    on_delete = models.CASCADE,
                                    related_name = 'blog_posts')

    # Managers
    objects    = models.Manager()   # The default manager.
    publicados = PublicadoManager() # Manager por Publicados
    
    def __str__(self):
        return self.titulo
    
    def get_url_absoluta(self):
        return reverse("blog:detalle_post", 
                       args=[self.publicado.year, 
                             self.publicado.month, 
                             self.publicado.day, 
                             self.slug])
    
    