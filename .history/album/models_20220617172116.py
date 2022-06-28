from django.db import models
from account.models import MyUser

class AlbumInfo(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.models.ForeignKey(MyUser, verbose_name='用户', on_delete=models.CASCADE)
    title=models.CharField('标题', max_length=50,blank=True)
    introduce=models.CharField('描述',max_length=200,blank=True)
    photo=models.ImageField('图片', upload_to='', height_field=None, width_field=None, max_length=None)