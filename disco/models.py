from django.db import models
from PIL import Image

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
    capa = models.ImageField('Capa', upload_to='capas/',blank=True,null=True)

    def __str__ (self):
        return self.titulo
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.capa and hasattr(self.capa, 'path'):
            try:
                img = Image.open(self.capa.path)
                if img.height >= 300 or img.width >= 300:
                    output_size = (200, 200)
                    img.thumbnail(output_size)
                    img.save(self.capa.path)
            except (IOError, FileNotFoundError):
                pass
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'
        ordering = ['titulo']

class Musicas(models.Model):
    titulo = models.CharField('Titulo',max_length=200)
    segundos = models.IntegerField('Segundos',default=0)
    album = models.ForeignKey(Albuns,on_delete=models.PROTECT)
    

