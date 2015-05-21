"""
Django settings for Bares project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#            'NAME': 'baresdb',                      # Or path to database file if using sqlite3.
#            # The following settings are not used with sqlite3:
#            'USER': 'alexggp',
#            'PASSWORD': 'zjones90',
#            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for #localhost through TCP.
#            'PORT': '',                      # Set to empty string for default.
#        }
#    }
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm1e7qsm9q=fs&snsa7!lhtfh4b8_+_ow9d(3sn-%s!q9sc&nle'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'MisBares'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Bares.urls'

WSGI_APPLICATION = 'Bares.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_URL = '/static/'
MEDIA_ROOT = 'uploads/'
MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'MisBares/static'),
)

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES={}
DATABASES['default'] =  dj_database_url.config(default='postgres://alexggp:zjones90@localhost/baresdb')

#DATABASES['default'] =  dj_database_url.config()
# Enable Connection Pooling
#DATABASES['default']['ENGINE'] = 'django_postgrespool'
#DATABASES['default']['NAME'] = 'baresdb'
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



#for python social auth
TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth'
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2'
)
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY='102669346737155'
SOCIAL_AUTH_FACEBOOK_SECRET='048996d6463831cd1ddfca915d0dd0b4'



SOCIAL_AUTH_PIPELINE = (
    # recibe via backend y uid las instancias de social_user y user
    'social.pipeline.social_auth.social_details',

    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',

    # Recibe segun user.email la instancia del usuario y lo reemplaza con uno que recibio anteriormente
    'social.pipeline.social_auth.social_user',

    # Trata de crear un username valido segun los datos que recibe
    'social.pipeline.user.get_username',

    # Crea un usuario nuevo si uno todavia no existe
    'social.pipeline.user.create_user',
    
    #Coge la foto de perfil
    #'MisBares.mis_pipelines.save_profile',

    # Trata de conectar las cuentas
    'social.pipeline.social_auth.associate_user',

    # Recibe y actualiza social_user.extra_data
    'social.pipeline.social_auth.load_extra_data',

    # Actualiza los campos de la instancia user con la informacion que obtiene via backend
    'social.pipeline.user.user_details',

)