from django.db import models
from category.models import *
from subcat.models import *

class products(models.Model):
    name = models.CharField(max_length = 100,unique=True)
    description = models.CharField(max_length = 100,unique=True)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    sub_cat_id = models.ForeignKey(SubCategories, related_name='products',on_delete=models.CASCADE)
    is_featured = models.CharField(max_length = 100)
    

# Create your models here.
