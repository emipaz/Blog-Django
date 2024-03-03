from django import forms
from .models import Comentarios

class EmailPostForm(forms.Form):
    nombre     = forms.CharField(max_length=25)
    # email      = forms.EmailField()
    para       = forms.EmailField()
    comentario = forms.CharField(required=False,widget=forms.Textarea)
    
class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('nombre','email','cuerpo')
        
class SearchForm(forms.Form):
    consulta = forms.CharField()
    
    