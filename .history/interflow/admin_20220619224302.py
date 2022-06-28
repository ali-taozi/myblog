from django.contrib import admin

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['article','commentator','content','created']
    #根据当前用户名设置数据访问权限
    def get_queryset(self,request):
        qs=super().get_queryset(request)
        return qs.filter(article_author_id=request.user.id)
    #新增或修改数据时，设置外键可选值
    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name='article':
            id=request.user.id
            kwargs['queryset']=Comment.objects.filter(article_author_id=id)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)