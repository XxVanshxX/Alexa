from userbot import client, CMD_HELP
from telethon import events
from userbot.events import javes05
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from pathlib import Path
from userbot import LOAD_PLUG
import sys, asyncio, traceback, os
import userbot.utils


@javes05(outgoing=True, pattern="^!installall (.*)")
async def install(event):
    try:
      chat = event.pattern_match.group(1) ; text = f"**Installing plugins from {chat}..\n\n**" ; cui = await client.get_messages(chat, limit = 75, filter=InputMessagesFilterDocument)  ; total = int(cui.total) ; total_doxx = range(0, total)
    except:
    	return await event.edit("Error\nUsage: `!installall <channel/group username>`")
    for ixo in total_doxx:
        await event.edit(text) ; mxo = cui[ixo].id ; downloaded_file_name = await event.client.download_media(await client.get_messages(chat, ids=mxo), "userbot/modules/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name) ; shortname = path1.stem
            if (os.path.basename(downloaded_file_name)).endswith('.py'):
               try:
                 load_module(shortname.replace(".py", "")) ; text += f"**✔️Installed** {(os.path.basename(downloaded_file_name))}\n"
               except:
               	text += f"**❌Failed to install** {(os.path.basename(downloaded_file_name))}\n" ; os.remove (downloaded_file_name) ; pass
            else: 
                  text += f"**⚠️Skiped** {(os.path.basename(downloaded_file_name))}\n" ; os.remove (downloaded_file_name)
        else:
            text += f"**⚠️Skiped** {(os.path.basename(downloaded_file_name))}\n" ; os.remove (downloaded_file_name)
    return await event.edit(f"{text}\n\n**Install completed**")
        
        
        
CMD_HELP.update({
    "install":
    "`!install <reply to a plugin>`\
\n**Usage:** Install the plugin\
\n\n`!installall <channel/group username>`\
\n**Usage:**Install all plugins from the channel or group\
"
})



