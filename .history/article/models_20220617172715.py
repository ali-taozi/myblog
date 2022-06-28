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
        verbose_name='博文fen'lei'
    