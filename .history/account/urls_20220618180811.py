from django.urls import path
urlpatterns = [
    #用户注册
    path('register.html',register,name='register'),
    #用户登录
    path('login.html',userLogin,name='userLogin')
]
