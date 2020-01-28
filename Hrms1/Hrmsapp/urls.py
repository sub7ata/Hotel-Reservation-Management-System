from rest_framework import routers
from Hrmsapp import views
from django.urls import path,include,re_path
from  Hrmsapp.views import *

# app_name ='Hrmsapp'

urlpatterns = [
    path('hotel/',api_hotel_list_view,name='hotel-objects'),
    path('room/',api_room_list_view,name='room-objects'),
    path('guest/',api_guest_list_view,name='guest-objects'),
    path('booking/',api_booking_list_view,name='booking-objects')
]
