from django.db import models
from django.urls import reverse
import uuid
class User(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname       = models.CharField(max_length=120) #max_legth is compulsory when using a char field, you can set it to max_length=None
    lname       = models.CharField(max_length=120)
    email       = models.CharField(max_length=120)
    password    = models.CharField(max_length=120)
    contact     = models.CharField(max_length=13)
    address     = models.TextField(blank = True, null = True)
    enabled     = models.BooleanField(default = True)
    deleted     = models.BooleanField(default = False)
    
    def get_absolute_url(self):
        return reverse("users:details", kwargs={"user_id": str(self.id)})