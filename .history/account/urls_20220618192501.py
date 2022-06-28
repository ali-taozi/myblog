from django.urls import path
from .views import *
urlpatterns = [
    #用户注册
    path('register.html',register,name='register'),
    #用户登录
    path('login.html',userLogin,name='userLogin'),
    #博主资料信息页
    path('abo')
]
