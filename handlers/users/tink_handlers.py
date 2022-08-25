from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.callback_datas import menu_callbacks
from keyboards.inline.keyboards import start_menu
from loader import dp, bot
from states.states import Start, BTC
from src.analyser import insert_in_analysis_table
from loguru import logger
import os
from db.selector import collect_dict
from src.services_manager import get_data_from_tink


logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


@dp.callback_query_handler(menu_callbacks.filter(click1='stock_market'), state=Start.Start_menu)
async def show_tink_digest(call: CallbackQuery, state: FSMContext):
    await state.get_state()

    text = await get_data_from_tink()

    await call.message.answer(text=text)

    # В анализ
    insert_in_analysis_table(call.from_user.id, call.from_user.first_name, call.from_user.last_name,
                             call.from_user.username, call.data.split(':')[1])