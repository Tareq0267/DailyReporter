# Generated by Django 4.2.7 on 2023-11-22 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0007_remove_dailyreport_vibrational_reading_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='HSE_id',
        ),
        migrations.CreateModel(
            name='HSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HSE_id', models.IntegerField()),
                ('LTI', models.IntegerField()),
                ('RWC', models.IntegerField()),
                ('MTC', models.IntegerField()),
                ('TRC', models.IntegerField()),
                ('FAC', models.IntegerField()),
                ('Highlights', models.TextField()),
                ('DailyReport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dr.dailyreport')),
            ],
        ),
    ]