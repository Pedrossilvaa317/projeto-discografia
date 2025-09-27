from django.forms import ModelForm
from .models import Musicas, Albuns, Bandas

class MusicaForm(ModelForm): 
    class Meta:
        model = Musicas
        fields = '__all__'

class AlbumForm(ModelForm):
    class Meta:
        model = Albuns
        fields = '__all__'

class BandaForm(ModelForm):
    class Meta:
        model = Bandas
        fields = '__all__'