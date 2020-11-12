# Generated by Django 2.2.16 on 2020-11-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201110_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='sex',
        ),
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown')], default='Male', max_length=6, verbose_name='Genero'),
        ),
    ]