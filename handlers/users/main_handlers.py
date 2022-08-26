from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, ContentTypes
from keyboards.inline.keyboards import start_menu
from loader import dp
from states.states import Start
from loguru import logger
from loader import access

logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


@dp.message_handler(Command('start'))
async def show_start_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(text="Подтвердить свой номер", request_contact=True))
    await message.answer("Подтверди свой номер", reply_markup=keyboard)
    await Start.Auth.set()


@dp.message_handler(Command('reset'), state="*")
async def reset_states(message: Message):
    await message.answer(text="Состояния сброшены. Возврат к авторизации...")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(text="Подтвердить свой номер", request_contact=True))
    await message.answer("Подтверди свой номер", reply_markup=keyboard)
    await Start.Auth.set()


@dp.callback_query_handler(state=None)
async def lost_state(call: CallbackQuery, state: FSMContext):
    await state.get_state()
    await call.message.answer(text='Cостояние пользователя сброшено.\nСейчас вы будете перенаправлены на сценарий авторизации.\nНажми на "подтвердить свой номер".')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(text="Подтвердить свой номер", request_contact=True))

    await call.message.answer("Подтверди свой номер", reply_markup=keyboard)
    await Start.Auth.set()


@dp.message_handler(content_types=ContentTypes.CONTACT, state=Start.Auth)
async def auth(message: Message, state: FSMContext):
    await state.get_state()
    user_phone = message.contact.phone_number
    await state.update_data(Phone=user_phone)  # Запомним телефон клиента
    #logger.info(f'user_phone:{user_phone}')
    if user_phone == access:
        text = 'Привет! Выбирай кнопку'
        await message.answer(text=text, reply_markup=start_menu)
        await Start.Start_menu.set()
    else:
        await message.answer_video(video='BAACAgIAAxkBAAMuYuu8wDrG8ctliC_7upWnLDHwlRcAAsgYAAL_s2FL6cqy1UcDE9YpBA')


