from django.db import models

class About(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length=500)
    fb = models.CharField(max_length=500)
    git = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    s_image = models.ImageField(upload_to='images/')

class Service(models.Model):
    s_name = models.CharField(max_length = 100)
    s_description = models.CharField(max_length=500)
    s_image = models.ImageField(upload_to='services/')
    



