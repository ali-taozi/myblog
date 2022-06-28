from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from .models import AlbumInfo

# Create your views here.
def album(request,id,page):
    albumList=AlbumInfo.objects.filter(user_id=id)
    paginator=Paginator(albumList,8)
    
