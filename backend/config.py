import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://myuser:mypassword@localhost/cognitive_activities')

DEBUG = True
