from django.db import models
from account.models import MyUser

class AlbumInfo(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.models.ForeignKey("account.MyUser", verbose_name=_(""), on_delete=models.CASCADE)