from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NoteEditForm,NoteCreateForm,CreateUserForm,SettingsForm
import datetime
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group,User
from .models import Note


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


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['user','admin'])
def notes(request):
    un = request.user
    notes = Note.objects.all().filter(user=un)
    notes_num = notes.count()
    context = {
        "notes":notes,
        "notes_num":notes_num,
    }
    return render(request, "mydashboard/Notes/notes.html", context)

@login_required(login_url='loginPage')
def editNote(request, pk_note):
    note = Note.objects.get(id=pk_note)
    form = NoteEditForm(instance=note)
    if request.method == "POST":
        form = NoteEditForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            note.date_created = datetime.datetime.now()
            note.save()
            messages.success(request, 'Your note was successfully updated!')
            return redirect('notes')

    context = {
        "note":note,
        "form":form,
    }
    return render(request, "mydashboard/Notes/editnote.html", context)  

@login_required(login_url='loginPage')
def createNote(request):
    username = request.user
    un = User.objects.all().get(username=username).id
    form = NoteCreateForm()
    if request.method == "POST":
        form = NoteCreateForm(request.POST)
        print(form['user'].value())
        if form.is_valid():
            form.save()
            messages.success(request, 'Your note was successfully created!')
            return redirect('notes')
    context = {"form":form,
                "id":un,
                }
    return render(request, "mydashboard/Notes/createnotes.html", context) 

@login_required(login_url='loginPage')
def deleteNote(request, pk_delete):
    note = Note.objects.get(id=pk_delete)
    if request.method == "POST":
        note.delete()
        messages.success(request, 'Your note was successfully deleted!')
        return redirect('notes')
    context = {
        "note":note,
    }
    return render(request, 'mydashboard/Notes/deletenotes.html', context)       