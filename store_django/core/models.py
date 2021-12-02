from django.db import models
from django.db.models.deletion import DO_NOTHING

class Category(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    title = models.CharField(max_length=250, blank=True)  
    category = models.ForeignKey(Category, blank=True, on_delete=DO_NOTHING)
    description = models.CharField(max_length= 700)
    image = models.URLField(max_length=250)
    comment = models.CharField(max_length=250, null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)

    def __str__(self):
        return self.title
    
