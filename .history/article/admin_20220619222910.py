from django.contrib import admin
from .models import *

admin.site.site_title='博客管理后台'
admin.site.site_header='博客管理'

@admin.register(ArticleTag)
class ArticalTagAdmin(admin.ModelAdmin):
    list_display=['id','tag','user']
    #根据当前用户名设置数据访问权限
    def get_queryset(self,request):
        qs=super().get_queryset()
