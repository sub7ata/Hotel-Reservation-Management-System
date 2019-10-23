from rest_framework import serializers
from .models import Booking,Room,Manager,Hotel,Guest


# class HotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Hotel
#         fields= ('name','manager','city',)

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields =('name','gender','id','guest',)

# class GuestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Guest
#         fields = ('name','gender',)
#
# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Room
#         fields =('room_no','room_type','is_available',)
#
# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Booking
#         fields =('guest','no_of_guests','Room_no','checkin_time','checkout_time','charge',)
