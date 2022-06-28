from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.urls import reverse

def register(request):
    title='zhe'
