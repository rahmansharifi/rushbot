import json
from pyromod import listen
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fb import firebase

bought = firebase('/bought')

@Client.on_callback_query(group=6)
async def _(Client, Query):
    global bought
    if Query.data == 'buyaccount':
        try:
            Key = list(bought.load().keys())[0]
            Obj = bought.read(Key)
        except:
            await Query.message.edit(
                'متاسفانه شماره ای برای فروش موجود نیست',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                        ],
                    ]
                )
            )
            return None
        await Query.message.edit(
            '⚡️ خرید اکانت - شماره ای که باید وارد تلگرام کنید: `{}`'.format(Obj['number']),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🔐 گرفتن کد 🔐','code '+Key)
                    ],
                    [
                        InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                    ],
                ]
            )
        )