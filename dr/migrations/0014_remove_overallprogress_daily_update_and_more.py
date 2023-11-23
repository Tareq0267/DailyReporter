# Generated by Django 4.2.7 on 2023-11-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0013_dailyupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overallprogress',
            name='daily_update',
        ),
        migrations.AddField(
            model_name='overallprogress',
            name='daily_update',
            field=models.ManyToManyField(to='dr.dailyupdate', verbose_name='daily_update'),
        ),
    ]
