from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),    
    path('about/', views.about, name='about'),    
    path('contact/', views.contactUS, name='contact'),    
    path('services/', views.services, name='services'),    
    path('service1/', views.service1, name='service1'),    
    path('service2/', views.service2, name='service2'),    
    path('service3/', views.service3, name='service3'),    
]