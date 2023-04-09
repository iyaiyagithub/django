from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
      path('IM/', views.product_list, name = 'product_list'),
      path('IM/', views.product_create, name = 'product_create'),
      path('IM/delete/<int:id>/', views.product_delete, name = 'product_delete'),
      path('IM/<int:id>/', views.inbound_create, name = 'inbound_create'),
      path('IM/', views.outbound_create, name = 'outbound_create'),
      path('IM/', views.inventory, name = 'inventory'),
      

]
