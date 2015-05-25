"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ba1usk_37)pz23b7)z+qatfmz6$kf#$_o9c#v2^3bllz2w7ne7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1',]

TEMPLATE_DIRS = (
     os.path.join(os.path.dirname(__file__),'templates'),
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'kerajinan',
    'bootstrap3',
    'registration',
    'pagination_bootstrap',
    'social.apps.django_app.default',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination_bootstrap.middleware.PaginationMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

SOCIAL_AUTH_TWITTER_KEY = 'Rlx3i6Iqzx7L9VZyPOxIXbe44'
SOCIAL_AUTH_TWITTER_SECRET = 'gtymQbHvZ1GRLavjsK3COvr3Pc0qz4H9MN6sTlhDvLTcdOWsgz'

SOCIAL_AUTH_FACEBOOK_KEY = '888287441209960'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b26e5eb52494b4fd23a2961a91f840fa'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kerajinan',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
    }
}

AUTH_USER_MODEL = 'kerajinan.UserProfile'

SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/')
MEDIA_URL  = '/static/images/'

ACCOUNT_ACTIVATION_DAYS = 3
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kusumaputra05@gmail.com'
EMAIL_HOST_PASSWORD = 'mei092013'
# EMAIL_HOST_PASSWORD = 'hwpitnrtvgiugwpg'
EMAIL_PORT = 587
EMAIL_USE_TLS = 1

