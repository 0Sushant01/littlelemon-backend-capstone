#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('bookings/', views.BookingView.as_view(), name='booking-list'),
    path('menu/', views.MenuView.as_view(), name='menu-list'),
]
