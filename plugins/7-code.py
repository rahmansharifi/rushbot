import pyrogram
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fb import firebase

bought = firebase('/bought')

@Client.on_callback_query(group=7)
async def _(Client, Query):
    global bought
    if Query.data.startswith('code '):
        Obj = bought.read(Query.data.split()[1])
        pyro = pyrogram.Client(
            'agent',
            in_memory=True, 
            api_id=762229,
            api_hash='9749fd3fa72176a0312c45ff5e42228f',
            app_version='1.0',
            device_model='Whitebox Server',
            system_version='1.0',
            session_string=Obj['session'],
            proxy=dict(scheme='socks5', hostname='127.0.0.1', port=9150)
        )
        await pyro.connect()
        Codes = pyro.get_chat_history(777000,1)
        async for m in Codes:
            Secret = m.text[12:17]
        await Query.message.edit('کد اتصال شما `{}` می باشد'.format(Secret))
        await pyro.disconnect()
        bought.delete(Query.data.split()[1])