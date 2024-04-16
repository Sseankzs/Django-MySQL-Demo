# Generated by Django 5.0.2 on 2024-04-12 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('authorization', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Swarm',
            fields=[
                ('swarm_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('quantity', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Oversees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gnome_chompski.employee')),
                ('swarm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gnome_chompski.swarm')),
            ],
        ),
        migrations.CreateModel(
            name='Gnome_Chompskis',
            fields=[
                ('chompskis_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('age', models.SmallIntegerField(blank=True, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('no_teeth', models.PositiveIntegerField()),
                ('swarm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gnome_chompski.swarm')),
            ],
        ),
    ]
