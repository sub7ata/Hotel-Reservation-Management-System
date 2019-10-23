from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save


class Guest(models.Model):
    name = models.CharField(max_length=200)
    gender=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    guest=models.ForeignKey(Guest, on_delete=models.CASCADE)
    gender=models.CharField(default="Male", max_length=10)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    city= models.CharField(max_length=200)
    # id=models.IntegerField()

    def __str__(self):
        return self.name


class Room(models.Model):
    room_no=models.IntegerField(default=101)
    hotel=models.ForeignKey(Hotel,null=True,on_delete=models.CASCADE)
    # =models.IntegerField()
    room_type=models.CharField(max_length=200,default='standard')
    is_available=models.BooleanField(default=True)

    @property
    def get_price(self):
        price = 0
        if self.room_type == 'Deluxe':
            price = 1000
        elif self.room_type == 'Standard':
            price = 800
        elif self.room_type == 'Single':
            price = 500
        elif self.room_type == 'Double':

            price = 700
        elif self.room_type == 'Super Deluxe':
            price = 1500
        else:
            if self.room_type == 'Presidential':
                price = 2000
        return price

    # r_type=models.CharField(max_length=200)
    def __str__(self):
        return str(self.room_no)


    # def price(self):
    #     if self.room_type=='standard':
    #         return 1000

class Booking(models.Model):
    # guest_name=models.CharField(max_length=200)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    checkin_time=models.DateTimeField(default=datetime.today())
    checkout_time=models.DateTimeField()
    no_of_guests=models.IntegerField(default=1)
    # is_available=models.BooleanField(default=True)


    # def bill(self):
    #     if :
    #         difference=(self.checkin_time-self.checkout_time).Days
    #         if

    @property
    def Room_no(self):
        return self.room.room_no


    @property
    def charge(self):
        total_fee = self.checkout_time - self.checkin_time
        if self.room.room_type == 'Deluxe':
            return total_fee.days * 1000
        elif self.room.room_type == 'Standard':
            return total_fee.days * 800
        elif self.room.room_type == 'Single':
            return total_fee.days * 500
        elif self.room.room_type == 'Double':
            return total_fee.days * 700
        elif self.room.room_type == 'Super Deluxe':
            return total_fee.days * 1500
        elif self.room.room_type == 'Presidential':
            return total_fee.days * 2000


@receiver(post_save,sender=Booking)
def  RType(sender, instance, created, **kwargs):
    obj = instance.room
    if created:
        obj.is_available = False
        obj.save()
    # if obj.is_available ==False:
    #     if obj.checkin_time>= checkin_time and obj.checkin_time<= checkout_time:
    #         return  "room is not available in the selected dates"
    #     if obj.checkin_time< checkin_time and obj.checkout_time> checkout_time:
    #         return



# @receiver(post_save,sender=Guest)
# def be_active(sender,instance,active,**kwargs):
#
