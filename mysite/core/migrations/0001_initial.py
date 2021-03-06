# Generated by Django 2.2.4 on 2019-11-13 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RideDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('driver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Driver')),
                ('passenger_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Passenger')),
            ],
        ),
    ]
