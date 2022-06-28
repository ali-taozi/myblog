from django.contrib import admin
from .models import *

admin.site.site_title='博客管理后台'
admin.site.site_header='博客管理'

@admin.register(ArticleTag)
class ArticalTagAdmin(admin.ModelAdmin):
    list_display=['id','tag','user']
    #g'ne
