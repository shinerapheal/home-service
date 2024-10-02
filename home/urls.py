from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('home',views.index),
     path('', views.login_view, name='login_view'),
    path('worker_register/', views.worker_register, name='worker_register'),
    path('customer_register/', views.customer_register, name='customer_register'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('worker_home',views.worker_home,name='worker_home'),
    path('customer_home',views.customer_home,name='customer_home'),
    path('aboutus',views.aboutus),
    path('service',views.services),
    path('ac',views.ac),
    path('fridge',views.fridge),

    path('book',views.book),
    path('confi',views.confi),
    path('cosreq',views.cusreq),
    path('workdet',views.wrkdet),
    path('bookstatus',views.bookstatus),
    path('alo',views.alo),

    path('approve',views.approve),
    path('worfil',views.worfil),
    path('cusde',views.cusde),
    path('cusfil',views.cusfil),







    
]