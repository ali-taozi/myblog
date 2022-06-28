from django.shortcuts import render,redirect

#分页功能
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from account.models import MyUser
from album.models import AlbumInfo
from .models import ArticalInfo,ArticalTag
from django.urls import reverse
# Create your views here.

def article(request,id,page):
    album=AlbumInfo.objects.filter(user_id=id)
    tag=ArticalTag.objects.filter(user_id=id)
    user=MyUser.objects.filter(id=id).first()
    if not user:
        return redirect(reverse('register'))
    ats=ArticleInfo.objects.filter(author_id=id).order_by('-created')
    paginator=Paginator(ats,10)
    try:
        pageInfo=paginator.page(page)
    except PageNotAnInteger:
            #如果参数page的数据类型不是整型，就返回第一页数据
            pageInfo=paginator.page(1)
        except EmptyPage:
            #若用户的访问页数大于总页数，就返回最后一页数据
            pageInfo=paginator.page(paginator.num_pages)    
        return render(request,'board.html',locals())
