from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous inputs

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('RentHome')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('RentHome')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('RentHome')
         
            
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been created successfully. ")

        return redirect('RentHome')
    else:
        return HttpResponse('Not found')    
    
   
def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully loged in.")
            return redirect('RentHome')

        else:
            messages.error(request, "Invalid Credentials.") 
            return redirect('RentHome')   

    

def handlelogout(request):
    
    logout(request)
    # messages.success("Successfully logged out")
    return redirect('RentHome')    