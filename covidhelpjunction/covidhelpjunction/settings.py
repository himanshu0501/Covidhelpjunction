"""
Django settings for covidhelpjunction project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$=oa46)-s2lxj89*@v0q0xbh3p(j0ej9)4g8#ms3ihiz92&aen'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'donationbox',
    'user_profile.apps.UserProfileConfig',
    'crispy_forms',
    'oxygenrefill',    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'covidhelpjunction.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'covidhelpjunction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project3',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'Himns0501#',
    }
}


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


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'  # its telling to use the bootstrap 

MEDIA_ROOT = os.path.join(BASE_DIR,'media/') # here we are using the os module to specify that the path should be created independent of the os and that path should be inside the BASE_DIR with folder name media
MEDIA_URL = '/media/'  

LOGIN_REDIRECT_URL='home'  # /account/profile this is the bydefault link that django search for as the user login so that django can try it to navigate him to the profile page 
# so here LOGIN_REDIRECT_URL  is trying to divert that navigation to the home page of our blog hence set this URL to home 

LOGIN_URL = 'login'  # as the user try to access the profile page so there we have given a decorator which says that after only login you can see the profile page so django check the profile at
# /account/login so to change that url instead of profile we have divert that url to login page first and as the user will then directly instead of going to the home page it will go to the profile page whose navigation we have given in our view in donationbox app.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #this module is created to send the mail to gmail the user to reset the password 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'himanshu18060501@gmail.com'
EMAIL_HOST_PASSWORD = 'himns0501@'      # here we are connecting the user to send the mail on this host user.
# after that we will get one error called password reset complete  for that we  will add one more route 



GOOGLE_API_KEY = ""