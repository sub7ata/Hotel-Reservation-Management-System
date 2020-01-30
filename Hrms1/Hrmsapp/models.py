from django.db import models
from datetime import datetime,date,timedelta
# from django.utils.timezone.now
from django.dispatch import receiver
from django.db.models.signals import post_save

class Guest(models.Model):
    name = models.CharField(max_length=200)
    age=models.IntegerField(default=20)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    # staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    city= models.CharField(max_length=200)
    # id=models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    room_no=models.IntegerField(default=101)
    hotel=models.ForeignKey(Hotel,null=True,on_delete=models.CASCADE)
    # =models.IntegerField()
    room_type=models.CharField(max_length=200,default='standard')
    rate=models.FloatField()
    is_available=models.BooleanField(default=True)
    no_of_beds=models.IntegerField(default=3)
    # check_out=models.BooleanField(default=False)

    
    def __str__(self):
        return str(self.room_no)


    def hotel_name(self):
        return self.hotel.name

class Booking(models.Model):
    # guest_name=models.CharField(max_length=200)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    checkin_date=models.DateTimeField(default=datetime.now())
    checkout_date=models.DateTimeField(default=datetime.now() + timedelta(days=1))
    check_out=models.BooleanField(default=False)
    no_of_guests=models.IntegerField(default=1)

    def __str__(self):
        return self.guest.name

    def charge(self):
        if self.check_out:
            if self.checkin_date==self.checkout_date:
                return self.room.rate
            else:
                time_delta = self.checkout_date - self.checkin_date
                total_time = time_delta.days
                total_cost =total_time*self.room.rate
                # return total_cost
                return total_cost
        else:
            return 'calculated when checked out'        
    
@receiver(post_save,sender=Booking)
def  RType(sender, instance, created, **kwargs):
    room = instance.room
    if created:
        room.is_available = False
    room.save()
    if instance.check_out ==True:
        room.is_available=True
    room.save()    
