# Generated by Django 4.2.6 on 2023-12-08 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('emp_no', models.IntegerField(blank=True, primary_key=True, serialize=False, unique=2)),
                ('e_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.IntegerField(blank=True)),
                ('hire_date', models.DateField()),
                ('sal', models.IntegerField(blank=True)),
                ('comm', models.IntegerField(blank=True)),
                ('dept_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]