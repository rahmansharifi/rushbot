from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query(group=3)
async def _(Client, Query):
    if Query.data == 'support':
        await Query.message.edit(
            '[👥](https://www.precisionsg.com/hubfs/vendor%20vs%20third%20party%20support.jpg)'+' پشتیبانی و تسویه\n\nلطفا برای تسویه یا پشتیبانی به حساب ما منتقل شوید',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('👥 پشتیبانی ربات 👥',url='https://t.me/rush_acc_sup')
                    ],
                    [
                        InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                    ],
                ]
            )
        )