"""
Django settings for dwarkeshevents project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Try to import cloudinary - handle gracefully if not available during build
try:
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api
    CLOUDINARY_AVAILABLE = True
except ImportError:
    print("Warning: Cloudinary not available during build")
    CLOUDINARY_AVAILABLE = False


load_dotenv()  # Load environment variables from .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-v864642e6ttk78e%nr69e-owm)*5_t3w3s2!#+gw!@_yrvig$h')

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
# Read DEBUG from environment or default to True for local development
DEBUG = os.getenv('DEBUG', 'True') == 'True'  # Correctly handles both string and boolean values

# Use appropriate ALLOWED_HOSTS based on DEBUG mode
if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
else:
    ALLOWED_HOSTS = ['dwarkesh-events.onrender.com', '.onrender.com']  # Render.com domains


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'gallery',  # Your custom app for managing events
    'contact',  # Your custom app for handling contact forms
]

# Add cloudinary apps only if available
if CLOUDINARY_AVAILABLE:
    INSTALLED_APPS += [
        'cloudinary',
        'cloudinary_storage',
        'storages',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # For serving static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dwarkeshevents.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # Adjust this path as needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dwarkeshevents.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Use PostgreSQL for production, SQLite for development
if os.getenv('DATABASE_URL'):
    # Production database (PostgreSQL)
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Development database (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'


# WhiteNoise configuration for Django 5.2+
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Media Files (for Cloudinary)
MEDIA_URL = '/media/'

# Cloudinary Configuration - only if available
if CLOUDINARY_AVAILABLE:
    # Cloudinary settings for django-cloudinary-storage
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', 'dqkgzzmkr'),
        'API_KEY': os.getenv('CLOUDINARY_API_KEY', '762694757195965'),
        'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', 'scbWa9j0BuvZsU2SEOTBYQIfpBo'),
    }
    
    # Basic cloudinary config (for API usage)
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME', 'dqkgzzmkr'),
        api_key=os.getenv('CLOUDINARY_API_KEY', '762694757195965'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET', 'scbWa9j0BuvZsU2SEOTBYQIfpBo'),
        secure=True
    )
else:
    # Fallback to filesystem storage during build
    print("Using filesystem storage (Cloudinary not available)")

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'dwarkesh.events.management@gmail.com')  # Default for Render
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'vdwkhjhryrtlmitk')  # Default for Render  
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'dwarkesh.events.management@gmail.com')  # Default for Render

# ======================================
# Iframe Embedding Configuration
# ======================================

# Allow iframe embedding from any website
X_FRAME_OPTIONS = 'ALLOWALL'

# Alternative method: Remove X-Frame-Options header entirely
# Comment out the line above and uncomment the lines below if needed
# SECURE_FRAME_DENY = False
# X_FRAME_OPTIONS = None

# Content Security Policy for iframe embedding
# This allows your site to be embedded in iframes from any origin
CSP_FRAME_ANCESTORS = ["'*'"]

# Additional security headers for iframe embedding
SECURE_CONTENT_TYPE_NOSNIFF = False  # Allow content type sniffing for better iframe compatibility