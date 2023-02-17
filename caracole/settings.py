import os
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT = "caracole"
PROJECT_VERBOSE = PROJECT.capitalize()
WAGTAIL_SITE_NAME = PROJECT_VERBOSE

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"
if DEBUG:
    SECRET_KEY = "django-insecure-un&^-yd2(xdo#_@or@bozh)trtweg))^oegpor8@=$srjplaz1"
else:
    SECRET_KEY = os.environ["SECRET_KEY"]

DOMAIN_NAME = os.environ.get("DOMAIN_NAME", "io")
HOSTNAME = os.environ.get("ALLOWED_HOST", f"{PROJECT}.{DOMAIN_NAME}")
ALLOWED_HOSTS = [HOSTNAME, f"{HOSTNAME}:8000"]
ALLOWED_HOSTS += [f"www.{host}" for host in ALLOWED_HOSTS]
CSRF_TRUSTED_ORIGINS = [
    "http://" if DEBUG else "https://" + host for host in ALLOWED_HOSTS
]


INSTALLED_APPS = [
    PROJECT,
    "ndh",
    "django.contrib.admin",
    "registration",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django_bootstrap5",
    # "videgrenier",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.legacy.sitemiddleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = f"{PROJECT}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "ndh.context_processors.settings_constants",
                f"{PROJECT}.context_processors.wagtree",
            ],
        },
    },
]

WSGI_APPLICATION = f"{PROJECT}.wsgi.application"

DB = os.environ.get("DB", "db.sqlite3")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / DB,
    }
}
if DB == "postgres":
    DATABASES["default"].update(
        ENGINE="django.db.backends.postgresql",
        NAME=os.environ.get("POSTGRES_DB", DB),
        USER=os.environ.get("POSTGRES_USER", DB),
        HOST=os.environ.get("POSTGRES_HOST", DB),
        PASSWORD=os.environ["POSTGRES_PASSWORD"],
    )

_APV = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": f"{_APV}.UserAttributeSimilarityValidator",
    },
    {
        "NAME": f"{_APV}.MinimumLengthValidator",
    },
    {
        "NAME": f"{_APV}.CommonPasswordValidator",
    },
    {
        "NAME": f"{_APV}.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", "fr-FR")
TIME_ZONE = os.environ.get("TIME_ZONE", "Europe/Paris")
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = int(os.environ.get("SITE_ID", 1))

MEDIA_ROOT = f"/srv/{PROJECT}/media/"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
STATIC_ROOT = f"/srv/{PROJECT}/static/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST = "mail.gandi.net"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", f"majo@{HOSTNAME}")
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
DEFAULT_FROM_EMAIL = f"{PROJECT_VERBOSE} <{EMAIL_HOST_USER}>"
SERVER_EMAIL = f"Server {DEFAULT_FROM_EMAIL}"
REPLY_TO = f"webmaster@{HOSTNAME}"
ADMINS = [(f"{PROJECT_VERBOSE} Webmasters", f"webmaster@{HOSTNAME}")]

if os.environ.get("MEMCACHED", "False").lower() == "true":
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
            "LOCATION": "memcached:11211",
        }
    }

if not DEBUG and os.environ.get("RAVEN", "False").lower() == "true":
    INSTALLED_APPS.append("raven.contrib.django.raven_compat")
    RAVEN_CONFIG = {"dsn": os.environ["DSN"]}

ACCOUNT_ACTIVATION_DAYS = 15
REGISTRATION_AUTO_LOGIN = True

DATES_VIDE_GRENIER = {
    "open": date(2019, 4, 18),
    "close": date(2019, 6, 19),
    "event": date(2019, 6, 23),
    "inscriptions": [
        date(2019, 5, 15),
        date(2019, 5, 22),
        date(2019, 5, 29),
        date(2019, 6, 5),
        date(2019, 6, 12),
        date(2019, 6, 19),
    ],
}

NDH_TEMPLATES_SETTINGS = [
    "DATES_VIDE_GRENIER",
]

AUTHENTICATION_BACKENDS = ["yeouia.backends.YummyEmailOrUsernameInsensitiveAuth"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

WAGTAILADMIN_BASE_URL = "https://caracole.io"
