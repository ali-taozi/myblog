from django.db import models
from account.models import MyUser

class AlbumInfo(models.Model):
    id=models.AutoField()