from userbot import CMD_HELP
from telethon import events
import asyncio
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
import random, re
from collections import deque
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Cat"     


@borg.on(admin_cmd(pattern=r"theart$", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 117)

    animation_chars = [

            "❤️",

            "🧡",

            "💛",

            "💚",

            "💙",

            "💜",

            "🖤",

            "💘",

            "💝",

            "❤️",

            "🧡",

            "💛",

            "💚",

            "💙",

            "💜",

            "🖤",

            "💘",

            "💝"

        ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 100])