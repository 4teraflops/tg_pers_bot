import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from loguru import logger

logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


# Храним чувствительные данные в переменной окружения
load_dotenv()
token = os.getenv('token')
webhook_url = os.getenv('webhook_url')
admin_id = os.getenv('admin_id')
access = os.getenv('access')
# Параметры для прокси
#PROXY_AUTH = aiohttp.BasicAuth(login=config.py.PROXY_USER, password=config.py.PROXY_PASS)
bot = Bot(token)
storage = MongoStorage('localhost', 27017, db_name='aiogram_fsm')
dp = Dispatcher(bot, storage=storage)

