from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command('start'),group=1)
async def _(Client, Message):
    await Message.reply(
        'به ربات خرید و فروش اکانت مجازی Rush خوش آمدید.\nبرای استفاده از ربات از گزینه های پایین استفاده کنید'+'[🙂](https://cdn.sanity.io/images/14xthjfi/production/4818187b085f4ef7750bdbaf0ee372dd04786125-1800x1012.jpg)',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('👤 حساب کاربری 👤','myaccount')
                ],
                [
                    InlineKeyboardButton('خرید اکانت ⚡️','buyaccount'),
                    InlineKeyboardButton('✨ فروش اکانت','sellaccount')
                ],
                [
                    InlineKeyboardButton('💳 تسویه و پشتیبانی 👥','support')
                ],
            ]
        )
    )