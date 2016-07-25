from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

# fields = ('name', 'sensor',  'body', 'created_at', 'status', 'author')
class Entry(models.Model):
    STATUS_ON = "on"
    STATUS_OFF = "off"
    STATUS_SET = (
            (STATUS_ON, "ON"),
            (STATUS_OFF, "OFF"),
    )
    name = models.CharField(max_length=128)
    sensor = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_OFF, max_length=8)
    author = models.ForeignKey(User, related_name='entries')
