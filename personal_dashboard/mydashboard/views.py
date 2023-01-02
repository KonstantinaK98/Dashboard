from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NoteEditForm,NoteCreateForm,CreateUserForm,SettingsForm,ProjectCreateForm,ProjectEditForm
import datetime
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group,User
from .models import Note,Project

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['user','admin'])
def dashboard(request):
    return render(request, 'mydashboard/base.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['user','admin'])
def projects(request):   
    un = request.user
    projects = Project.objects.all().filter(user=un)
    projects_num = projects.count()
    context = {
        "projects":projects,
        "projects_num":projects_num,
    }
    return render(request, "mydashboard/Projects/projects.html", context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')       
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

@login_required(login_url='loginPage')
def createProject(request):
    username = request.user
    un = User.objects.all().get(username=username).id
    form = ProjectCreateForm()
    if request.method == "POST":
        form = ProjectCreateForm(request.POST)
        print(form['user'].value())
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project was successfully created!')
            return redirect('projects')
    context = {"form":form,
                "id":un,
                }
    return render(request, "mydashboard/Projects/createProject.html", context)   

@login_required(login_url='loginPage')
def editProject(request, pk_project):
    project = Project.objects.get(id=pk_project)
    form = ProjectEditForm(instance=project)
    if request.method == "POST":
        form = ProjectEditForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            project.date_created = datetime.datetime.now()
            project.save()
            messages.success(request, 'Your project was successfully updated!')
            return redirect('projects')
    context = {
        "project":project,
        "form":form,
    }
    return render(request, "mydashboard/Projects/editProject.html", context)    

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

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['user','admin'])
def calendar(request):
    return render(request, "mydashboard/Calendar/calendar.html")
    
      

@login_required(login_url='loginPage')
def deleteProject(request, pk_delete):
    project = Project.objects.get(id=pk_delete)
    if request.method == "POST":
        project.delete()
        messages.success(request, 'Your project was successfully deleted!')
        return redirect('projects')
    context = {
        "project":project,
    }
    return render(request, 'mydashboard/Projects/deleteProject.html', context)
