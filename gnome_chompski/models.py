# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table     
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    authorization = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'employee'
        
    def __str__(self):
        return self.fname + " " + self.lname



class GnomeChompskiEmployee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    authorization = models.CharField(max_length=50)

    class Meta:
        db_table = 'gnome_chompski_employee'
        
    def __str__(self):
        return self.fname + " " + self.lname


class GnomeChompskiGnomeChompskis(models.Model):
    chompskis_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.SmallIntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    no_teeth = models.PositiveIntegerField()
    swarm = models.ForeignKey('GnomeChompskiSwarm', models.DO_NOTHING)

    class Meta:
        db_table = 'gnome_chompski_gnome_chompskis'
        
    def __str__(self):
        return self.name


class GnomeChompskiOversees(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(GnomeChompskiEmployee, models.DO_NOTHING)
    swarm = models.ForeignKey('GnomeChompskiSwarm', models.DO_NOTHING)

    class Meta:
        db_table = 'gnome_chompski_oversees'

    def __str__(self):
        return self.employee.fname + " " + self.employee.lname + " oversees " + self.swarm.name

class GnomeChompskiSwarm(models.Model):
    swarm_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    quantity = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)

    class Meta:
        db_table = 'gnome_chompski_swarm'


class GnomeChompskis(models.Model):
    chompskis_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.SmallIntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    no_teeth = models.PositiveIntegerField(blank=True, null=True)
    swarm = models.ForeignKey('Swarm', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'gnome_chompskis'


class Oversees(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    swarm = models.ForeignKey('Swarm', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'oversees'


class Swarm(models.Model):
    swarm_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'swarm'

