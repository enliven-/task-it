# Django settings for Userena demo project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'private/development.db'),
    }
}

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}


# Internationalization
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('nl', ugettext('Dutch')),
    ('fr', ugettext('French')),
    ('pl', ugettext('Polish')),
    ('pt', ugettext('Portugese')),
    ('pt-br', ugettext('Brazilian Portuguese')),
    ('es', ugettext('Spanish')),
)

# LOCALE_PATHS = (
#     os.path.join(PROJECT_ROOT, 'locale'),
# )

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public/media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public/static/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'collegecircles/static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_g-js)o8z#8=9pr1&amp;05h^1_#)91sbo-)g^(*=-+epxmt4kc9m#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    # "django_sorting.middleware.SortingMiddleware",
    
)

# Add the Guardian and userena authentication backends
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Settings used by Userena
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
AUTH_PROFILE_MODULE = 'profiles.Profile'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140

ROOT_URLCONF = 'collegecircles.urls'
WSGI_APPLICATION = 'collegecircles.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'collegecircles/templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'guardian',
    'south',
    'userena',
    'uni_form',
    'pagination',
    'easy_thumbnails',
    'userena.contrib.umessages',
    'collegecircles.profiles',
    'collegecircles.tribes',
    'collegecircles.swaps',
    'tagging',
    # 'collegecircles.tagging_ext',
    'threadedcomments',
    # 'swaps',
    'avatar',
    # 'collegecircles.swaps',
    # 'collegecircles.groups',
    # 'collegecircles.tribes'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Needed for Django guardian
ANONYMOUS_USER_ID = -1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'taskit.backend@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'taskit.backend@gmail.com'
EMAIL_HOST_PASSWORD = 'taskitviksitsyal'
EMAIL_PORT = 587
EMAIL_USE_TLS = True