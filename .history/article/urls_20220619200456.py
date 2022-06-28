from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('',RediRectView.as_view(url='user/login.html')),
    #
]
