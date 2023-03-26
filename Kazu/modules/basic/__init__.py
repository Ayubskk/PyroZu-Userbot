import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Kazu"])

async def join(client):
    try:
        await client.join_chat("")
        await client.join_chat("")
        await client.join_chat("")
        await client.join_chat("")
    except BaseException:
        pass
