from django.db import models
from cloudinary.models import CloudinaryField

# models
class Photo(models.Model):
  image = CloudinaryField('image')
