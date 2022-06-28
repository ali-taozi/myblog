from django.db import models
from django.utils import timezone
from account.models import MyUser
# Create your models here.

#文章管理模型
#分类标签
class ArticleTag(models.Model):
    id=models.AutoField(primary_key=True)
    tag=models.CharField('标签', max_length=500)
    user=models.models.ForeignKey(MyUser, verbose_name='用户', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='博文分类'
        verbose_name_plural='博文分类'

#文章正文内容
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

#评论信息
class Comment(models.Model):
    article=models.ForeignKey(ArticleInfo, verbose_name='suo'shu', on_delete=models.CASCADE)