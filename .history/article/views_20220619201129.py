from django.shortcuts import render,redirect

#分页功能
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from account.models import MyUser
from album.models import AlbumInfo
from .models import ArticalInfo,ArticalTag
from d
# Create your views here.
