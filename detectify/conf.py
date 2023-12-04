from decouple import config

APP_ADDRESS = config('APP_ADDRESS', default='localhost')
APP_PORT = config('APP_PORT', default=5000)
DEBUG = config('DEBUG', default=False)