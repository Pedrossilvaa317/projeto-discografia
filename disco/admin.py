from django.contrib import admin
from .models import Bandas
from .models import Musicas
from .models import Albuns

class BandaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    ordering = ['-nome']
    search_fields = ['nome']
    list_filter = ['nome']
    

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo','banda','data']
    ordering = ['-titulo']
    search_fields = ['Albuns']
    list_filter = ['titulo']
    


admin.site.register(Bandas, BandaAdmin)
admin.site.register(Albuns,AlbumAdmin)
