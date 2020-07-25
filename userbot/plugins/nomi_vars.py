"""Commands:
.bella
.fanculo
.meladai
.melodai"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="bella (.*)", outgoing=True)) 
async def _(event): 
    if event.fwd_from: 
        return 
    animation_interval = 0.5 
    animation_ttl = range(0, 101) 
    input_str = event.pattern_match.group(1) 
    #if input_str == "bella": 
    await event.edit(f"{input_str}") 
    animation_chars = [ 
 
            f"{input_str}", 
 
            f"{input_str} sei ", 
 
            f"{input_str} sei veramente ", 
            
           f"{input_str} sei veramente bella 🥺", 
 
        ] 
 
    for i in animation_ttl: 
            await asyncio.sleep(animation_interval) 
            await event.edit(animation_chars[i % 4])


@bot.on(dev_cmd(pattern="fanculo (.*)", outgoing=True)) 
async def _(event): 
    if event.fwd_from: 
        return 
    animation_interval = 0.5 
    animation_ttl = range(0, 101) 
    input_str = event.pattern_match.group(1) 
    #if input_str == "fanculo": 
    await event.edit(f"{input_str}") 
    animation_chars = [ 
 
            f"{input_str}", 
 
            f"{input_str} ma ", 
 
            f"{input_str} ma vai ", 
            
           f"{input_str} ma vai a",
           
           f"{input_str} ma vai a fanculo 🖕🏼", 
 
        ] 
 
    for i in animation_ttl: 
            await asyncio.sleep(animation_interval) 
            await event.edit(animation_chars[i % 4])


@bot.on(dev_cmd(pattern="meladai (.*)", outgoing=True)) 
async def _(event): 
    if event.fwd_from: 
        return 
    animation_interval = 0.5 
    animation_ttl = range(0, 101) 
    input_str = event.pattern_match.group(1) 
    #if input_str == "meladai": 
    await event.edit(f"{input_str}") 
    animation_chars = [ 
 
            f"{input_str}", 
 
            f"{input_str} mi ", 
 
            f"{input_str} mi dai ", 
            
           f"{input_str} mi dai la",
 
           f"{input_str} mi dai la figa? 👉🏼👈🏼", 
 
        ] 
 
    for i in animation_ttl: 
            await asyncio.sleep(animation_interval) 
            await event.edit(animation_chars[i % 4])


@bot.on(dev_cmd(pattern="melodai (.*)", outgoing=True)) 
async def _(event): 
    if event.fwd_from: 
        return 
    animation_interval = 0.5 
    animation_ttl = range(0, 101) 
    input_str = event.pattern_match.group(1) 
    #if input_str == "melodai": 
    await event.edit(f"{input_str}") 
    animation_chars = [ 
 
            f"{input_str}", 
 
            f"{input_str} mi ", 
 
            f"{input_str} mi dai ", 
            
           f"{input_str} mi dai il",
 
           f"{input_str} mi dai il cazzo? 👉🏼👈🏼", 
 
        ] 
 
        for i in animation_ttl: 
            await asyncio.sleep(animation_interval) 
            await event.edit(animation_chars[i % 4])