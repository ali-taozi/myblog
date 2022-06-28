from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.urls import reverse

#用户注册
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
                #设置用户为超级管理员状态
                'is_superuser':1,
                #激活用户状态
                'is_staff':1
            }
            user=MyUser.objects.create_user(**d)
            user.save()
            tips='注册成功，请登录'
            logout(request)
            return redirect(reverse('userLogin'))
    return render(request,'user.html',locals())

#用户登录
def userLogin(request):
    title='登录博客'
    pageTitle='用户登录'
    confirmPassword=False
    button='登录'
    urlText='用户注册'
    urlName='register'
    if request.method=='POST':
        u=request.POST.get('username','')
        p=request.POST.get('password','')
        if MyUser.objects.filter(username=u):
            user=authenticate(username=u,password=p)
            if user:
                if user.is_active:
                    login(request,user)
                kwargs={'id':request.user.id,'page':1}
                return redirect(reverse('article',kwargs=kwargs))
            else:
                tips='账号或密码错误，请重新输入'
        else:
            tips='用户bu'
            d={
                'username':u,
                'password':p,
                'is_superuser':1,
                'is_staff':1
            }
            user=MyUser.objects.create_user(**d)
            user.save()
            tips='注册成功，请登录'
            logout(request)
            return redirect(reverse('userLogin'))
    return render(request,'user.html',locals())