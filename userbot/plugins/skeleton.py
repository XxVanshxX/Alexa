from telethon import events

import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"Skeletons"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 27)

    await event.edit("Skeletons")

    animation_chars = [

            "☠️💀🦴",
            
            "☠️🦴💀",

            "🦴☠️💀",

            "🦴💀☠️",

            "☠️💀🦴",
            
            "☠️🦴💀",

            "🦴☠️💀",

            "🦴💀☠️",
            
            "☠️💀🦴",
            
            "☠️🦴💀",

            "🦴☠️💀",

            "🦴💀☠️",

            "☠️💀🦴",
            
            "☠️🦴💀",

            "🦴☠️💀",

            "🦴💀☠️",
            
            "☠️💀🦴",
            
            "☠️🦴💀",

            "🦴☠️💀",

            "🦴💀☠️",
          
            "☠️💀🦴",
            
            "☠️🦴💀",

            "🦴☠️💀",

            "🦴💀☠️",
            
            "☠️💀🦴",
            
            "☠️🦴💀",

            "🦴☠️💀",

            "🦴💀☠️",
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 27])