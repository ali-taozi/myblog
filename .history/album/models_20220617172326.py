from django.db import models
from account.models import MyUser
#图片墙
class AlbumInfo(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.models.ForeignKey(MyUser, verbose_name='用户', on_delete=models.CASCADE)
    title=models.CharField('标题', max_length=50,blank=True)
    introduce=models.CharField('描述',max_length=200,blank=True)
    photo=models.ImageField('图片', upload_to='images/album', blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='图片墙管理'
        verbose_name_plural='图片墙管理'
