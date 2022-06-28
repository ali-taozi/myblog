from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.urls import reverse

def register(request):
    title='注册博客'
    pageTitle='用户注册'
    confirmPassword=True
    button='注册'
    urlText='用户登录'
    urlName='userLogin'
    if request.method=='POST':
        u=request.POST.get('username','')
        p=request.POST.get('password','')
        cp=request.POST.get('cp','')
        if MyUser.objects.filter(username=u):
            tips='用户已存在'
        elif cp!=p:
            tips='两次密码输入不一致'
        else:
            d={
                'username':u,
                'password':p,
                'is_'
            }
