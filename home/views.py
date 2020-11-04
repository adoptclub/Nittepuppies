from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .models import RescueComplaint
from .models import Feedback_Note
# from .forms import UserForm
from django.contrib.auth import authenticate, login, logout,models
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render(request, 'index.html')

def handlesignup(request):
    if request.method == 'POST':
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        username = request.POST['username']
        email_number = request.POST['email_number']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        try:
            rescue = request.POST['rescue']
            rescue = True
        except:
            rescue = False

        shelter = request.POST['shelter']
        age = request.POST['age']

        if password == conf_password:
            try:
                myuser = User.objects.create_user(username=username,password=password,
                email_number=email_number,rescue=rescue,shelter=shelter,age=age)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                return render(request,'index.html')
            except:
                messages.error(request, "This Username is already taken, Please change your Username")
                return render(request,'SignUp.html')
        
        else:
            messages.error(request, "Please verify the passwords are Correct")
            return render(request,'SignUp.html')


def handlesignin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        try:
            username = request.POST.get('loginusername')
            password = request.POST.get('loginpassword')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'home.html')

        except:
            messages.error(request,'Your Username or Password was Incorrect !!')
            return redirect('index')

def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'SignUp.html')

def Logout(request):
    logout(request)
    return redirect('index')

def Rescue(request):
    return render(request,'Rescue.html')

def handleRescue(request):
    if request.method == 'POST':
        try:
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            adress1 = request.POST['adress1']
            adress2 = request.POST['adress2']
            city = request.POST['city']
            region = request.POST['region']
            code = request.POST['code']
            country = request.POST['country']
            date_incident = request.POST['date_incident']
            location = request.POST['location']
            details = request.POST['details']

            username = fname + ' ' + lname

            myuser = RescueComplaint.objects.create(username=username, email=email, street_address1=adress1, 
            street_address2=adress2, city=city, region=region, postalcode=code, country=country, 
            date_incident=date_incident, incident_location=location, details=details
            )

            myuser.save()
            messege = "Thank for Helping and Reporting!!!!"
            messages.success(request,messege)
            return render(request,'home.html')
        except:
            feedback(request)
    return render(request,'home.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']

        myuser = Feedback_Note.objects.create(name=name, email=email, comment=comment)

        myuser.save()

        messege = "Thank for Giving Feedback!!!!"
        messages.success(request,messege)
        return render(request,'home.html') 

