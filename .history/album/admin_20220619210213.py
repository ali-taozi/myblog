from django.contrib import admin
from .models import AlbumInfo
from account.models import MyUser
# Register your models here.

@admin.register(AlbumInfo)
class AlbumInfoAdmin(admin.ModelAdmin):
    list_display=['id','user','title','introduce','photo']
    #根据当前用户名设置数据访问权限
    def get_queryset(self,request):
        qs=super().get_queryset(request)
        return qs.filter(id=request.user.id)
    #新增或修改数据时，设置外键可选值
    def formfield_for_foreignkey(self,db_fields,request,**kwargs):
        if db_fields.name=='user'
