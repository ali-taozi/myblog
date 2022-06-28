from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    #首页地址自动跳转到用户登录页面
    path('',RediRectView.as_view(url='user/login.html')),
    #文章列表
    path('<int:id>/<int:page>.html',article,name='article'),
    path('detail')
]

