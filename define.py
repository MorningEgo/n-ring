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
#サーバーid(んご、TestMain)
scguild = os.environ['SCG_ID']
guildid = os.environ['GUILD_ID']

#メッセージ送信チャンネル(んご：登校動画・ライブ配信、test：チャンネル指定メッセージ)
send_ch = 1053725844448739398
#send_ch = 1022544579611856996

#名前更新チャンネル(んご：専用ステージ、最下層のボイス)
rename_ch = 1054417954038632578
#rename_ch = 1054419304155721858
#-------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  client