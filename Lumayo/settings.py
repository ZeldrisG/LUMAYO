"""
Django settings for Lumayo project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')x7&gvjgrejwcrcwbr8&6+as7=3md_lvgu*lg!)5b1^@)s4(k#'

# SECURITY WARNING: don't run with debug turned on in production!...
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'whitenoise.runserver_nostatic',
    'widget_tweaks',
    'LumayoApp',
    'usuarios',
    'libros',
    'carrito',
    'reserva',
    'ordenes',
    'envios',
    'metodos_pago',
    'foro',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Lumayo.urls'

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

WSGI_APPLICATION = 'Lumayo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dtnlu4i3mje63',
        'USER': 'fajfwtiwrggxwg',
        'PASSWORD': '2c9103807a28a398b0e2d7b74e56f78635416f3ff16de716897df0c02b36ad3e',
        'HOST': 'ec2-54-235-108-217.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# import dj_database_url

# db_from_env = dj_database_url.config(default='postgres://fajfwtiwrggxwg:2c9103807a28a398b0e2d7b74e56f78635416f3ff16de716897df0c02b36ad3e@ec2-54-235-108-217.compute-1.amazonaws.com:5432/dtnlu4i3mje63')
# DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

AUTH_USER_MODEL = 'usuarios.Usuario'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

LOGIN_REDIRECT_URL = 'usuarios:usuarios'

LOGOUT_REDIRECT_URL = 'usuarios:login'

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

ADMINS = [
    ('luba', 'l.narvaez@utp.edu.co'),
    ('mao', 'mauroalternativo519@gmail.com')
]

import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

# Configuracion SMTP

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lumayoapp@gmail.com'
EMAIL_HOST_PASSWORD = 'lumayo2021'

STRIPE_PUBLIC_KEY ='pk_test_51J7pTSI8EiHjhXXU7pOz6QKFgJ7coDDnGkwVwu88I7dZPC4VtKKcKmx1SFlX2dlPGQrbeDGtibNeQMVC5AveJtaY007xQ5npE4'
STRIPE_PRIVATE_KEY = 'sk_test_51J7pTSI8EiHjhXXUV7bEYoIh3VbakfDrEFaNqRuBIYhnPp8CK1a3wq3ZRYip64LMo1fp3rPhi73DTGHCWcjr2GR200nIrtjAB1'

DATE_INPUT_FORMATS = ['%Y-%m-%d']
