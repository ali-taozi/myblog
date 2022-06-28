from django.db import models
from account.models import MyUser
from django.utils import timezone
# Create your models here.
#留言板信息管理

class ArticleInfo(models.Model):
    author=models.ForeignKey(Myuser, verbose_name='用户', on_delete=models.CASCADE)
    title=models.CharField('标题', max_length=200)
    content=models.CharField('内容')
    articlephoto=models.ImageField('文章图片',blank=True,upload_to='images/article')
    reading=models.IntegerField('阅读量',default=0)
    liking=models.IntegerField('点赞量',default=0)
    created=models.DateTimeField('创建时间', default=timezone.now)
    updated=models.DateTimeField('更新时间', auto_now=True)
    article_tag=models.ManyToManyField(ArticleTag, blank=True,verbose_name='文章标签')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='博文管理'
        verbose_name_plural='博文管理'