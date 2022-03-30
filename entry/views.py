from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings 
from django.core.mail import send_mail 

def about(request):
    return render(request, 'about.html')
def mail(request):
    subject = 'welcome to GFG world'
    message = 'Hithank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = ['agryashu23@gmail.com', ] 
    send_mail( subject, message, email_from, recipient_list ) 
    return redirect('/')
    

# Create your views here.
def plan(request):
    if request.user.is_authenticated:
        return render(request, 'plan.html')
    else:
        return render(request, 'login.html')
def entry(request):
    if request.user.is_authenticated:
        return render(request, 'entry.html')
    else:
        return render(request, 'login.html')
def okok(request):
    return redirect('/')
def planm(request):
    if request.user.is_authenticated:
        return render(request, 'planm.html')
    else:
        return render(request, 'login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    
    else:
        return render(request, 'login.html')
def gallery(request):
    return render(request, 'gallery.html')
