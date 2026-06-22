from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games, name='games'),
    path('games/<int:product_id>/', views.product_detail, name='product_detail'),
    path('psplus/', views.psplus, name='psplus'),
    path('contact/', views.contact, name='contact'),
]