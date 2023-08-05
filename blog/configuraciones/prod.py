from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carloslionel56$default',
        'USER': 'carloslionel56',
        'PASSWORD': 'estaEslaClave.498',  
        'HOST': 'carloslionel56.mysql.pythonanywhere-services.com',  
        'PORT': '3306',  
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'proyectblog827@gmail.com'
EMAIL_HOST_PASSWORD = 'nqhqivdafeyyxizl'   #4dmin1239


DEBUG = False

ALLOWED_HOSTS = ['carloslionel56.pythonanywhere.com']

# SOLO SE DEFINE CUANDO DEBUG = False
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
