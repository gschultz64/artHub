from django.db import models
from django.contrib.auth.models import User

# models

class Media(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return 
