from django.shortcuts import render,redirect
#导入分页相关功能
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
#导入文章标签等模型
from article.models import ArticalTag
from account.models import MyUser
from album.models import AlbumInfo
from .models import Board
from django.urls import reverse

# Create your views here.
def board(request,id,page):
    album=AlbumInfo.objects.filter(user_id=id)
    tag=ArticalTag.objects.filter(user_id=id)
    user=MyUser.objects.filter(id=id).first()
    if not user:
        return redirect(reverse('register'))
    if request.method='GET':
        boardList=Board.objects.filter(user_id=id).order_by('-created')
        paginator=Paginator(boardList,10)
        try:
            pageInfo=paginator.page(page)
        except PageNotAnInteger:
            #如果参数page的数据类型不是整型，就返回第一页数据
            pageInfo=paginator.page(1)
        except EmptyPage:
            #若用户的访问页数大于总页数，就返回最后一页数据
            pageInfo=paginator.page(paginator.num_pages)    
        return render(request,'board.html',locals())
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('')
