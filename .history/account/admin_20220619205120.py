from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display=[
        'username','email','name','introduce',
        'company','profession','address','telephone',
        'wx','qq','wb','photo'
    ]
    #在修改页面添加'mobile','qq','weChat'的信息输入框
    #将源码的useradmin.fields转换成列表格式
    fieldsets=list(UserAdmin.)