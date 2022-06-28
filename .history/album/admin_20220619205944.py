from django.contrib import admin
from .models import AlbumInfo
from account.models import MyUser
# Register your models here.

@admin.register(AlbumInfo)
class AlbumInfoAdmin(admin.ModelAdmin):
    list_display=['id','user','title']
