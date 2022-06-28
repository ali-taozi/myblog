from django.shortcuts import render,redirect
#导入分页相关功能
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
#导入文章标签等模型
from article.models import ArticalTag
from account.models import MyUser
from album.models import AlbumI

# Create your views here.
