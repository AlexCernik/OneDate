from decouple import config
from . import db

DATABASES = db.POSTGRES_PRODUCTION

# Dropbox for image
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropboxStorage'
DROPBOX_OAUTH2_TOKEN = config('DROPBOX_TOKEN')
DROPBOX_CONSUMER_KEY = config('DROPBOX_KEY')
DROPBOX_CONSUMER_SECRET = config('DROPBOX_SECRET')