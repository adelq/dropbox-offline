from django.db import models

class User(models.Model):
    dropbox_email = models.CharField(max_length=100)
    dropbox_password = models.CharField(max_length=100)