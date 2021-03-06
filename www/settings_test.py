from settings import *

# Configure Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['-s']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True

# Use syncdb rather than applying migrations
SOUTH_TESTS_MIGRATE = False

# Disable logging
import logging
logging.disable(logging.CRITICAL)
