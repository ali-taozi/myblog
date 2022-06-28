#自定义Admin后台系统
from django.contrib.admin.apps import AdminConfig
#继承父类AdminConfig
#重新设置属性default_site的值，使它指向MyAdminSite类
class MyAdminConfig(AdminConfig):
    default_site='myblog.myadmin.MyAdminSite'
