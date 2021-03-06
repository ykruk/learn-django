# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-31 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0009_auto_20190330_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exposition_img',
            options={'verbose_name': 'Фото экспозиции', 'verbose_name_plural': 'Фото экспозиции'},
        ),
        migrations.AlterModelOptions(
            name='post_img',
            options={'verbose_name': 'Фото новости', 'verbose_name_plural': 'Фото новости'},
        ),
        migrations.RemoveField(
            model_name='message',
            name='copy',
        ),
        migrations.AddField(
            model_name='message',
            name='reply',
            field=models.NullBooleanField(verbose_name='Рассмотрено'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_name',
            field=models.CharField(max_length=100, verbose_name='Имя отправителя'),
        ),
    ]
