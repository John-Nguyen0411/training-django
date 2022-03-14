"""
Django settings for training project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import environ
from datetime import timedelta
from .logging import LOGGING
from .swagger import SWAGGER_SETTINGS  # noqa

env = environ.Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = environ.Path(__file__) - 3

BASE_URL = env("BASE_URL", default="http://localhost")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    
    'rest_framework',
    "rest_framework.authtoken",
    "oauth2_provider",
    "rest_auth",
    
    'storages',
    'corsheaders',
    'djangoql',
    'post_office',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    
    'rest_framework_swagger',
    'drf_yasg',
    'django_filters',
    
    "django_celery_beat",
    "django_celery_results",
]

PROJECT_APPS = [
    'usermodel',
    'core',
    'product',
    'cart'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'config.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'user_auth.authentication.CustomJWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static', 
            }
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# User Model Definition
AUTH_USER_MODEL = 'usermodel.User'

AUTHENTICATION_BACKENDS = [
     'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('RDS_DB_NAME', 'training'),
        'USER': os.environ.get('RDS_USERNAME', 'training'),
        'PASSWORD': os.environ.get('RDS_PASSWORD', '123321'),
        'HOST': os.environ.get('RDS_HOSTNAME', '127.0.0.1'),
        'PORT': os.environ.get('RDS_POST', '5432'),
    },
}
#Site matching query does not exist
SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD_EMAIL = "email"
ACCOUNT_AUTHENTICATION_METHOD_USERNAME = "username"
ACCOUNT_EMAIL_VERIFICATION_MANDATORY = "mandatory"

#celery -A core worker -P eventlet -c 10
#celery -A core beat
#  Celery
BROKER_URL = env("CELERY_BROKER_URL", default="django://")
CELERYD_MAX_TASKS_PER_CHILD = 100
CELERYD_TASK_SOFT_TIME_LIMIT = 2400  # 40 minutes
CELERY_RESULT_BACKEND = "django-db"
CELERY_IGNORE_RESULT = False


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Admin URL Definition
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/')

# Redis Settings
REDIS_URL = env('REDIS_URL', default=None)

if REDIS_URL:
    CACHES = {
        "default": env.cache('REDIS_URL')
    }
    
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {  # 'catch all' loggers by referencing it with the empty string
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}


AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default=None)
if AWS_STORAGE_BUCKET_NAME:
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN', default=None) or f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=600'}

    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'tutorial.storages.StaticStorage'

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'tutorial.storages.PublicMediaStorage'
else:
    MIDDLEWARE.insert(2, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
    WHITENOISE_USE_FINDERS = True
    STATIC_HOST = env('DJANGO_STATIC_HOST', default='')
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = STATIC_HOST + '/static/'
    if DEBUG:
        WHITENOISE_AUTOREFRESH = True
        
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='test@example.com')


# AllAuth Settings
AUTHENTICATION_BACKENDS += [
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'usermodel.forms.MyCustomSignupForm'}
ACCOUNT_MAX_EMAIL_ADDRESSES = 2
SOCIALACCOUNT_PROVIDERS = {

}
SOCIALACCOUNT_PROVIDERS_GOOGLE_CLIENT_ID = env('SOCIALACCOUNT_PROVIDERS_GOOGLE_CLIENT_ID', default=None)
if SOCIALACCOUNT_PROVIDERS_GOOGLE_CLIENT_ID:
    SOCIALACCOUNT_PROVIDERS['google'] = {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': SOCIALACCOUNT_PROVIDERS_GOOGLE_CLIENT_ID,
            'secret': env('SOCIALACCOUNT_PROVIDERS_GOOGLE_SECRET'),
        }
    }

# Crispy Forms Settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django Post Office Settings
EMAIL_BACKEND = 'post_office.EmailBackend'

POST_OFFICE = {
    'BACKENDS': {
        'default': 'django_ses.SESBackend',
    },
    'DEFAULT_PRIORITY': 'now',
}

# AWS SES Settings
AWS_SES_REGION_NAME = env('AWS_SES_REGION_NAME', default='us-east-1')
AWS_SES_REGION_ENDPOINT = env('AWS_SES_REGION_ENDPOINT', default='email.us-east-1.amazonaws.com')
AWS_SES_CONFIGURATION_SET = env('AWS_SES_CONFIGURATION_SET', default=None)


EXPIRED_TOKEN_MINUTES = env.int("EXPIRED_TOKEN_MINUTES", default=100)
EXPIRED_REFRESH_DAYS = env.int("EXPIRED_REFRESH_DAYS", default=30)


# JWT PUBLIC/PRIVATE KEY PATH
JWT_PUBLIC_KEY_PATH = env.str("JWT_PUBLIC_KEY_PATH", default="jwt_api_key.pub")
JWT_PRIVATE_KEY_PATH = env.str("JWT_PRIVATE_KEY_PATH", default="jwt_api_key")

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=EXPIRED_TOKEN_MINUTES),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=EXPIRED_REFRESH_DAYS),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "RS256",
    "SIGNING_KEY": open(JWT_PRIVATE_KEY_PATH).read(),
    "VERIFYING_KEY": open(JWT_PUBLIC_KEY_PATH).read(),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

