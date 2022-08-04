from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callbacks

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='BTC', callback_data=menu_callbacks.new('menu', click1='btc')),
        InlineKeyboardButton(text='Акции', callback_data=menu_callbacks.new('menu', click1='stock_market'))
    ]
])

