#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.NewMessage(pattern="^/thumb$"))
async def sett(event):    
    Drone = event.client                    
    
    
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.", buttons=Button.force_reply())
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        

@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    await event.reply(f'Hii,\nI am @pyrogrammers save restricted contents bot, I can save files of restricted channels as well as group.\n**Hit /help to learn more.**', 
                      buttons=[
                        [Button.url("Updates Channel", url="https://t.me/pyrogrammers"),
                         Button.url("Support Group", url="https://t.me/+7ScFy39Vckk5MWQ1")],
                       
                        [Button.url("YouTube Channel", url="https://youtube.com/channel/UC2anvk7MNeNzJ6B4c0SZepw")],
                    ])
    # start help Message
@Drone.on(events.NewMessage(pattern="^/help$"))
async def search(event):
    await event.reply('<b><u>For Public Restricted Channel contents.</b></u>\nTo get public restricted Channel contents, just send your Post link i will give you that post without Downloading.\n\n<b><u>For Private Restricted Channel contents.</b></u>\nTo get private restricted Channel contents, First send me Channel invite link so that i can join your channel after that send me post link of your restricted Channel to get that post.', parse_mode="HTML")
#end help Message

