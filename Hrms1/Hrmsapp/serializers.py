from rest_framework import serializers
from .models import *

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Guest
        fields = ('name','age',)


class HotelSerializer(serializers.ModelSerializer):
    # staff=StaffSerializer()
    class Meta:
        model= Hotel
        fields= ('id','name','city','phone',)

class RoomSerializer(serializers.ModelSerializer):
    hotel=HotelSerializer
    class Meta:
        model=Room
        fields =('id','room_no','room_type','is_available',)

class BookingSerializer(serializers.ModelSerializer):
    guest=GuestSerializer
    room=RoomSerializer
    hotel=HotelSerializer
    class Meta:
        model= Booking
        fields =('guest','no_of_guests','hotel','checkin_date','checkout_date','check_out','charge',)
