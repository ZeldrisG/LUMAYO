# Generated by Django 3.1.7 on 2021-04-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issn', models.CharField(max_length=8)),
                ('titulo', models.CharField(max_length=110)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('fec_publicacion', models.DateField()),
                ('estado', models.CharField(choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')], default='Nuevo', max_length=50)),
                ('existencias', models.IntegerField()),
                ('idioma', models.CharField(choices=[('Español', 'Español'), ('Ingles', 'Ingles'), ('Ruso', 'Ruso'), ('Japones', 'Japones'), ('Coreano', 'Coreano')], default='Español', max_length=50)),
                ('num_pags', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('portada', models.ImageField(upload_to='libros/portadas')),
            ],
        ),
    ]
