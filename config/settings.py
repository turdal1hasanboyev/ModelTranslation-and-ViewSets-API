from pathlib import Path
# for translation gettext lazy
from django.utils.translation import gettext_lazy as _
import os # for model translation

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-h$#%fm_y784alt5)7q2tsn-8e)1ibm96fr8zh!lp68j$tohq=!'

DEBUG = False

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'app.User'

INSTALLED_APPS = [
    'modeltranslation', # model translation

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # build-in apps
    'rest_framework',

    # local apps
    'app',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware', # model translation

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [BASE_DIR / 'templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True # language

USE_TZ = True

# language

#defaul language
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

# languages tillar
LANGUAGES = (
    ('uz', _('Uzbek')),
    ('en', _('English')),
    ('ru', _('Russian')),
)

# local path ochish
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    # BASE_DIR / 'locale',
)

#tarjima qilinadigan tillar
MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')

# tillar va kodi default holatda qaysi turishi
PARLER_LANGUAGES = {
    None: (
        {'code': 'uz', },  # Uzbek
        {'code': 'ru', },  # Russian
        {'code': 'en', },  # English
    ),
    'default': {
        'fallbacks': ['uz'],
        'hide_untranslated': False,
    }
}

# translation fayllar
MODELTRANSLATION_TRANSLATION_FILES = (
    'app.translations',
)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'