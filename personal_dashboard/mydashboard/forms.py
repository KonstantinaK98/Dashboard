from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Project,Note
  

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SettingsForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']               


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','color','user']  


class ProjectEditForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','color']

class NoteCreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title','description','color','user']  


class NoteEditForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title','description','color']        