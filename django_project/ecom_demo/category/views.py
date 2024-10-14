from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def catDemo(req):
    return HttpResponse("this is cat demo view")
def catDemoInsert(req):
    return HttpResponse("this is cat demo Insert view")

def catPageShow(req):
    return render(req,'category/cat.html')
