from django import forms
from django.contrib import admin
from .models import Booking,Room,Manager,Hotel,Guest
# Register your models here.

class ManagerAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ManagerAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        name=self.cleaned_data.get('name')
        if len(name)<4:
            raise forms.ValidationError('name should be more than 4',code='error')
        return self.cleaned_data


    def save(self,commit=True):
        return  super(ManagerAdminForm,self).save(commit==commit)

class GuestAdminForm(forms.ModelForm):
    def __init__(self):
        super(GuestAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError('name should be more than 4', code='error')
        return self.cleaned_data

    def save(self,commit=True):
        return super(GuestAdminForm,self).save(commit=commit)

class HotelAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(HotelAdminForm,self).__init__(*args,**kwargs)

    def save(self, commit=True):
        return super(HotelAdminForm,self).save(commit=commit)

class RoomAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(RoomAdminForm,self).__init__(*args,**kwargs)

    def save(self, commit=True):
        return super(RoomAdminForm,self).save(commit=commit)

class BookingAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookingAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        no_of_guests = self.cleaned_data.get('no_of_guests')
        if no_of_guests >3:
            raise forms.ValidationError('room cannot accomodate more than 3', code='error')
        name1 = self.cleaned_data.get('guest')
        if name1.name > 1:
            raise forms.ValidationError(' u literally cannot make another booking now', code='error')
        return self.cleaned_data


    def save(self, commit=True):
        return super(BookingAdminForm,self).save(commit=commit)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name','gender',)
    form = ManagerAdminForm

admin.site.register(Manager,ManagerAdmin)

class GuestAdmin(admin.ModelAdmin):
    list_display = ('name','gender',)
    form = GuestAdminForm

admin.site.register(Guest,GuestAdmin)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','city',)
    form = HotelAdminForm
admin.site.register(Hotel,HotelAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display=('room_no','room_type','is_available','get_price',)
    ordering = ['room_no']
    form = RoomAdminForm

admin.site.register(Room,RoomAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display=('guest','no_of_guests','Room_no','checkin_time','checkout_time','charge',)
    form = BookingAdminForm

admin.site.register(Booking,BookingAdmin)








