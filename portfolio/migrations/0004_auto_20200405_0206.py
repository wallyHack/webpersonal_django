# Generated by Django 2.0 on 2020-04-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200404_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición'),
        ),
    ]
