from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from Rent.models import saveAd
# Create your views here.
def index(request): 
    AdData=saveAd.objects.all()
    return render(request,'Rent/html/index.html',{'AdData':AdData})

def about(request):
    return render(request,'Rent/html/aboutus.html')

def contact(request):
    return render(request,'Rent/html/contact.html')

def owner(request):
    return render(request,'Rent/html/owner.html')

def saveAdd(request):
    if request.method=="POST":
        Owner_Name = request.POST.get('Owner_Name')
        Owner_pic = request.FILES['Owner_pic']
        House_address  =request.POST.get('House_address')
        Building_img1 = request.FILES['Building_img1']
        Room_img1 = request.FILES['Room_img1']
        Room_img2 = request.FILES['Room_img2']
        Room_img3 = request.FILES['Room_img3']
        
        
        House_type =request.POST.get('House_type')
        AllowedFor = request.POST.get('AllowedFor')
        House_description = request.POST.get('House_description')
        city = request.POST.get('city')
        state = request.POST.get('state')
        district = request.POST.get('district')
        pin_no = request.POST.get('pin_no')
        phone_no = request.POST.get('phone_no')
        Alt_phone_no = request.POST.get('Alt_phone_no')
        Price = request.POST.get('Price')
        date_added = request.POST.get('date_added')
        

        sAd=saveAd(Owner_Name=Owner_Name,Owner_pic=Owner_pic,House_address=House_address,Building_img1=Building_img1,Room_img1=Room_img1,Room_img2=Room_img2,Room_img3=Room_img3,House_type=House_type,AllowedFor=AllowedFor,House_description=House_description,city=city,state=state,district=district,pin_no=pin_no,phone_no=phone_no,Alt_phone_no=Alt_phone_no,Price=Price,date_added=date_added)
        sAd.save()
        messages.success(request, "Thank you for posting your House to our Apna Ashiyana.")
    
    return render(request,'Rent/html/index.html') 


def tenant(request):
    AdData=saveAd.objects.all()
    return render(request,'Rent/html/properties.html',{'AdData':AdData})  

def signup(request):
    return render(request,'')                

def handlelogout(request):
    
    logout(request)
    # messages.success("Successfully logged out")
    return redirect('RentHome')  

def houseDetails(request,id):
    det = saveAd.objects.filter(id=id).first()
    context ={
        'det': det 
    }

    return render(request,'Rent/html/prod.html',context)