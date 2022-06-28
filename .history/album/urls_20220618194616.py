from django.urls import path
from .models import 
urlpatterns = [
    path('<int:id>/<int:page>.html',album,name='album')
]
