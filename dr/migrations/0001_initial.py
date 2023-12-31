# Generated by Django 4.2.7 on 2023-11-22 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HSE_id', models.IntegerField()),
                ('overall_progress_id', models.IntegerField()),
                ('report_no', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('todays_activity', models.TextField()),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_running', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dr.area')),
            ],
        ),
        migrations.CreateModel(
            name='VibrationalReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dr.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('is_approver', models.BooleanField(default=False)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dr.cluster')),
            ],
        ),
        migrations.CreateModel(
            name='OverallProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_update', models.TextField()),
                ('daily_report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dr.dailyreport')),
            ],
        ),
        migrations.CreateModel(
            name='Manhour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manpower', models.CharField(max_length=255)),
                ('manhours', models.IntegerField()),
                ('contractor', models.CharField(max_length=255)),
                ('total_LTI', models.IntegerField()),
                ('daily_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dr.dailyreport')),
            ],
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='prepared_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prepared_reports', to='dr.user'),
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='reviewed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_reports', to='dr.user'),
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='vibrational_reading',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dr.vibrationalreading'),
        ),
        migrations.AddField(
            model_name='area',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dr.cluster'),
        ),
    ]
