"""personal_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mydashboard import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage, name='loginPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name="registerPage"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('projects', views.projects, name='projects'),
    path('logout/', auth_views.LogoutView.as_view(next_page="loginPage"), name='logout'),
    path('createProject', views.createProject, name='createProject'),
    path('editProject/<str:pk_project>/', views.editProject, name="editProject"),
    path('deleteProject/<str:pk_delete>/', views.deleteProject, name="deleteProject"),
    path('notes', views.notes, name='notes'),
    path('createNote', views.createNote, name='createNote'),
    path('editNote/<str:pk_note>/', views.editNote, name="editNote"),
    path('deleteNote/<str:pk_delete>/', views.deleteNote, name="deleteNote"),
    path('calendar', views.calendar, name='calendar'),
]
