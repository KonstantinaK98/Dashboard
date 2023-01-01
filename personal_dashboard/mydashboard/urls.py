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
    path('',views.loginPage, name='loginPage'),
]