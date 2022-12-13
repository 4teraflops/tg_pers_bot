from aiogram.dispatcher.filters.state import StatesGroup, State


class Start(StatesGroup):
    Auth = State()
    Phone = State()
    Start_menu = State()


class BTC(Start):
    BTC_Digest = State()


class Tink(Start):
    Tink_Digest = State()
