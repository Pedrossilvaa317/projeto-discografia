

from django import forms
from django.forms import ModelForm
from .models import Musicas, Albuns, Bandas

class MusicaForm(ModelForm):
    class Meta:
        model = Musicas
        fields = ['titulo', 'segundos', 'album']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'segundos': forms.NumberInput(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-select'}),
        }

class AlbumForm(ModelForm):
    class Meta:
        model = Albuns
        fields = ['titulo', 'banda', 'data','capa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'banda': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'capa': forms.FileInput(attrs={'class': 'form-control'}),
        }

class BandaForm(ModelForm):
    class Meta:
        model = Bandas
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }