import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from loguru import logger

logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


# Храним чувствительные данные в переменной окружения
load_dotenv()
token = os.getenv('TOKEN')
webhook_url = os.getenv('WEBHOOK_URL')
admin_id = os.getenv('ADMIN_ID')
access = os.getenv('ADMIN_ID')
mongo_host = os.getenv('MONGO_HOST')
mongo_port = os.getenv('MONGO_PORT')
mongo_user = os.getenv('MONGO_USER')
mongo_pass = os.getenv('MONGO_PASS')
chat_id = os.getenv('CHAT_ID')
admin_chat_id = os.getenv('ADMIN_CHAT_ID')
postgres_db_user = os.getenv('POSTGRES_DB_USER')
postgres_db_pass = os.getenv('POSTGRES_DB_PASS')
postgres_db_host = os.getenv('POSTGRES_DB_HOST')
postgres_db_port = os.getenv('POSTGRES_DB_PORT')
postgres_db_name = os.getenv('POSTGRES_DB_NAME')
# Параметры для прокси
# PROXY_AUTH = aiohttp.BasicAuth(login=posgresql_config.py.PROXY_USER, password=posgresql_config.py.PROXY_PASS)
bot = Bot(token)
storage = MongoStorage(host=f'{mongo_host}', port=f'{mongo_port}', db_name='aiogram_fsm', username=f'{mongo_user}', password=f'{mongo_pass}')
dp = Dispatcher(bot, storage=storage)

