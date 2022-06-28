from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    name=models.CharField('姓名', max_length=50,default='匿名用户')
    introduce=models.TextField('')
    mobile=models.CharField('手机号码',max_length=11)
    qq=models.CharField('QQ号码',max_length=10)
    weChat=models.CharField('微信账号',max_length=50)
    #设置返回值
    def __str__(self):
        return self.username
    class Meta(AbstractUser.Meta):
        #自定义权限
        permissions=(('vip_myuser','Can vip user'),)
        