# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-20 00:49


import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0077_auto_20160819_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
