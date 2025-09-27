from django.db import models

class Bandas(models.Model):
    nome = models.CharField('Nome',max_length = 200)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Banda'
        verbose_name_plural = 'Bandas'
        ordering = ['nome']

class Albuns (models.Model):
    titulo = models.CharField('Titulo',max_length = 200)
    banda = models.ForeignKey(Bandas, on_delete=models.PROTECT)
    data = models.DateField('Data',null=False)

    def __str__ (self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'
        ordering = ['titulo']

class Musicas(models.Model):
    titulo = models.CharField('Titulo',max_length=200)
    segundos = models.IntegerField('Segundos',default=0)
    album = models.ForeignKey(Albuns,on_delete=models.PROTECT)
    

