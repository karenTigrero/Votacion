# Generated by Django 2.0.12 on 2020-03-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=220)),
                ('direccion', models.TextField()),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
                'ordering': ['apellidos'],
            },
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Lista')),
                ('propuesta', models.TextField(verbose_name='Propuesta')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('candidato_id', models.ManyToManyField(to='lista.Candidato')),
            ],
            options={
                'verbose_name': 'Lista',
                'verbose_name_plural': 'Listas',
                'ordering': ['nombre'],
            },
        ),
    ]