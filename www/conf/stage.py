from conf.default import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_code }}_stage',
        'USER': '{{ project_code}}_app',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

EMAIL_SUBJECT_PREFIX = '[{{ project_code }}][Stage] '

LOGGING = create_logging_dict(location('../../logs/stage'))

ALLOWED_HOSTS = ['{{ client }}-{{ project_code }}-stage.tangentlabs.co.uk']

# Create a new project on Sentry to get the DSN value to put here.
RAVEN_CONFIG['dsn'] = ''
