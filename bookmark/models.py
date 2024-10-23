from django.db import models

class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    makanan = models.ManyToManyField
# Create your models here.
