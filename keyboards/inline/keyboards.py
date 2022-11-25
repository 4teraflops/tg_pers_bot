from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callbacks

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='BTC', callback_data=menu_callbacks.new('start_menu', click1='btc')),
        InlineKeyboardButton(text='Тинь Инв', callback_data=menu_callbacks.new('start_menu', click1='stock_market'))
    ]
])

pool_very = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Yes', callback_data=menu_callbacks.new('start_menu', click1='start_daily_reporter')),
        InlineKeyboardButton(text='Not today', callback_data=menu_callbacks.new('start_menu', click1='daily_reporter_cancel'))
    ],
    [
        InlineKeyboardButton(text='Put off 1 hour', callback_data=menu_callbacks.new('start_menu', click1='daily_reporter_put_off'))
    ]
])
