"""
Django settings for aidants_connect project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

HOST = os.environ["HOST"]
# FC as FI
FC_AS_FI_CALLBACK_URL = os.environ["FC_AS_FI_CALLBACK_URL"]
FC_AS_FI_ID = os.environ["FC_AS_FI_ID"]
FC_AS_FI_SECRET = os.environ["FC_AS_FI_SECRET"]

# FC as FS
FC_AS_FS_BASE_URL = os.environ["FC_AS_FS_BASE_URL"]
FC_AS_FS_ID = os.environ["FC_AS_FS_ID"]
FC_AS_FS_SECRET = os.environ["FC_AS_FS_SECRET"]
FC_AS_FS_CALLBACK_URL = os.environ["FC_AS_FS_CALLBACK_URL"]

if os.environ.get("FC_AS_FS_TEST_PORT"):
    FC_AS_FS_TEST_PORT = int(os.environ["FC_AS_FS_TEST_PORT"])
else:
    FC_AS_FS_TEST_PORT = 0


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("APP_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("DEBUG") == "True":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [os.environ["HOST"]]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "aidants_connect_web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "aidants_connect.urls"

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
            ]
        },
    }
]

WSGI_APPLICATION = "aidants_connect.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_URL"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}

ssl_option = os.getenv("DATABASE_SSL")
if ssl_option:
    DATABASES["default"]["OPTIONS"] = {"sslmode": ssl_option}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"


LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "home_page"

AUTH_USER_MODEL = "aidants_connect_web.User"



DEMARCHES = [
    ("papiers", {
        "nom_machine": "PAPIERS",
        "titre": "PAPIERS - CITOYENNETÉ",
        "description": "État-civil, Passeport, Élections, Papiers à conserver, Carte d'identité…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png/papiers.png",
        }
     ),
    ("famille", {
        "nom machine" : "FAMILLE",
        "titre" : "FAMILLE",
        "description": "Allocations familiales, Naissance, Mariage, Pacs, Scolarité…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/famille.png",
        },
    ),
    ("social", {
        "nom machine" : "SOCIAL",
        "titre" : "SOCIAL - SANTÉ",
        "description": "Carte vitale, Chômage, Handicap, RSA, Personnes âgées…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/sante.png",
        },
    ),
    ("travail", {
        "nom machine" : "TRAVAIL",
        "titre" : "TRAVAIL",
        "description": "CDD, Concours, Retraite, Démission, Période d'essai…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/travail.png",
        },
    ),
    ("logement", {
        "nom machine" : "LOGEMENT",
        "titre" : "LOGEMENT",
        "description": "Allocations logement, Permis de construire, Logement social, Fin de bail…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/logement.png",
        },
    ),
    ("transport", {
        "nom machine" : "TRANSPORTS",
        "titre" : "TRANSPORTS",
        "description": "Carte grise, Permis de conduire, Contrôle technique, Infractions…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/transports.png",
        },
    ),
    ("argent", {
        "nom machine" : "ARGENT",
        "titre" : "ARGENT",
        "description": "Crédit immobilier, Impôts, Consommation, Livret A, Assurance, "
               "Surendettement…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/argent.png",

    }),
    ("justice", {
        "nom machine" : "JUSTICE",
        "titre" : "JUSTICE",
        "description": "Casier judiciaire, Plainte, Aide juridictionnelle, Saisie…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/justice.png",

    }),
    ("etranger", {
        "nom machine" : "ÉTRANGER",
        "titre" : "ÉTRANGER",
        "description": "Titres de séjour, Attestation d’accueil, Regroupement familial…",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/etrangers.png",

    }),
    ("loisirs", {
        "nom machine" : "LOISIRS",
        "titre" : "LOISIRS",
        "description": "Animaux, Permis bateau, Tourisme, Permis de chasser,",
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
                "/loisirs.png",
    })


]
