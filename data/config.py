from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

AUTH_NAME = env.str('BOT_API_AUTH_NAME')
AUTH_PASS = env.str('BOT_API_AUTH_PASS')
API_ADDRESS = env.str('BOT_API_ADDRESS')
API_AUTH_ADDRESS = API_ADDRESS + env.str('BOT_API_AUTH_ADDRESS')
