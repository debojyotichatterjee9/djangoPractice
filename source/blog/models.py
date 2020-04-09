from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title        = models.CharField(max_length=120)  # max_length = required length
    content      = models.TextField(blank=True, null=True)
    active       = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"id": self.id})
        # return f"/blog/{self.id}"
