from django.db import models

# Create your models here.
# COMMENT: Inherit this from the default Django class of model 
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='This is a sample sumary.')