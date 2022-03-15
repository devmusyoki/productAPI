from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone

class Category(MPTTModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    parentCategory = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            related_name='subcategories',
                            on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    class MPTTMeta:
        order_insertion_by = ['title']
        parent_attr = 'parentCategory'
        
      
        
        def __str__(self):
            return self.title



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
    description = models.CharField(default="some product", max_length=100)
    image = models.ImageField()
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(timezone.now())
    status = models.CharField(max_length=10, choices=options, default = 'published',)
    objects = models.Manager() # default manager
    ProductObjects = models.Manager() # custom manager
    link = models.URLField()
    
    
    class Meta:
        ordering = ('-published',)
 

    def __str__(self):
        return self.name
