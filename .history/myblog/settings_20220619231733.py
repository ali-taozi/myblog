"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s10e1+ou625cl!stxr)48#!ff0#q^bz1s7$z5q(fs$!(w&ibv5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'myblog.myapps.MyAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #账户管理（注册，登录，用户资料信息页）（自定义模型MyUser在User的基础上添加新字段）
    'account',
    #相册（模型AlbumInfo用于存储图片墙的图片信息，外键字段关联MyUser）
    'album',
    #文章管理（每篇文章设有分类标签（模型ArticleTag，外键字段关联MyUser），正文内容（模型ArticleInfo，与MyUser一对多，与ArticleTag多对多），评论信息（模型Comment，与ArticleInfo一对多）
    'article',
    #留言板功能（模型Board，外键关联MyUser一对多）
    'interflow',
    'ckeditor',
    'ckeditor_uploader',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 添加中间件LocaleMiddleWare，使内置支持中文
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    #'''
    #jinja2模板
    #{
    #    'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # 此处添加模板文件夹
    #    'DIRS': [
    #        BASE_DIR / 'templates',
            #BASE_DIR / 'index/templates'
    #    ],
    #    'APP_DIRS': True,  # 是否在app里查找模板文件
    #    'OPTIONS': {  # 用在填充RequestContext的上下文(模板里的变量和命令),一般无需修改
    #        'environment': 'messageBoard.jinja2.environment'
    #    },
    #},
    #'''
    #默认模板
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {'read_default_file': str(BASE_DIR / 'my.cnf')},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# 资源集合文件夹，解决上述不便之处,若设置，则上述STATIC_URL的值为通用路径名
#STATIC_ROOT=BASE_DIR / 'static'
STATICFILES_DIRS = [
    # 设置根目录资源文件夹
    #存放css，js，网页图片等静态资源
    BASE_DIR / 'publicStatic',
    # 设置app资源文件夹、
    #BASE_DIR / 'index/static',
]

# 媒体资源Media,用来存放经常变动的资源文件(文章图片，图片墙图片，用户头像)
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#配置自定义用户模型
AUTH_USER_MODEL='account.MyUser'

#django ckeditor编辑器的配置信息
CKEDITOR_UPLOAD_PATH='article_images'
CKEDITOR_CONFIGS={
    'default':{
        'toolbar':'Full'
    }
}
CKEDITOR_ALLOW_NONIMAGE_FI