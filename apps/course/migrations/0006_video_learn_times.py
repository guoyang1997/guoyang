# Generated by Django 2.2.16 on 2020-11-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='学习时长(分钟数)'),
        ),
    ]
