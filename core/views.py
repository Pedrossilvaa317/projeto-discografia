from django.shortcuts import render,HttpResponse

def index (request):
    template_name = 'index.html'
    context = {'mensagem' : 'Bem-Vindo!!'}
    return render (request, template_name,context)