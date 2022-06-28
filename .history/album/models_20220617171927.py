from django.db import models
from account.models import MyUser

class AlbumInfo(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.models.ForeignKey(MyUser, verbose_name='用户', on_delete=models.CASCADE)
    title=models.CharField('标题', max_length=50,blank)