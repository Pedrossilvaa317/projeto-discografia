from django.urls import path
from .views import musica_list,musica_new,musica_edit,musica_delete,album_list,album_new,album_edit,album_delete,banda_list,banda_new,banda_edit,banda_delete,banda_detail,album_detail


app_name = 'musica'

urlpatterns = [
    #musicas
    path('musica_list/',musica_list, name='musica_list'),
    path('musica_new/', musica_new, name='musica_new'),
    path('musica_edit/<int:pk>/',musica_edit, name='musica_edit'),
    path('musica_delete/<int:pk>/',musica_delete, name='musica_delete' ),
    
    #albuns
    path('album_list/',album_list, name='album_list'),
    path('album_new/',album_new, name='album_new'),
    path('album_edit/<int:pk>/', album_edit, name='album_edit'),
    path('album_delete/<int:pk>/', album_delete, name='album_delete'),

    #Banda
    path('banda_list/', banda_list, name = 'banda_list'),
    path('banda_new/', banda_new, name='banda_new'),
    path('banda_edit/<int:pk>/',banda_edit, name= 'banda_edit'),
    path('banda_delete<int:pk>/', banda_delete, name='banda_delete'),

    #Detalhes
    path('banda_detail/<int:pk>/',banda_detail,name='banda_detail'),
    path('album_detail/<int:pk>/', album_detail, name='album_detail')
]