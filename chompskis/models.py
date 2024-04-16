from django.db import models

# Create your models here.
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
    def __str__(self):
        return (f"{self.name}")


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
    def __str__(self): 
        return (f"{self.swarm_id}")

