import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DEBUG = True
ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ["10.10.6.80", "localhost"]
CSRF_TRUSTED_ORIGINS = ["http://10.10.6.80"]
SECRET_KEY = "django-insecure-i&65u#&3j4!b9(&0a=tipq6w*7y@*kdpyj_ts+2$pgb1m(*-(-"

# Application definition

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
]

SELF_APPS = ["query_engine"]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + SELF_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "noncodex_backend.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "noncodex_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "database" / "db.sqlite3",
        "OPTIONS": {
            "timeout": 20,
            "init_command": "\n".join(
                [
                    "PRAGMA cache_size=-1000000;",
                    "PRAGMA synchronous=OFF;",
                    "PRAGMA journal_mode=WAL;",
                    "PRAGMA temp_store=MEMORY;",
                ]
            ),
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


USE_TZ = True
USE_I18N = True
STATIC_URL = "static/"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files (CSS, JavaScript, Images)
STATIC_URL = f"{os.getenv('BASE_URL')}static/"
STATIC_ROOT = BASE_DIR / "static"

# Media files (CSS, JavaScript, Images)
MEDIA_ROOT = BASE_DIR / "datalake"
MEDIA_URL = f"{os.getenv('BASE_URL')}media/"
