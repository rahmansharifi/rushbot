from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query(group=4)
async def _(Client, Query):
    if Query.data == 'myaccount':
        await Query.message.edit(
            '[👤](https://www.venminder.com/hubfs/Blog_Images/2022_Blog_Posts/07.26.2022-reviewing-vendor-soc-complementary-user-entity-controls-cuecs-FEATURED.jpg)'+' حساب کاربری\n\nشماره حساب: {}\nاکانت های خریداری شده: {}\nاکانت های فروخته شده: {}\nمبلغی که از این بابت میگیرید: {} تومان'.format(
                Query.from_user.id,
                2,
                15,
                15*7000
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🏠 بازگشت به خانه 🏠','index')
                    ],
                ]
            )
        )