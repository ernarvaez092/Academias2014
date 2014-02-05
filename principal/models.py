#encoding:utf-8
from django.db import models

# Create your models here.

class Monumento(models.Model):
    nombre = models.CharField(max_length = 60)
    callePrincipal = models.CharField(max_length = 50)
    calleSecundaria = models.CharField(max_length = 50)
    referencia = models.TextField()
    fecha_nacimiento = models.DateField()
    fecha_muerte = models.DateField()
    reconocimientos = models.TextField()
    escuela = models.CharField(max_length = 50)
    colegio = models.CharField(max_length = 50)
    universidad = models.CharField(max_length = 50)
    titulo = models.CharField(max_length = 50)
    foto = models.ImageField(upload_to='academias/site_media/img/photos', verbose_name='Image')
    historia = models.TextField()
    lat = models.CharField(max_length=12)
    long = models.CharField(max_length=12)
        
    def __unicode__(self):
        return self.nombre
