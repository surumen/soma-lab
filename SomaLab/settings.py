"""
Django settings for SomaLab project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_FILE_DIR_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'projects')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_nd25#n8w*r6p780(7hq(s@$j%g)iib_hb_80ci@)!i9-8k^um'

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
    'django.contrib.sites',
    'projects',
    'practice',
    'contests',
    'userprofile',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'sass_processor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'SomaLab.middleware.AuthRequiredMiddleware.AuthRequiredMiddleware'
]

ROOT_URLCONF = 'SomaLab.urls'

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

WSGI_APPLICATION = 'SomaLab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(STATIC_FILE_DIR_ROOT, 'static'),
]

# Adding the sass finder to locate the generated .css file
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]


LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"
SIGNUP_URL = "/accounts/signup/"

EXCLUDED_URL = [LOGIN_URL,LOGOUT_URL,SIGNUP_URL,"/admin/"]

ERROR_MESSAGE = "Something went wrong please try again"
CORECT_SUBMISSION_MESSAGE = "Correct"
INCORECT_SUBMISSION_MESSAGE = "Wrong Answer"


DEFAULT_POINTS = 100
API_KEY = "hackerrank|1768852-1838|9171dce1a42a9fc576f587160de2ccf6762a635e"  #your API-KEY here
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Django allauth config
AUTHENTICATION_BACKENDS = (
  
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION='none'

ACCOUNT_EMAIL_REQUIRED='True'

# gmail smtp settings to send emails
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'moses.susrumen@gmail.com'
EMAIL_HOST_PASSWORD = '@Moses2018'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGGING = { 
    'version': 1, 
    'disable_existing_loggers': False, 
    'handlers': { 
        'console': { 
            'class': 'logging.StreamHandler', 
        }, 
    }, 
    'loggers': { 
        'django': { 
            'handlers': ['console'], 
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'), 
        }, 
    }, 
} 
