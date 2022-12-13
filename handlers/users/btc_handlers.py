from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.callback_datas import menu_callbacks
from keyboards.inline.keyboards import start_menu
from loader import dp, bot
from states.states import Start, BTC
from loguru import logger
from db.selector import collect_dict


logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


@dp.callback_query_handler(menu_callbacks.filter(click1='btc'), state=Start.Start_menu)
async def show_btc_menu(call: CallbackQuery, state: FSMContext):
    await state.get_state()
    dict_for_text = collect_dict()
    #logger.info(f'dict_for_text: {dict_for_text}')
    text = f'BTC/RUB : {dict_for_text["btc_rub"]}\n' \
           f'BTC/USD : {dict_for_text["btc_usd"]}\n' \
           f'Asset : {dict_for_text["asset_actual_rub"]}\n' \
           f'Profit : {dict_for_text["profit_rub"]}\n' \
           f'Percent Profit : {dict_for_text["profit_percent"]}'
    # Меняем текст в сообщении и убираем клавиатуру
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup='', text=text)
    # Отправляем стартовое меню, чтоб оно всегла было внизу
    text = 'Привет! Выбирай кнопку'
    await call.message.answer(text=text, reply_markup=start_menu)
