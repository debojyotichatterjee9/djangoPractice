from django.db import models

# Create your models here.
# COMMENT: Inherit this from the default Django class of model 
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_legth is compulsory when using a char field, you can set it to max_length=None
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField()
    available    = models.BooleanField()