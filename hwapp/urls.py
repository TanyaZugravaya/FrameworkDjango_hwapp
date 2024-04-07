from django.urls import path
from . import views
from .views import OrderList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/', OrderList.as_view(), name='order-list'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),

]
