from django import forms
from django.contrib import admin
from .models import Guest,Hotel,Room,Booking
# ,Hotel,Room,Booking
from django import forms
import re 
# class GuestAdminForm(forms.ModelForm):
#     def __init__(self,*args,**kwargs):
#         super(GuestAdminForm,self).__init__(*args,**kwargs)

#     def clean(self):
#         contact = self.cleaned_data.get('phone')
#         regex=r'^\d[10]$'
#         match=re.match(regex,contact)
#         if match is None:
#             raise forms.ValidationError('please enter a valid phone number', code='error')
#         return self.cleaned_data

#     def save(self,commit=True):
#         return super(GuestAdminForm,self).save(commit=commit)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name','age','phone',)
    # form = GuestAdminForm

admin.site.register(Guest,GuestAdmin)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','city','phone',)
    # form = HotelAdminForm
admin.site.register(Hotel,HotelAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display=('room_no','hotel','room_type','rate','is_available',)
    ordering = ['room_no']
    # form = RoomAdminForm

admin.site.register(Room,RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display=('guest','room','hotel','no_of_guests','checkin_date','checkout_date','check_out','charge',)
    # form = BookingAdminForm

admin.site.register(Booking,BookingAdmin)

