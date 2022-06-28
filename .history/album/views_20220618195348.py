from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from .models import AlbumInfo

# Create your views here.
def album(request,id,page):
    albumList=AlbumInfo.objects.filter(user_id=id)
    paginator=Paginator(albumList,8)
    try:
        pageInfo=paginator.page(page)
    except PageNotAnInteger:
        #如果参数page的数据类型不是整型，就返回第一页数据
        pageInfo=paginator.page(1)
    except EmptyPage:
        #若用户的访问页数大于总页数，就返回最后一页s
