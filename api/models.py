from django.db import models

#Create your models here.

class Character(models.Model):
  TYPE = [
    ('Paramecia', 'Paramecia'),
    ('Zoan', 'Zoan'),
    ('Logia', 'Logia'),
    ('None','None'),
    ('Unknown','Unknown'),
  ]
  GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unknown','Unknown'),
  ]
  RAZA = [
    ('Human', 'Human'),
    ('Kuja','Kuja'),
    ('Ancestral giant','Ancestral giant'),
    ('Shandian','Shandian'),
    ('Clone','Clone'),
    ('Nobles','Nobles'),
    ('Reindeer', 'Reindeer'),
    ('Animal','Animal'),
    ('Gyoji', 'Gyoji'),
    ('Giant', 'Giant'),
    ('Triton', 'Triton'),
    ('Mink', 'Mink'),
    ('Long arms', 'Long arms'),
    ('Long legs', 'Long legs'),
    ('Three eyes', 'Three eyes'),
    ('Dwarf', 'Dwarf'),
    ('King', 'King'),
    ('Hybrid', 'Hybrid'),
    ('Cyborg', 'Cyborg'),
    ('Newkama', 'Newkama'),
    ('Zombie', 'Zombie'),
    ('Unknown','Unknown'),
  ]
  EDAD = [(e, e) for e in range(1, 151)]
  RANGO = [
    ('Supernova', 'Supernova'),
    ('Shichibukai', 'Shichibukai'),
    ('Yonkou', 'Yonkou'),
    ('Pirata King', 'Pirata King'),
    ('Captain', 'Captain'),
    ('First official','First official'),
    ('Official', 'Official'),
    ('Liuetenant', 'Liuetenant'),
    ('Admiral', 'Admiral'),
    ('Vice admiral', 'Vice admiral'),
    ('Commodore', 'Commodore'),
    ('Legend', 'Legend'),
    ('None','None'),
    ('Unknown', 'Unknown'),
  ]
  ESTADO = [
    ('Alive', 'Alive'),
    ('Dead', 'Dead'),
    ('Unknown', 'Unknown'),
  ]
  OCU = [
    ('Captain', 'Captain'),
    ('Doctor', 'Doctor'),
    ('Swordsman', 'Swordsman'),
    ('Navigator', 'Navigator'),
    ('Sniper', 'Sniper'),
    ('Chef', 'Chef'),
    ('Tenryuubito','Tenryuubito'),
    ('archaeologist', 'archaeologist'),
    ('Carpenter', 'Carpenter'),
    ('Musician', 'Musician'),
    ('Explorer','Explorer'),
    ('Helmsman', 'Helmsman'),
    ('Servant', 'Servant'),
    ('Scientific', 'Scientific'),
    ('Pirate', 'Pirate'),
    ('Governing', 'Governing'),
    ('Samurai', 'Samurai'),
    ('Alcade', 'Alcade'),
    ('Assassin', 'Assassin'),
    ('Famous', 'Famous'),
    ('Minister', 'Minister'),
    ('Bounty hunter', 'Bounty hunter'),
    ('Revolutionary', 'Revolutionary'),
    ('King', 'King'),
    ('None','None'),
    ('Unknown', 'Unknown'),
  ]

  name = models.CharField(verbose_name='Nombre', max_length=50)
  image = models.ImageField(upload_to='Personaje', verbose_name='Imagen', null=True, blank=True)
  age = models.IntegerField(
    choices=EDAD,
    default=EDAD[0][1],
    verbose_name='Edad',
  )
  gender = models.CharField(
    max_length=6,
    choices=GENDER,
    default=GENDER[0][1],
    verbose_name='Genero',
  )
  # Descripción
  reward = models.DecimalField(verbose_name='Recompensa',max_digits=10, decimal_places=3,blank=True,null=True)
  fruit_name = models.CharField(
    verbose_name='Nombre de fruta',
    max_length=30,
    blank=True
  )
  fruit_type = models.CharField(
    max_length=20,
    choices=TYPE,
    default=TYPE[0][1],
    verbose_name='Tipo de fruta',
    blank=True
  )

  race = models.CharField(
    max_length=20,
    choices=RAZA,
    default=RAZA[0][1],
    verbose_name='Raza'
  )
  rank = models.CharField(
    max_length=30,
    choices=RANGO,
    default=RANGO[0][1],
    verbose_name='Rango'
  )
  status = models.CharField(
    max_length=6,
    choices=ESTADO,
    default=ESTADO[0][1],
    verbose_name='Estado'
  )
  origin = models.CharField(max_length=50, verbose_name='Origen',blank=True)
  occupation = models.CharField(
    max_length=20,
    choices=OCU,
    default=OCU[0][1],
    verbose_name='Ocupasion'
  )
  description = models.TextField(verbose_name='Descriccion',blank=True,null=True)
  created_on = models.DateTimeField(auto_now_add=True,verbose_name='Date published')
  update_on = models.DateTimeField(auto_now=True,verbose_name='Date updated')

  def __str__(self):
    return self.name
