from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm,SettingsForm
import datetime
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group,User

def home(request):
    return render(request, 'mydashboard/base.html')

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')       
        else:
            messages.info(request, "Username OR Password is incorrect!")       
            
    context = {}
    return render(request, 'mydashboard/login.html')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="user")
            user.groups.add(group)
            messages.success(request, "Your account was successfully created!")
            return redirect('loginPage')
        else:
            messages.error(request, "")    
    context = {
        "form":form,
    }
    return render(request, 'mydashboard/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('loginPage')



