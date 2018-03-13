from os import environ
from os.path import abspath, dirname, join

PROJECT = 'caracole'
PROJECT_VERBOSE = PROJECT.capitalize()

DOMAIN_NAME = environ.get('DOMAIN_NAME', 'io')
ALLOWED_HOSTS = [environ.get('ALLOWED_HOST', f'{PROJECT}.{DOMAIN_NAME}')]
ALLOWED_HOSTS += [f'www.{host}' for host in ALLOWED_HOSTS]

BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = environ['SECRET_KEY']
DEBUG = environ.get('DEBUG', 'False').lower() == 'true'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = f'{PROJECT}.urls'

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

WSGI_APPLICATION = 'caracole.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DB = environ.get('DB', 'postgres')
DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, DB),
    }
}
if DB == 'postgres':
    DATABASES['default'].update(
        ENGINE='django.db.backends.postgresql',
        NAME=environ.get('POSTGRES_DB', DB),
        USER=environ.get('POSTGRES_USER', DB),
        HOST=environ.get('POSTGRES_HOST', DB),
        PASSWORD=environ['POSTGRES_PASSWORD'],
    )

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

LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

MEDIA_ROOT = '/srv/media/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/srv/static/'
