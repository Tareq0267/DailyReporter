# Generated by Django 4.2.7 on 2023-11-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0003_alter_user_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='overall_progress_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dr.overallprogress'),
        ),
    ]