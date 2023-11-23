# Generated by Django 4.2.7 on 2023-11-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0016_overallprogress_month_overallprogress_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyupdate',
            name='cumulative_equipment_visited',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyupdate',
            name='equipment_visited',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyupdate',
            name='percent_actual',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyupdate',
            name='percent_planning',
            field=models.FloatField(blank=True, null=True),
        ),
    ]