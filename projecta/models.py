from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, default =1 )
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    image = models.ImageField()
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.name
