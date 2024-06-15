from keep_alive import keep_alive
import discord
from discord import ui, app_commands
import enum
import os
import random
from datetime import datetime, timedelta, timezone
import urllib.request, urllib.error
import re
import json
import typing
import time 
from time import sleep
from dotenv import load_dotenv
import pandas as pd # type: ignore
load_dotenv()

token = os.environ['DISCORD_BOT_TOKEN']

class aclient(discord.Client):

  def __init__(self):
    super().__init__(intents=discord.Intents.all())
    self.synced = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync(guild=discord.Object(id=token))
      self.synced = True

client = aclient()

tree = app_commands.CommandTree(client)

#-------------------------------------------------------------------------------------------#
#サーバーid
guildid = int(os.environ['GUILD_ID'])
scguild = int(os.environ['SCG_ID'])
#メッセージ送信チャンネル(んご：投稿動画・ライブ配信、test：チャンネル指定メッセージ)
send_ch = int(os.environ['LIVE_SEND_CH'])
#send_ch = int(os.environ['LIVE_SEND_CH_OP'])

#名前更新チャンネル(んご：専用ステージ、最下層のボイス)
rename_ch = int(os.environ['LIVE_RENAME_CH'])
#rename_ch = int(os.environ['LIVE_RENAME_CH_OP'])
owner_id = int(os.environ['OWNER_ID'])
#-------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  client