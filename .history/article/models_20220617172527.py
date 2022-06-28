from django.db import models
from django.utils import timezone
from account.models import MyUser
# Create your models here.

#文章管理模型
#分类标签
class ArticleTag(models.Model):
    id