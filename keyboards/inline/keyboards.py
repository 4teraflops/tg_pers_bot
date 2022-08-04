from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callbacks

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Службы мониторинга', callback_data=menu_callbacks.new('menu', click1='mons_menu'))
    ],
    [
        InlineKeyboardButton(text='Автотест demo.ckassa.ru',
                             callback_data=menu_callbacks.new('menu', click1='demo_checker'))
    ],
    [
        InlineKeyboardButton(text='Стукач', callback_data=menu_callbacks.new('menu', click1='news_poster'))
    ]
])

