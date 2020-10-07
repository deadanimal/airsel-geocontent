# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Role(models.Model):
    ROLE_CHOICE = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('accountant', 'Accountant'),
        ('technician', 'Technician'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(default="staff", max_length=20, choices=ROLE_CHOICE, null=True, blank=True)
    # Access
    create_access = models.BooleanField(default=False)
    read_access = models.BooleanField(default=False)
    update_access = models.BooleanField(default=False)
    delete_access = models.BooleanField(default=False)
    def __str__(self):
        return '%s - %s' % (self.user.username, self.role)

@receiver(post_save, sender=User)
def create_or_update_role(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(user=instance)
    else:
        if not hasattr(instance, 'role'):
            Role.objects.create(user=instance)
    instance.role.save()

class Geotag(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('solved', 'Solved'),
    )
    TYPE_CHOICE = (
        ('point', 'Point'),
        ('linestring', 'Line'),
        ('polygon', 'Polygon'),
    )

    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    location = models.TextField(max_length=500, null=True, blank=True)
    file = models.FileField(max_length=100, null=True, blank=True)