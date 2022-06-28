from django.db import models
from account.models import MyUser
from django.utils import timezone
# Create your models here.

#留言板信息管理
class Board(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('留言用户', max_length=50)
    email=models.CharField('邮箱地址', max_length=50)
    content=models.CharField('留言内容',max_length=500)
    created=models.DateTimeField('创建时间', default=timezone.now)
    user=models.models.ForeignKey(MyUser, verbose_name='用户', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='博文管理'
        verbose_name_plural='博文管理'