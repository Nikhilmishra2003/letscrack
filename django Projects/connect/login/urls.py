from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include
from.import views
from django.urls import path

urlpatterns = [

    path('register/', views.register, name="register"),
    # path('login/', views.LoginPage,name='login'),
    path('home/', views.HomePage, name='home'),
    path('home/login/', views.LoginPage, name='LoginPage'),
    path('logout/', views.LogoutPage, name='logout'),
    path('home/dashboard/', views.dashboard, name='dashboard'),
    path('UPSC Civil Service Exam/', views.find_out_more, name='find_out_more'),
    path('National Testing Agency/', views.find_out_more, name='find_out_more_1'),
    path('National Defence Academy/', views.find_out_more, name='find_out_more_2'),
    path('Madhya Pradesh Public Service Commission (MPPSC/', views.find_out_more, name='find_out_more_3'),


]