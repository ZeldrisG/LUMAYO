# Generated by Django 3.1.7 on 2021-07-16 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='ciencia_ficcion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genero',
            name='drama',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genero',
            name='fantasia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genero',
            name='mitología',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genero',
            name='policial',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genero',
            name='romance',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genero',
            name='terror',
            field=models.BooleanField(default=False),
        ),
    ]
