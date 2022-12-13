from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.callback_datas import menu_callbacks
from loader import dp, bot
from states.states import Start, Tink
from loguru import logger
from src.services_manager import get_data_from_tink
from keyboards.inline.keyboards import start_menu


logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


@dp.callback_query_handler(menu_callbacks.filter(click1='stock_market'), state=Start.Start_menu)
async def show_tink_digest(call: CallbackQuery, state: FSMContext):
    await state.get_state()

    text = await get_data_from_tink()
    # Меняем текст в сообщении и убираем клавиатуру
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup='', text=text)
    # Отправляем стартовое меню, чтоб оно всегла было внизу
    text = 'Привет! Выбирай кнопку'
    await call.message.answer(text=text, reply_markup=start_menu)

    #await Tink.Tink_Digest.set()
