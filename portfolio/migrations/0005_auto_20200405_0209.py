# Generated by Django 2.0 on 2020-04-05 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200405_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
    ]
