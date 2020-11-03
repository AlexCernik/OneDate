from decouple import config

POSTGRES_LOCAL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('API'),
        'USER':config('PRIVATE_USER'),
        'PASSWORD':config('PRIVATE_PASSWORD'),
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# NAME yoydev
# PASSWORD api_rest1234
POSTGRES_PRODUCTION = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '5432',
    }
}