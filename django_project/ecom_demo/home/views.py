from django.shortcuts import render

from category.models import *

# Create your views here.

def homePageShow(req):
    all_cats = Categories.objects.all()
    cats = {'cats':all_cats}

    return render(req,'home/home.html',cats)
