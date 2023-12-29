"""
Django settings for proyecto_WAPIPTDAH project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
""" IMPORTACION DE SECRETOS """
SECRET_KEY = config('KEY')
NEW_SECRET_KEY = config('KEY_NEW')
NOMBRE_CLOUDINARY = config('NAME_CLOUDINARY')
LLAVE_CLOUDINARY = config('API_KEY_CLOUDINARY')
SECRETO_CLOUDINARY = config('API_SECRET_CLOUD')
LLAVE_POSTGRESQL = config('LLAVE_POSTGRESQL')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ACCESS CONTROL ALLOW ORIGIN
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'APPWapiptda',
    'EstudioyEntrenamiento',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt', # Token de JWT para inicio de sesión
    'corsheaders',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware', # NUEVO MIDDLEWARE SESSION TIMEOUT
    'corsheaders.middleware.CorsMiddleware', # CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_WAPIPTDAH.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'proyecto_WAPIPTDAH.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

""" CONFIGURACIÓN DE BASE DE DATOS POSTGRESQL """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'EG4EDbba*5*152Bb2BEgBBed4cFg4GB1',
        'HOST': 'roundhouse.proxy.rlwy.net',
        'PORT': '30298',  # Reemplaza con el puerto correcto si es necesario
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


""" CLOUDINARY: CONFIGURACIÓN PARA ALMACENAMIENTO DE ARCHIVOS """
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': NOMBRE_CLOUDINARY,
    'API_KEY': LLAVE_CLOUDINARY,
    'API_SECRET': SECRETO_CLOUDINARY,
    'SECURE': False,
    'EXCLUDE_DELETE_ORPHANED_MEDIA_PATHS': (),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'
#DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-ue'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


""" CONFIGURACIÓN DE SESSION MIDDLEWARE PARA MANEJO DE SESIONES """
SESSION_EXPIRE_SECONDS = 300  # 5 minutos
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
#SESSION_TIMEOUT_REDIRECT = '/'
#SESSION_EXPIRE_SECONDS = 2700  # 45 minutos

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'proyecto_WAPIPTDAH/static'),)
STATIC_ROOT = '/code/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


""" CONFIGURACIÓN DE REST FRAMEWORK PARA MANEJO DE DATOS """
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication', # JWT
    ],
}


""" CONFIGURACIÓN DE TOKEN JWT PARA SEGURIDAD DE ENTRADAS Y SALIDAS DE DATOS """
from datetime import timedelta
SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_RESET_TIME": timedelta(hours=0),
    "BLACKLIST_AFTER_ROTATION": True,
    "VALIDATE_TOKEN": True,
}


""" CONFIGURACIÓN DE LA CONECCIÓN DE CORREO ELECTRÓNICO  """
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
#EMAIL_PORT = 465 # No se especifica el puerto ssl para facilidad de entrega


# CONFIGURACIÓN PARA LOS CORS HEADERS DE ACCESO DEL FRONTEND
CORS_ALLOW_ALL_ORIGINS = False  # Cambiado a False para especificar los dominios permitidos
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOWED_ORIGINS = [
    "https://react-frontend-production-b574.up.railway.app",
    'https://serverapi-production-c8a1.up.railway.app'
    # Agrega más dominios permitidos aquí si es necesario
]

ALLOWED_HOSTS = [
    # Otros hosts permitidos...
    'serverapi-production-c8a1.up.railway.app',
]

# DOMINIO
# SITE_URL = "http://aprender-wapiptdah.com"
