from django.shortcuts import render, redirect
from .models import Musicas,Albuns,Bandas
from .forms import MusicaForm, AlbumForm,BandaForm

def musica_list(request):
    musicas = Musicas.objects.all()
    template_name = 'musica_list.html'
    context = {
        'musicas' : musicas
    }
    return render (request, template_name,context)

def musica_new(request):
    if request.method == 'POST': 
        form = MusicaForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('musica:musica_list')
    else:
        template_name = 'musica_new.html'
        context = {
            'mensagem':'Cadastro de musicas',
            'form':MusicaForm()
        }
        return render(request, template_name, context)
    
def musica_edit(request,pk):
    musica = Musicas.objects.get(id = pk)
    if request.method == 'POST': 
        form = MusicaForm(request.POST,instance = musica) 
        if form.is_valid():
            form.save()
            return redirect('musica:musica_list')
    else:
        template_name = 'musica_edit.html'
        context = {
            'mensagem':'Alteração de musicas',
            'form':MusicaForm(instance = musica),
            'pk':pk
        }
        return render(request, template_name, context)
    
def musica_delete(request,pk):
    musica = Musicas.objects.get(id = pk)
    if request.method == 'POST':
        musica.delete()
        return redirect('musica:musica_list')
    template_name = 'musica_delete.html'
    context = {
        'musica': musica # Enviamos o álbum para o template
    }
    return render(request, template_name, context)

##################################################################################
#Álbum
def album_list (request):
    #1 Busca dos dados
    albuns = Albuns.objects.all()
    #2 Definição do Template
    template_name = 'album_list.html'
    #3 Criação do contexto
    context = {
        'albuns' : albuns
    }
    #4 Renderização da Resposta
    return render (request, template_name, context)

def album_new (request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('musica:album_list')
    else:
        form = AlbumForm()
    template_name = 'album_new.html'
    context = {
        'mensagem': 'Cadastro de Álbuns',
        'form': form
        }
    return render (request, template_name, context)

def album_edit (request, pk):
    album = Albuns.objects.get (id = pk)
    if request.method == 'POST':
        form = AlbumForm (request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect ('musica:album_list')
    else:
        form = AlbumForm(instance=album)
    template_name = 'album_edit.html'
    context = {
        'mensagem' : 'Edição de álbuns',
        'form' : form,
        'pk' : pk
    }
    return render (request, template_name,context)

def album_delete (request,pk):
    album = Albuns.objects.get (id = pk)
    if request.method == 'POST':
        album.delete()
        return redirect ('musica:album_list')

    template_name = 'album_delete.html'
    context = {
        'album': album 
    }
    return render(request, template_name, context)

###################################################################
#Banda

def banda_list (request):
    bandas = Bandas.objects.all()
    template_name = 'banda_list.html'
    context = {
        'bandas' : bandas
    }

    return render (request, template_name,context)
    
def banda_new (request):
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('musica:banda_list')
    else:
        form = BandaForm()
    template_name = 'banda_new.html'
    context = {
        'Mensagem' : 'Cadastro de bandas',
        'form' : form 
    }

    return render (request, template_name, context)

def banda_edit (request, pk):
    banda = Bandas.objects.get (id = pk)
    if request.method == 'POST':
        form = BandaForm (request.POST, instance=banda)
        if form.is_valid:
            form.save()
            return redirect ('musica:banda_list')
    else:
        form = BandaForm(instance=banda)
    template_name = 'banda_edit.html'
    context = {
        'mensagem' : 'Editar bandas',
        'pk' : pk,
        'form' : form
    }

    return render (request,template_name,context)

def banda_delete (request,pk):
    banda = Bandas.objects.get(id = pk)
    if request.method == 'POST':
        banda.delete()
        return redirect ('musica:banda_list')
    
    template_name = 'banda_delete.html'
    context = {
        'banda': banda 
    }
    return render(request, template_name, context)

################################################################
#banda detalhes

def banda_detail (request,pk):
    banda = Bandas.objects.get(id = pk)
    albuns = banda.albuns_set.all()
        
    template_name = 'banda_detail.html'
    context = {
        'mensagem' : 'Detalhes',
        'banda': banda,
        'albuns' : albuns
    }
    return render (request,template_name,context)

def album_detail(request,pk):
    album = Albuns.objects.get(id = pk)
    musicas = album.musicas_set.all()

    template_name = 'album_detail.html'
    context = {
        'mensagem' : 'Detalhes',
        'album': album,
        'musicas': musicas
    }

    return render (request,template_name,context)