# Generated by Django 4.2.7 on 2023-11-22 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0005_remove_dailyreport_overall_progress_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='vibrational_reading',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dr.vibrationalreading'),
        ),
    ]
