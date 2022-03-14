from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    class ProductObjects(models.Manager):
        def get_queryset(self):
            return super(Product, self).get_queryset() .filter(status='published')
    
    options = (
           ('draft', 'Draft'),
           ('published', 'Published')
       )
    
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, default =1 )
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    image = models.ImageField()
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(default = timezone.now())
    status = models.CharField(max_length=10, choices=options, default = 'published',)
    objects = models.Manager() # default manager
    link = models.URLField()
    
    
    class Meta:
        ordering = ('-published')
 

    def __str__(self):
        return self.name
