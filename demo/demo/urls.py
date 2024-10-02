"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    path('demo2/',views.demo2),
    path('about/',views.about, name='about_home'),
    path('service/',views.service, name='service_admin'),
    path('about/insert',views.aboutInsert, name='about_insert'),
    path('service/insert',views.serviceInsert, name='service_insert'),
    path('about/edit/<int:uid>',views.aboutEdit, name='about_edit'),
    path('about/edit',views.aboutUpdate, name='about_update'),
    path('about/delete/<int:uid>',views.aboutDel, name='about_delete'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
