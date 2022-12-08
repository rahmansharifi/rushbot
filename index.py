from pyrogram import Client, filters, idle

app = Client(
    'agent',
    in_memory=True, 
    api_id=762229,
    api_hash='9749fd3fa72176a0312c45ff5e42228f',
    app_version='1.0',
    device_model='Whitebox Server',
    system_version='1.0',
    bot_token='5988252315:AAFOC9dyVKMWrvSVkY4sNT9wpdS3mUrHlT4',
    plugins=dict(root='plugins'),
    proxy=dict(scheme='socks5', hostname='127.0.0.1', port=9150)
)

app.start()
print(True)
idle()
app.stop()