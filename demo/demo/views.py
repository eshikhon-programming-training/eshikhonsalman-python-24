from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *

def home(req):
    single_data = About.objects.get(id=9)
    service_data = Service.objects.all()
    data = {'d':single_data,'s_data':service_data}
    return render(req,'index.html',data)


def about(req):
    all_data = About.objects.all() #queryset
    data = {'about_d':all_data}
    return render(req,'about.html',data)
def service(req):
    # all_data = About.objects.all() #queryset
    # data = {'about_d':all_data}
    return render(req,'service.html')

def aboutEdit(req,uid):
    single_data = About.objects.get(id=uid)
    data = {'d':single_data}
    return render(req,'edit.html',data)

def aboutDel(req,uid):
    single_data = About.objects.get(id=uid)
    single_data.delete()
    return redirect('about_home')


def aboutInsert(req):
    name = req.POST.get('fname')
    desc = req.POST.get('desc')
    fb = req.POST.get('fb')
    git = req.POST.get('git')
    phone = req.POST.get('phone')
    email = req.POST.get('email')
    u_image = req.FILES.get('img')

    about_obj = About()

    about_obj.name = name
    about_obj.description = desc
    about_obj.fb = fb
    about_obj.git = git
    about_obj.phone = phone
    about_obj.email = email
    about_obj.s_image = u_image

    about_obj.save()


    return redirect('about_home')
def serviceInsert(req):
    name = req.POST.get('s_name')
    desc = req.POST.get('s_desc')
    img = req.FILES.get('img')

    service_obj = Service()
    service_obj.s_name = name
    service_obj.s_description = desc
    service_obj.s_image = img
    service_obj.save()

    return  redirect('service_admin')

def aboutUpdate(req):
    id = req.POST.get('uid')
    name = req.POST.get('fname')
    desc = req.POST.get('desc')
    fb = req.POST.get('fb')
    git = req.POST.get('git')
    phone = req.POST.get('phone')
    email = req.POST.get('email')

    about_obj = About.objects.get(id=id)

    about_obj.name = name
    about_obj.description = desc
    about_obj.fb = fb
    about_obj.git = git
    about_obj.phone = phone
    about_obj.email = email

    about_obj.save()


    return redirect('about_home')
    # return render(req,'about.html')
def demo2(req):
    a= 10
    b = 20
    prod_price = [1,2,3,4]
    sum = a+b
    sub = a-b
    data = {'d':sum,'sub':sub,'prod':prod_price}
    return render(req,'basic2.html',data)