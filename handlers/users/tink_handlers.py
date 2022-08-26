from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.callback_datas import menu_callbacks
from loader import dp
from states.states import Start
from loguru import logger
from src.services_manager import get_data_from_tink


logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


@dp.callback_query_handler(menu_callbacks.filter(click1='stock_market'), state=Start.Start_menu)
async def show_tink_digest(call: CallbackQuery, state: FSMContext):
    await state.get_state()

    text = await get_data_from_tink()

    await call.message.answer(text=text)