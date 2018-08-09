from django.db import models
from django.contrib.auth.models import User

# models

class Media(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return 

class UserProfile(models.Model):
    bio = models.CharField(max_length=250)
    
    user = models.ManyToManyField(User)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

