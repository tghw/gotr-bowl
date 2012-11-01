import os

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
ADMIN_EMAILS = [
    # Put your admin emails here.
    'test@example.com',
]
SECRET_KEY = 'Use os.urandom(24) to generate a secret key.'
