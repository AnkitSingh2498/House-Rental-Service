from django.contrib.admin.sites import site 
from django.contrib import admin
from . import models
from Rent.models import saveAd
class SaveAdv(admin.ModelAdmin):
    list_display=('Owner_Name','Owner_pic','House_address','Building_img1','Room_img1','Room_img2','Room_img3','House_type','AllowedFor','House_description','city','state','district','pin_no','phone_no','Alt_phone_no','Price','date_added')
admin.site.register(saveAd)
# Register your models here.
