from django.db import models
from category.models import *

class SubCategories(models.Model):
    name = models.CharField(max_length = 100,unique=True)
    cat_id = models.ForeignKey(Categories, related_name='subcategories',on_delete=models.CASCADE)
    

# Create your models here.
