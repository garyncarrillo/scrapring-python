# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class menu(models.Model):
	titulo = models.CharField(max_length=10)
	url = models.TextField()
	#time = models.DateTimeField()




class informacion(models.Model):
	titulo = models.CharField(max_length=20)
	img = models.TextField()



class Planes(models.Model):
	titulo =models.CharField(max_length=10)
	valor = models.TextField()
	informacion = models.TextField()
	url = models.TextField()

class Cabeceras(models.Model):
     cabecera = models.TextField()
     pie = models.TextField()

class mprincipal(models.Model):
	titulo = models.TextField()
	url = models.TextField()


