from django.contrib import admin
from django.urls import path
from mydashboard import views

urlpatterns = [
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name="registerPage"),
    path('home', views.home, name='home'),
    path('logout/', views.logoutPage, name="logoutPage"),
    path('notes/', views.notes, name="notes"),
    path('editNote/<str:pk_note>/', views.editNote, name="editNote"),
    path('deleteNote/<str:pk_delete>/', views.deleteNote, name="deleteNote"),
    path('createNote', views.createNote, name="createNote"),
    path('projects/', views.projects, name="projects"),
    path('editProject/<str:pk_project>/', views.editProject, name="editProject"),
    path('deleteProject/<str:pk_delete>/', views.deleteProject, name="deleteProject"),
    path('createProject', views.createProject, name="createProject"),
    path('',views.loginPage, name='loginPage'),
    path('calendar/',views.calendar, name="calendar"),
]