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
    #在修改页面添加'mobile','qq'