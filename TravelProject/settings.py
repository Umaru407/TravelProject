"""
Django settings for TravelProject project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '-c1cg^-j%2l-e_-(0+ey030&yvz@^k$x@%w0pwgm#of%)qrqe+'

SECRET_KEY = os.environ.get('SECRET_KEY', default='-c1cg^-j%2l-e_-(0+ey030&yvz@^k$x@%w0pwgm#of%)qrqe+')


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ["*"]


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
    'corsheaders',
    'TravelProject',
    'storages',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TravelProject.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['frontend/build'],
        'DIRS': [],
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
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
}


WSGI_APPLICATION = 'TravelProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 't2',
#         'USER': 'root',
#         'PASSWORD': 'apple910407',
#         'HOST': 'localhost',
#         'PORT': 3306,
#         'OPTIONS':{'charset':'utf8mb4'}
        
#     }
# } 


DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgres://aitraveldb_user:tR1MRoPzJ95qpqEqp0lUs5FJbf9MmQFL@dpg-clasr3ug1b2c73a826lg-a.singapore-postgres.render.com/aitraveldb',
        # default='postgres://aitraveldb_user:tR1MRoPzJ95qpqEqp0lUs5FJbf9MmQFL@dpg-clasr3ug1b2c73a826lg-a/aitraveldb',
        conn_max_age=600
    )
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'railway',
#         'USER': 'root',
#         'PASSWORD': 'Ha0aIJNVhR0IkHlHoVSe',
#         'HOST': 'containers-us-west-200.railway.app',
#         'PORT': 7921,
        
        
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/






CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    
]

##STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# MEDIA_URL = "/api/media/"
# MEDIA_ROOT= os.path.join(BASE_DIR,"media/")
AUTH_USER_MODEL = 'api.Account'

# USE_S3 = os.getenv('USE_S3') == 'TRUE'
USE_S3 = False

if USE_S3:
    # aws settings
    # AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    # AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

    AWS_ACCESS_KEY_ID = 'AKIASHKK6YEOCTDNDDER'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'aitravel'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATIC_URL = '/frontend/build/'

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'frontend/static'),)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/build/static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')