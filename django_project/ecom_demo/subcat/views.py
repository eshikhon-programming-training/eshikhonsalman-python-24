from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from category.models import *
from .models import *
from django.contrib import messages


def subCatPageShow(req):
    all_cats = Categories.objects.all()
    all_subcats = SubCategories.objects.prefetch_related('cat_id').all()
    cats = {'cats':all_cats,'subcats':all_subcats}
    return render(req,'subcat/subcat.html',cats)

def subcatDemoInsert(req):
    cat_id = req.POST.get('cat_name')
    sub_cat_name = req.POST.get('sub_cat_name')
    category_instance = get_object_or_404(Categories, id=cat_id)
    sub_cat_obj = SubCategories()
    sub_cat_obj.name = sub_cat_name
    sub_cat_obj.cat_id = category_instance
    sub_cat_obj.save()
    messages.success(req, "Sub Category created successfully")

    return redirect('subcatpageshow')
