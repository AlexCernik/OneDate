from django.db import models

# Create your models here.

class Fruit(models.Model):
	fruit_name = models.CharField(verbose_name='Nombre de fruta',max_length=50)
	fruit_type = models.CharField(verbose_name='Tipo de fruta',max_length=50)
  created_on = models.DateTimeField(auto_now_add=True)
  update_on = models.DateTimeField(auto_now=True)

class Description(models.Model):
  fruit = models.ManyToManyField(Fruit)
	race = models.CharField(verbose_name='Raza')
	rank = models.CharField(verbose_name='Rango')
	state = models.CharField(verbose_name='Estado')
	origin = models.CharField(verbose_name='Origen')
	attack = models.TextField(verbose_name='Ataques')
	occupation = models.CharField(verbose_name='Ocupasion')
	description = models.TextField(verbose_name='Descriccion')

class Character(models.Model):
	name = models.CharField(verbose_name='Nombre', max_length=50)
	image = models.ImageField(verbose_name='Imagen')
	date_old = models.DateTimeField(verbose_name='Fecha de nacimiento')
	ega = models.DateTimeField(verbose_name='Edad')
	sex = models.CharField(verbose_name='Sexo', max_length=1)
	value = models.IntegerField(verbose_name='Recompensa')