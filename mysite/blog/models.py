from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

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
    slug        = models.SlugField(max_length = 250)
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

    
    def __str__(self):
        return self.titulo
    
    