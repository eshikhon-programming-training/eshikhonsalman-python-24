from django.shortcuts import render

from category.models import *
from subcat.models import *
from product.models import *
from django.db.models import Prefetch, Count

# Create your views here.

def homePageShow(req):
    all_cats_subcats = SubCategories.objects.prefetch_related('cat_id').all()
    all_products = products.objects.all()

    for i in all_products:
        print(i.actual_price)
        print(i.discount)
        i.discount_price = i.actual_price - ((i.actual_price*i.discount)/100)
        # print(discount_price)
    # for i in all_cats_subcats:
    #     print(i)

    # Fetch distinct categories with their subcategories
    categories = Categories.objects.annotate(subcat_count=Count('subcategories')).filter(subcat_count__gt=0).prefetch_related(
        Prefetch('subcategories', queryset=SubCategories.objects.all())
    ).distinct()

    # Now render the categories and their subcategories
    for category in categories:
        print(f"Category: {category.name}")
        for subcat in category.subcategories.all():
            print(f"  Subcategory: {subcat.name}")  # Adjust according to your subcategory field

    cats = {'cats_subcats':categories,'prod':all_products}

    return render(req,'home/home.html',cats)

def product_details(req,id):
    single_product = products.objects.get(id=id)
    single_product.discount_price = single_product.actual_price - ((single_product.actual_price*single_product.discount)/100)
    print(single_product.discount_price)
    data = {'data':single_product}
    return render(req,'products/detail.html',data)
