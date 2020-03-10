# Generated by Django 2.0.12 on 2020-03-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Votante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=220)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.TextField(max_length=220)),
                ('correo', models.CharField(max_length=220)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('sexo_id', models.ManyToManyField(to='votante.Sexo')),
            ],
            options={
                'verbose_name': 'Votante',
                'verbose_name_plural': 'Votantes',
                'ordering': ['apellido'],
            },
        ),
    ]