# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-30 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0008_auto_20190330_2228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exposition',
            options={'verbose_name': 'Экспозиция', 'verbose_name_plural': 'Экспозиции'},
        ),
        migrations.AlterModelOptions(
            name='exposition_img',
            options={'verbose_name': 'Фото экспозиции'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='post_img',
            options={'verbose_name': 'Фото новости'},
        ),
    ]
