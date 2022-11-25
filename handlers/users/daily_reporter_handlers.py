from aiogram.dispatcher import FSMContext
from states.states import DailyPool
from aiogram.dispatcher.filters import Command
from keyboards.inline.callback_datas import menu_callbacks
from handlers.users.main_handlers import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, ContentTypes
from keyboards.inline.keyboards import start_menu, pool_very
from loader import dp, bot
from states.states import Start
from loguru import logger
from loader import access
import time
from datetime import datetime
from loader import admin_chat_id


logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


@dp.message_handler()
async def start_daily_pool():
    text = 'Как насчет daily pooling?'
    await bot.send_message(text=text, chat_id=admin_chat_id, reply_markup=pool_very)


@dp.callback_query_handler(menu_callbacks.filter(click1='start_daily_reporter'), state='*')
async def accept_daily_pool(call: CallbackQuery):
    text = 'Скинь данные по сну\nFormat: h:mm/h:mm'
    # Меняем текст в сообщении и убираем клавиатуру
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup='', text=text)

    await DailyPool.Start_Daily_Pool.set()


