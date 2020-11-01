from django.db import models


# Create your models here.


class Fruit(models.Model):
    TYPE = (
        (1, 'Normal'),
        (2, 'Rara')
    )
    fruit_name = models.CharField(verbose_name='Nombre de fruta', max_length=50)
    fruit_type = models.CharField(max_length=1, choices=TYPE, default = 1, verbose_name='Tipo de fruta')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)


class Character(models.Model):
    SEX = (
        (1, 'Mujer'),
        (2, 'Hombre')
    )
    RAZA = (
        (1, 'Humano'),
        (2, 'Elfo')
        )
    EDAD = list()
    for e in range(1, 50):
        EDAD.append((e,e))
    RANGO = (
        (1, 'Soldado'),
        (2, 'Mayor')
    )
    ESTADO = (
        (1, 'Vivo'),
        (2, 'Muerto')
    )
    OCU = (
        (1, 'Programador'),
        (2, 'Test')
    )
    ATK = (
        (1, 'Golpe Relampago'),
        (2, 'Chancletazo')
    )

    name = models.CharField(verbose_name='Nombre', max_length=50)
    image = models.ImageField(upload_to='Personaje', verbose_name='Imagen')
    date_old = models.DateTimeField(verbose_name='Fecha de nacimiento')
    ega = models.CharField(max_length=1, choices=EDAD, default = 1, verbose_name='Edad')
    sex = models.CharField(max_length=1, choices=SEX, default = 1, verbose_name='Sexo')
    value = models.IntegerField(verbose_name='Recompensa')

    # Descripción
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    race = models.CharField(max_length=1, choices=RAZA, default = 1, verbose_name='Raza')
    rank = models.CharField(max_length=1, choices=RANGO, default = 1, verbose_name='Rango')
    state = models.CharField(max_length=1, choices=ESTADO, default = 1, verbose_name='Estado')
    origin = models.CharField(max_length = 12, verbose_name='Origen')
    attack = models.CharField(max_length=1, choices=ATK, default = 1, verbose_name='Ataques')
    occupation = models.CharField(max_length=1, choices=OCU, default = 1, verbose_name='Ocupasion')
    description = models.TextField(verbose_name='Descriccion')

