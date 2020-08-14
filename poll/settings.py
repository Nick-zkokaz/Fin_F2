"""
Django settings for poll project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '20tzx35j_w=0=a)w_p7mbdk$jgdd6qexo%pny3ng(q*z!r*g&^'
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '20tzx35j_w=0=a)w_p7mbdk$jgdd6qexo%pny3ng(q*z!r*g&^')
#SECRET_KEY = 'e#!xkhudyp^e4^ht0_tiwh7nn9n0oo8!%qftg2s8m5k%x6t1j&'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'e#!xkhudyp^e4^ht0_tiwh7nn9n0oo8!%qftg2s8m5k%x6t1j&')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', 'fin-f2-nickkokaz.herokuapp.com']


# Application definition

INSTALLED_APPS = [
	'questions',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'crispy_forms',
	'tinymce',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'poll.urls'

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

WSGI_APPLICATION = 'poll.wsgi.application'


# Database default
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.sqlite3',
# 		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# 	}
# }

#for deploy on heroku

# DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}

# for Docker-compose settings:

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'postgres',
       'USER': 'postgres',
       'HOST': 'db',
       'PORT': 5432,
   }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#TinyMCE widget configuration
TINYMCE_JS_URL = os.path.join(MEDIA_URL + "tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT + "tiny_mce")
TINYMCE_SPELLCHECKER = False
TINYMCE_PLUGINS = [
	'safari',
	'table',
	'advlink',
	'advimage',
	'iespell',
	'inlinepopups',
	'media',
	'searchreplace',
	'contextmenu',
	'paste',
	'wordcount'
]

TINYMCE_DEFAULT_CONFIG={
	'theme' : "advanced",
	'plugins' : ",".join(TINYMCE_PLUGINS), # django-cms
	'language' : 'ru',
	"theme_advanced_buttons1" : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect,|,spellchecker",
	"theme_advanced_buttons2" : "cut,copy,paste,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,image,cleanup,code,|,forecolor,backcolor,|,insertfile,insertimage",
	"theme_advanced_buttons3" : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
	'theme_advanced_toolbar_location' : "top",
	'theme_advanced_toolbar_align' : "left",
	'theme_advanced_statusbar_location' : "bottom",
	'theme_advanced_resizing' : True,
	'table_default_cellpadding': 2,
	'table_default_cellspacing': 2,
	'cleanup_on_startup' : False,
	'cleanup' : False,
	'paste_auto_cleanup_on_paste' : False,
	'paste_block_drop' : False,
	'paste_remove_spans' : False,
	'paste_strip_class_attributes' : False,
	'paste_retain_style_properties' : "",
	'forced_root_block' : False,
	'force_br_newlines' : False,
	'force_p_newlines' : False,
	'remove_linebreaks' : False,
	'convert_newlines_to_brs' : False,
	'inline_styles' : False,
	'relative_urls' : False,

	'formats' : {
		'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
		'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
		'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
		'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
		'strikethrough' : {'inline' : 'del'},
		'italic' : {'inline' : 'em'},
		'bold' : {'inline' : 'strong'},
		'underline' : {'inline' : 'u'}
	},
	'pagebreak_separator' : "",
	'template_external_list_url': 'lists/template_list.js',
	'external_link_list_url': 'lists/link_list.js',
	'external_image_list_url': 'lists/image_list.js',
	'media_external_list_url': 'lists/media_list.js',
}