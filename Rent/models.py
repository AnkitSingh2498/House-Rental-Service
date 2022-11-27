from django.db import models

# Create your models here.s
class saveAd(models.Model):
    # user = models.ForeignKey()
    Owner_Name = models.CharField(max_length=100,null=True)
    Owner_pic = models.ImageField(upload_to='Housepic', null=True, blank=True)
    House_address  =models.TextField(null=False)
    Building_img1 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    Room_img1 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    Room_img2 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    Room_img3 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    House_type = models.CharField(max_length=100,null = False,default="2BHK/3BHK/SINGLE")
    AllowedFor = models.CharField(max_length=100, null=False, default="All")
    House_description = models.TextField(null = False,default="Write something About how good and what are the facilities your renters will get there like electricity/Water etc")
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    district = models.CharField(max_length=100,null=False,default="Not Mention")
    pin_no = models.IntegerField(null=True)
    phone_no = models.CharField(max_length=100,default="")
    Alt_phone_no = models.CharField(max_length=100,default="")
    Price = models.IntegerField(null = True, default='1000')
    date_added = models.DateTimeField(auto_now_add=True)

