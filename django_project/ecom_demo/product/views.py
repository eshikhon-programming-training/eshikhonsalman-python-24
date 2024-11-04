from django.shortcuts import render,redirect,get_object_or_404


from subcat.models import*
from . models import*

# Create your views here.

def productPageShow(req):
    all_sub_cat = SubCategories.objects.all()
    data = {'data':all_sub_cat}
    return render(req,'products/product.html',data)

def product_insert(req):
    sub_cat_id = req.POST.get('sub_cat_name')
    prod_name = req.POST.get('prod_name')
    prod_desc= req.POST.get('prod_Description')
    prod_act_price= req.POST.get('prod_act_price')
    prod_discount= req.POST.get('prod_discount')
    prod_image= req.FILES.get('prod_image')
    sub_category_instance = get_object_or_404(SubCategories, id=sub_cat_id)
    product_obj = products()
    product_obj.name = prod_name
    product_obj.description = prod_desc
    product_obj.actual_price = prod_act_price
    product_obj.discount = prod_discount
    product_obj.image = prod_image
    product_obj.sub_cat_id = sub_category_instance
    product_obj.save()
    return redirect('productPageShow')