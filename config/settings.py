import os
from pathlib import Path
from config.custom_config import UNFOLD,setup_logging
# ======================================= BASE SETTINGS =======================================
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1

SECRET_KEY = 'django-insecure-%cq-(md-*c872)6y31u!!k_ry6rp!+4a_ptd(l!5$rf)@n!k&+'

DEBUG = True

LOGGING_STATUS =True

ALLOWED_HOSTS = ['*']

DB = True  #True bo'lsa  PostgreSql False bo'lsa  Sqlite ni o'zlashtiradi

UNFOLD = UNFOLD


# ======================================= INSTALLED APPS =======================================
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


THIRD_PARTY_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    # 'ckeditor',
    # 'ckeditor_uploader',
]

CUSTOM_APPS = [
    'main',
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + CUSTOM_APPS

# ======================================= MIDDLEWARE =======================================
CORS_ALLOW_ALL_ORIGINS = True

DJANGO_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE = DJANGO_MIDDLEWARE

# ======================================= URLS & WSGI =======================================
ROOT_URLCONF = 'config.urls'

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
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ======================================= DATABASE =======================================
import os 


if DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'palermo',
            'USER': 'palermouser',
            'PASSWORD': 'palermo1',
            # 'HOST': 'localhost' if not DEBUG else os.getenv("DB_HOST"),
            # 'HOST': '167.99.126.7',
            'HOST': 'localhost',
            # 'HOST': '46.101.127.46',



            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',  # SQLite uchun fayl manzili
        }
    }






# ======================================= AUTHENTICATION =======================================
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

# ======================================= INTERNATIONALIZATION =======================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True




# ======================================= STATIC & MEDIA =======================================



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # To'g'ri yo'l

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Bu to'g'ri

# ======================================= DEFAULT SETTINGS =======================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




if LOGGING_STATUS:
    setup_logging() 
    