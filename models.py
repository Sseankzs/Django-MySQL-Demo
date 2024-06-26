# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    authorization = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class GnomeChompskiEmployee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    authorization = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gnome_chompski_employee'


class GnomeChompskiGnomeChompskis(models.Model):
    chompskis_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.SmallIntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    no_teeth = models.PositiveIntegerField()
    swarm = models.ForeignKey('GnomeChompskiSwarm', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gnome_chompski_gnome_chompskis'


class GnomeChompskiOversees(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(GnomeChompskiEmployee, models.DO_NOTHING)
    swarm = models.ForeignKey('GnomeChompskiSwarm', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gnome_chompski_oversees'


class GnomeChompskiSwarm(models.Model):
    swarm_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    quantity = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)

    class Meta:
        managed = False
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
        managed = False
        db_table = 'gnome_chompskis'


class Oversees(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    swarm = models.ForeignKey('Swarm', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oversees'


class Swarm(models.Model):
    swarm_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swarm'
