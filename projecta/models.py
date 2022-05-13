from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


class Type(models.Model):
    rows = models.BooleanField(default=False)
    dropdown = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Type"

    def __str__(self):
        return f"{self.rows}{self.dropdown}"


class Category(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='entries', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image= models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(max_length=200, blank=True)
    slug = models.SlugField(max_length=130, editable=False)
    type = models.OneToOneField(Type, on_delete=models.CASCADE, null=True,)
    create_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    class MPTTMeta:
        order_insertion_by = ['title']
    
    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return f"{self.title}"



class Product(models.Model):
    
    class ProductObjects(models.Manager):
        def get_queryset(self):
            return super(Product, self).get_queryset() .filter(status='published')
    
    options = (
           ('draft', 'Draft'),
           ('published', 'Published')
       )
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    description = models.CharField(default="some product", max_length=100)
    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default = 'published',)
    objects = models.Manager() # default manager
    ProductObjects = models.Manager() # custom manager
    link = models.URLField()
    
    def __str__(self):
        return self.title


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title



