from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    #首页地址自动跳转
    path('',RediRectView.as_view(url='user/login.html')),
    #
]
