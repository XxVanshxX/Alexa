from userbot.events import javes05
from userbot import bot, BOTLOG_CHATID
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import rekcah05
client = javes = bot 
from telethon.tl.functions.messages import GetCommonChatsRequest
from userbot import JAVES_NAME, JAVES_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
from telethon.events import ChatAction

async def get_user_from_event(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(f"`{JAVES_NNAME}`: ** Pass the user's username, id or reply!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Failed \n **Error**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
   






@client.on(ChatAction)
async def handler(rkG): 
   if rkG.user_joined or rkG.user_added:      
       try:       	
         from userbot.modules.sql_helper.gmute_sql import is_gmuted
         guser = await rkG.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned User Joined!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned`")                                                
                 except:                          
                    return 
    	
        





@javes.on(events.NewMessage(incoming=True))
async def muter(rkG):
    try:        
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
    except:
        return    
    gmuted = is_gmuted(rkG.sender_id)    
    if gmuted:
        for i in gmuted:
            if i.sender == str(rkG.sender_id):
                if rkG.is_private:                           
                    await rkG.client(BlockRequest(rkG.sender_id))
                    return await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gban User Found!!** \n"        
                     f"**Victim Id**: [{rkG.sender_id}](tg://user?id={rkG.sender_id})\n"                                
                     f"**Action **  : `Blocked`")                                                    
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned User Joined!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned`")                                                
                 except:                          
                    return 

















@javes05(outgoing=True, pattern="^!gban(?: |$)(.*)")
async def gspider(rk):    
   me = await rk.client.get_me() ; await rk.edit(f"`{JAVES_NNAME}:` **Requesting  to gban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
   if rk.is_private:       
   	user = rk.chat ; reason = rk.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = rk.chat.title  
   try:       
    user, reason = await get_user_from_event(rk)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await rk.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
   if user:      
        if user.id == 710844948:     
    	             return await rk.edit(f"`{JAVES_NNAME}:`**Error! cant gban this user.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import gmute 
          await client.edit_permissions(rk.chat_id, user, view_messages=False)    
          a += 1
          await rk.client.send_message(rk.chat_id, f"`{JAVES_NNAME}:` **Requested to gban user!!** \n"                     
                     f"`GbanAdmin`: **{my_username}**\n"
                     f"`GbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `Banned`\n"                    
                     f"**Gbanned Reason**  : `{reason}`")                                                       
        except:
   	     pass
        try:
          common = await client(GetCommonChatsRequest(user, 0, 100))        
        except:
          return await rk.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
        try:
          await rk.client(BlockRequest(user))
          block = 'True'
        except Exception as e:      
          block = 'Failed(error sent)'
          error = str(e)
          if BOTLOG_CHATID:
             await rk.client.send_message(BOTLOG_CHATID, f"Faild to block user here is the error report , send it to @javessupport \n\n **Error**\n {error}")
        try:
         for chat in common.chats:                	  
               await client.edit_permissions(chat.id, user, view_messages=False)          
               a += 1
               await rk.client.send_message(chat.id, f"`{JAVES_NNAME}:` **Requested to gban user!!** \n"                     
                     f"`GbanAdmin`: **{my_username}**\n"
                     f"`GbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `Banned`\n"                    
                     f"**Gbanned Reason**  : `{reason}`")                                                                                     
        except Exception as e:
             b += 1
             #error = str(e)
             #await rk.client.send_message(BOTLOG_CHATID, f"Gban error failed chat id error report \n\n **Error**\n {error}")        
       
          
   else:
       await rk.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if gmute(user.id) is False:
            return await rk.edit(f"`{JAVES_NNAME}:`**Error! User probably already gbanned.**")
   except:
    	pass
   await rk.edit(f"`{JAVES_NNAME}:` **Gbanned  {a} chat(s) , Failed {b} chat(s)\n Block user - {block}\n Gban watch - True \n\n Victim Name [{user.first_name}](tg://user?id={user.id})**") 
        




@javes05(outgoing=True, pattern="^!ungban(?: |$)(.*)")
async def gspider(rk):    
   me = await rk.client.get_me() ; await rk.edit(f"`{JAVES_NNAME}:` **Requesting to ungban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0   
   try:
     from userbot.modules.sql_helper.gmute_sql import ungmute
   except:
   	return
   if rk.is_private:       
   	user = rk.chat ; reason = rk.pattern_match.group(1) ; chat_title = 'PM'  
   else:   	   	
   	chat_title = rk.chat.title  
   try:       
    user, reason = await get_user_from_event(rk)    
    await client.edit_permissions(rk.chat_id, user, send_messages=True) 
    a += 1
    await rk.client.send_message(rk.chat_id, f"`{JAVES_NNAME}:` **Requested to ungban user!!** \n"                     
                     f"`GbanAdmin`: **{my_username}**\n"
                     f"`UnGbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `UnBanned`")         
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await rk.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
   if user:
       if not user == 710804948:    	   
        try:
          common = await client(GetCommonChatsRequest(user, 0, 100))        
        except:
          return await rk.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
        try:
          await rk.client(UnblockRequest(user))
          unblock = 'True'
        except Exception as e:      
          unblock = 'Failed(error sent)'
          error = str(e)
          if BOTLOG_CHATID:
              await rk.client.send_message(BOTLOG_CHATID, f"Faild to unblock user here is the error report , send it to @javessupport \n\n **Error**\n {error}")
        try:
         for chat in common.chats:                	  
               await client.edit_permissions(chat.id, user, send_messages=True)          
               a += 1
               await rk.client.send_message(chat.id, f"`{JAVES_NNAME}:` **Requested to ungban user!!** \n"                     
                     f"`GbanAdmin`: **{my_username}**\n"
                     f"`GbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `UnBanned`")                                                         
        except Exception as e:
             b += 1                          
       else:  	 
          return await rk.edit(f"`{JAVES_NNAME}:`**I cant ungban this user**")
   else:
       await rk.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if ungmute(user.id) is False:
            return await rk.edit(f"`{JAVES_NNAME}:`**Error! User probably already ungbanned.**")
   except:
    	pass
   await rk.edit(f"`{JAVES_NNAME}:` **UnGbanned  {a} chat(s) , Failed {b} chat(s)\n UnBlock user - {unblock}\n Gban watch - False \n\n Victim Name [{user.first_name}](tg://user?id={user.id})**") 
        




@javes.on(rekcah05(pattern=f"gban(?: |$)(.*)", allow_sudo=True))
async def gspider(rk):    
   me = await rk.client.get_me() ; rkp = await rk.reply(f"`{JAVES_NNAME}:` **Requesting  to gban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
   if rk.is_private:       
   	chat_title = 'PM'
   else:
   	chat_title = rk.chat.title  
   try:       
    user, reason = await get_user_from_event(rk)    
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await rkp.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
   if user:
        if user.id == 710844948:     
    	             return await rkp.edit(f"`{JAVES_NNAME}:`**Error! cant gban this user.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import gmute 
          await client.edit_permissions(rk.chat_id, user, view_messages=False)    
          a += 1
          await rk.client.send_message(rk.chat_id, f"`{JAVES_NNAME}:` **Requested to gban user!!** \n"                     
                     f"`GbanAdmin`: **Sudo**\n"
                     f"`GbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `Banned`\n"                    
                     f"**Gbanned Reason**  : `{reason}`")                                                       
        except:
   	     pass	   
        try:
          common = await client(GetCommonChatsRequest(user, 0, 100))        
        except:
          return await rkp.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
        try:
          await rk.client(BlockRequest(user))
          block = 'True'
        except Exception as e:      
          block = 'Failed(error sent)'
          error = str(e)
          if BOTLOG_CHATID:
             await rk.client.send_message(BOTLOG_CHATID, f"Faild to block user here is the error report , send it to @javessupport \n\n **Error**\n {error}")
        try:
         for chat in common.chats:                	  
               await client.edit_permissions(chat.id, user, view_messages=False)          
               a += 1
               await rk.client.send_message(chat.id, f"`{JAVES_NNAME}:` **Requested to gban user!!** \n"                     
                     f"`GbanAdmin`: **Sudo**\n"
                     f"`GbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `Banned`\n"                    
                     f"**Gbanned Reason**  : `{reason}`")                                                                                     
        except Exception as e:
             b += 1
             #error = str(e)
             #await rk.client.send_message(BOTLOG_CHATID, f"Gban error failed chat id error report \n\n **Error**\n {error}")        
       
   else:
       await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if gmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already gbanned.**")
   except:
    	pass
   await rkp.edit(f"`{JAVES_NNAME}:` **Gbanned  {a} chat(s) , Failed {b} chat(s)\n Gban watch - True \n\n Victim Name [{user.first_name}](tg://user?id={user.id})**") 
        




@javes.on(rekcah05(pattern=f"ungban(?: |$)(.*)", allow_sudo=True))
async def gspider(rk):    
   me = await rk.client.get_me() ; rkp = await rk.reply(f"`{JAVES_NNAME}:` **Requesting  to ungban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0   
   try:
     from userbot.modules.sql_helper.gmute_sql import ungmute
   except:
   	return
   if rk.is_private:       
   	chat_title = 'PM'
   else:   	   	
   	chat_title = rk.chat.title  
   try:       
    user, reason = await get_user_from_event(rk)    
    await client.edit_permissions(rk.chat_id, user, send_messages=True) 
    a += 1
    await rk.client.send_message(rk.chat_id, f"`{JAVES_NNAME}:` **Requested to ungban user!!** \n"                     
                     f"`GbanAdmin`: **Sudo**\n"
                     f"`GbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `UnBanned`")         
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await rkp.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
   if user:
       if not user == 710804948:    	   
        try:
          common = await client(GetCommonChatsRequest(user, 0, 100))        
        except:
          return await rkp.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
        try:
          await rk.client(UnblockRequest(user))
          unblock = 'True'
        except Exception as e:      
          unblock = 'Failed(error sent)'
          error = str(e)
          if BOTLOG_CHATID:
              await rk.client.send_message(BOTLOG_CHATID, f"Faild to unblock user here is the error report , send it to @javessupport \n\n **Error**\n {error}")
        try:
         for chat in common.chats:                	  
               await client.edit_permissions(chat.id, user, send_messages=True)          
               a += 1
               await rk.client.send_message(chat.id, f"`{JAVES_NNAME}:` **Requested to ungban user!!** \n"                     
                     f"`GbanAdmin`: **Sudo**\n"
                     f"`GbannedChat` : **{chat_title}**\n\n"
                     f"**Victim Name**: [{user.first_name}](tg://user?id={user.id})\n"
                     f"**Victim ID** : `{user.id}`\n"  
                     f"**Action** : `UnBanned`")                                                         
        except Exception as e:
             b += 1                          
       else:  	 
          return await rkp.edit(f"`{JAVES_NNAME}:`**I cant ungban this user**")
   else:
       await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if ungmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already ungbanned.**")
   except:
    	pass
   await rkp.edit(f"`{JAVES_NNAME}:` **UnGbanned  {a} chat(s) , Failed {b} chat(s)\n UnBlock user - {unblock}\n Gban watch - False \n\n Victim Name [{user.first_name}](tg://user?id={user.id})**") 
        



