import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Base settings
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-+qxo-$t-lyccc-(!mkcv+(#yts-%75sb(-nt4jr&0vmq_)jasp')

DEBUG = bool(int(os.getenv('DEBUG', False)))

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(' ')

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'debug_toolbar',

    'account',
    'blog',
]

if not DEBUG:
    CORS_ALLOWED_ORIGINS = [
        '192.168.149.243:5000',
        '127.0.0.1:5000',
    ]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'account.backends.CaseInsensitiveModelBackend',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('POSTGRES_ENGINE', 'django.db.backends.sqlite3'),
#         'NAME': os.getenv('POSTGRES_DB', os.path.join(BASE_DIR, 'db.sqlite3')),
#         'USER': os.getenv('POSTGRES_USER', 'user'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
#         'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
#         'PORT': os.getenv('POSTGRES_PORT', '5432'),
#     }
# }


# Password validation
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

AUTH_USER_MODEL = 'account.Account'


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static / Media
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Logging
LOG_PATH = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'log_file'],
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d %(module)s] %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'djangoblog.log'),
            'when': 'D',
            'formatter': 'verbose',
            'interval': 1,
            'delay': True,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'config': {
            'handlers': ['log_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
