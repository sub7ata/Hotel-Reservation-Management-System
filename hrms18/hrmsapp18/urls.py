from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hotels', views.HotelView)
router.register('managers',views.ManagerView)
router.register('rooms',views.RoomView)
router.register('guests',views.GuestView)
router.register('bookings',views.BookingView)
urlpatterns = [
    path('', include(router.urls))
]
