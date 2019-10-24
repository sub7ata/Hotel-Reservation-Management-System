from rest_framework import serializers
from .models import Booking,Room,Manager,Hotel,Guest




class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Guest
        fields = ('name','age',)

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    guest=GuestSerializer()
    class Meta:
        model = Manager
        fields =('name','gender','id','guest',)



class HotelSerializer(serializers.ModelSerializer):
    manager=ManagerSerializer()
    class Meta:
        model= Hotel
        fields= ('name','manager','city',)
#
class RoomSerializer(serializers.ModelSerializer):
    hotel=HotelSerializer
    class Meta:
        model=Room
        fields =('room_no','room_type','is_available',)
#
# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Booking
#         fields =('guest','no_of_guests','Room_no','checkin_time','checkout_time','charge',)
