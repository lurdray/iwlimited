from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('factory/', views.factory, name='factory'),
    path('category/', views.category, name='category'),
    path('category/<slug:slug>/', views.SingleCategoryView, name='single_category'),
    path('showroom/', views.showroom, name='showroom'),
    path('quote/', views.quote, name='quote'),
    path('stock/', views.stock, name='stock'),
    
]
