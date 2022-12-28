from pyrogram import Client



app = Client("test696_bot")


#print('runing...')

@app.on_message(group=1)
async def messageHandler(client,message):
    await message.reply(message.text)

app.run()