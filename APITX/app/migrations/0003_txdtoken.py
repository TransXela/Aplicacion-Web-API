# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160928_1313'),
    ]

    operations = [
        
        migrations.AddField("TxdDenuncia", "latitud", models.FloatField(blank=True, null=True)),
        migrations.AddField("TxdDenuncia", "longitud", models.FloatField(blank=True, null=True)),
        migrations.AddField("TxdHorariodetalle", "estado", models.FloatField(blank=True, null=True)),
        migrations.RemoveField(
            model_name='txdchofer',
            name='nolicencia',
        ),
    ]
