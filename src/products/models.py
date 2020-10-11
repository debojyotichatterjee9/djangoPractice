from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
# COMMENT: Inherit this from the default Django class of model 
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title       = models.CharField(max_length=120) #max_legth is compulsory when using a char field, you can set it to max_length=None
    description = models.TextField(blank = True, null = True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField()
    available   = models.BooleanField(default = True)
    
    def get_absolute_url(self):
        print(str(self.id))
        return reverse("details", kwargs={"product_id": str(self.id)})