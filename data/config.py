from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

AUTH_NAME = env.str('BOT_API_AUTH_NAME')
AUTH_PASS = env.str('BOT_API_AUTH_PASS')
API_ADDRESS = env.str('BOT_API_ADDRESS')
API_AUTH_ADDRESS = API_ADDRESS + env.str('BOT_API_AUTH_ADDRESS')
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.str('REDIS_PORT')
REDIS_DB = env.int('REDIS_DB')
REDIS_POOL = env.int('REDIS_POOL')
REDIS_PREFIX = env.str('REDIS_PREFIX')
