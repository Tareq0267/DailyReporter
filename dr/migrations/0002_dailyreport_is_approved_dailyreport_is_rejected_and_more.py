# Generated by Django 4.2.7 on 2023-11-22 06:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreport',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vibrationalreading',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vibrationalreading',
            name='reading',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]