import define_first as I
from command_files.beginner_custom.scteam import sct
from command_files.cl.cl import clc, R
from loop import loop_1s,loop_1m,loop_1h
from command_files.cl.role.loop import cl_loop
from discord.ext import tasks
####################################################################
# 起動メッセージ

@I.client.event
async def on_ready():
  #loop_1s.start()
  #loop_1m.start()
  #loop_1h.start()

  cl_loop.start()
		
  mode = [
    "VALORANT", "Overwatch2", "Apex Legends", "Splatoon3", "Minecraft",
    "Sons of The FOREST", "Garry's Mod", "原神", "Escape from Tarkov",
    "大乱闘スマッシュブラザーズ Special", "カタン島の開拓者たち", "麻雀", "Adobe AfterEffects 2003",
    "Adobe Photoshop 814", "Adobe Illustrator 514"
  ]

  print("ンゴ～")
  print('------------------------------')
  print("discord.py Ver." + I.discord.__version__)  # discord.pyのバージョン
  print('------------------------------')
  activ = I.discord.Activity(status=I.discord.Status.online,
                              name="おまえら",
                              type=I.discord.ActivityType.watching)
  I.tree.add_command(sct)
  I.tree.add_command(clc)
  I.tree.add_command(R)
  await I.client.change_presence(activity=activ)
  await I.tree.sync(guild=I.discord.Object(id=I.guildid))
  await I.tree.sync(guild=I.discord.Object(id=I.scguild))