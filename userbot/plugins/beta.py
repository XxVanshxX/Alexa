import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import javes05
from userbot import bot, CMD_HELP
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)

@javes05(outgoing=True, pattern="^!mail(?: |$)(.*)")
async def _(event):
   if event.fwd_from:
      return 
   chat = "@fakemailbot"
   command = "/id"
   await event.edit(f"`{JAVES_NNAME}: ` **Fakemail list getting check @fakemailbot **")
   async with bot.conversation(chat) as conv:
        try:
            m = await event.client.send_message("@fakemailbot","/id")     
            await asyncio.sleep(5)
            k = await event.client.get_messages(entity="@fakemailbot", limit=1, reverse=False) 
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError: 
            await event.reply("```Please unblock @fakemailbot and try again```")
            



@javes05(outgoing=True, pattern="^!ushort(?: |$)(.*)")
async def _(event):
       rksong = event.pattern_match.group(1)      
       await event.edit(f"**{JAVES_NNAME}: `shorting `** {rksong} ** `url please wait........`")
       chat = "@LinkGeneratorBot"
       async with bot.conversation(chat) as conv:         
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=355705793))              
              await conv.send_message("/start")
              response = await conv.get_response()     
              if not response.text.startswith("🔗"):      
                         await event.edit(f"**{JAVES_NNAME}**: `sorry, look like my frined is sleeping.... please try later `")
              else:
                         await conv.send_message(rksong)
                         song2 = await conv.get_response()
                         await bot.send_message(event.chat_id, song2)                         
              
                   

@javes05(outgoing=True, pattern="^!name2(?: |$)(.*)")
async def _(event):
 reply_message = await event.get_reply_message()
 idd = reply_message.from_id
 if idd == 710844948:
  await reply_message.reply(f"`{JAVES_NNAME}: he is my master so i can't `")
 else:
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("`Can't scan bot meaage`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```reply to a media message```")
       return
    chat = "@SangMataInfo_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Reply to actual users message.`")
       return
    await event.edit("` Hacking........`")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await bot.forward_messages(chat, reply_message)
              response = await conv.get_response()
          except YouBlockedUserError: 
              await event.reply("`Please unblock @sangmatainfo_bot and try again`")
              return
          if response.text.startswith("Forward"):
             await event.edit("`Privacy error!`")
          else: 
             await bot.send_message(event.chat_id, response)                         
             song2 = await conv.get_response()
             await bot.send_message(event.chat_id, song2)                         








@javes05(outgoing=True, pattern="^!lyrics2(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{JAVES_NNAME}: ` **Reply to any user message.**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit(f"`{JAVES_NNAME}: ` **ype & send song then tag it type !lyrics2**")
       return
    chat = "@iLyricsBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{JAVES_NNAME}: ` **Reply to actual users message.**")
       return
    await event.edit(f"`{JAVES_NNAME}: ` **Processing please check @iLyricsBot**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=232268607))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply(f"`{JAVES_NNAME}: ` **error1**")
              return
          if response.text.startswith("Hello,"):
             await event.edit(f"`{JAVES_NNAME}: ` **privacy error**")
          else: 
             await asyncio.sleep(10)
             await event.edit(f"{response.message.message}")






@javes05(outgoing=True, disable_errors=True, pattern="^!fry(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{JAVES_NNAME}: ` **reply to a sticker**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"`{JAVES_NNAME}: ` **reply to a sticker**")
       return
    chat = "@image_deepfrybot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{JAVES_NNAME}: ` **Reply to actual users message.***")
       return
    await event.edit(f"`{JAVES_NNAME}: ` **Frying image...**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=432858024))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @image_deepfrybot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{JAVES_NNAME}: ` **privacy error**")
          else:
          	if response.text.startswith("Select"):
          		await event.edit(f"`{JAVES_NNAME}: Please go to` @DrWebBot `and select your language.`") 
          	else: 
          			await bot.send_file(event.chat_id, response.message.media)



@javes05(outgoing=True, disable_errors=True, pattern="^!mask(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{JAVES_NNAME}: ` **Reply to a photo/Sticker**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"`{JAVES_NNAME}: ` **Reply to a sticker/photo**")
       return
    chat = "@hazmat_suit_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{JAVES_NNAME}: ` **Reply to actual users message.**")
       return
    await event.edit(f"`{JAVES_NNAME}: ` **Making mask.....**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=905164246))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @hazmat_suit_bot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{JAVES_NNAME}: ` **privacy error**")
          else:
          	if response.text.startswith("Select"):
          		await event.edit(f"`{JAVES_NNAME}: Please go to` @DrWebBot `and select your language.`") 
          	else: 
          			await bot.send_file(event.chat_id, response.message.media)



