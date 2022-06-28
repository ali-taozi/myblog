from django.apps import AppConfig
import os
#修改app在后台admin的显示名称
#default_app_config的值来自apps.py的类名
default_app_config='account.IndexConfig'
#获取当前app的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_))