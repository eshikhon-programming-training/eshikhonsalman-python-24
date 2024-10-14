from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages

# Create your views here.

def catDemo(req):
    return HttpResponse("this is cat demo view")
def catDemoInsert(req):
    cat_name =  req.POST.get('cat_name')
    if(cat_name==''):
        messages.error(req, "The category name cannot be empty")

    elif(len(cat_name)<2):
        messages.error(req, "The name field length must be a minimum of 2")
    elif(Categories.objects.filter(name=cat_name).exists()):
        messages.error(req, "The given value already exists")
    else:
        cat_obj = Categories()
        cat_obj.name = cat_name
        cat_obj.save()
        messages.success(req, "Category created successfully")
        
    return redirect('catpageshow')

def catPageShow(req):
    return render(req,'category/cat.html')
