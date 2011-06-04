from django.db import models

# Create your models here.

class Relay(models.Model):
    fingerprint = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    is_anonymous = models.BooleanField

class RelayDetails(models.Model):
    name = models.CharField(max_length=257) # TODO: figure out if this is a performance issue
    bandwidth = models.CharField(max_length=257)
    status = models.IntField
