from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        userName = request.POST['username'];
        password = request.POST['password'];
        print(userName,password);
    return render(request,'login.html',{})

def signup(request):
    if request.method == 'POST':
        userName = request.POST['username'];
        password = request.POST['password'];
        firstname = request.POST['firstname'];
        lastname = request.POST['lastname'];
        email = request.POST['email'];
        number = request.POST['number'];
        rePassword = request.POST['repassword'];
        print(userName,firstname,lastname,email,number,password,rePassword);
    return render(request,'signup.html',{})