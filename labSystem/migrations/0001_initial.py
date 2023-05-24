# Generated by Django 4.2.1 on 2023-05-23 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('number_of_pcs', models.IntegerField()),
                ('building_number', models.IntegerField()),
                ('floor_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('number_of_chairs', models.IntegerField()),
                ('status', models.CharField(choices=[('AC', 'Active'), ('um', 'under maintenance')], default='AC', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='LabReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number_of_pcs', models.IntegerField()),
                ('report_status', models.CharField(choices=[('SW', 'Software'), ('HW', 'Hardware')], default='SW', max_length=2)),
                ('report_description', models.CharField(max_length=2000)),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('is_repaired', models.BooleanField(default=False)),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labSystem.lab')),
            ],
        ),
    ]
