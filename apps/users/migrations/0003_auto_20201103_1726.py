# Generated by Django 2.2.16 on 2020-11-03 17:26

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='adress',
            field=DjangoUeditor.models.UEditorField(default='', max_length=100, verbose_name='地址'),
        ),
    ]
