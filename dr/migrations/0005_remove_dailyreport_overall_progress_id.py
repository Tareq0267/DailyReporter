# Generated by Django 4.2.7 on 2023-11-22 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0004_alter_dailyreport_overall_progress_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='overall_progress_id',
        ),
    ]
