import define as I
from define import json
from storages.cl.cl_editable import cl_editable
from storages.cl.cl_list import cl_list
from discord.ext import tasks


@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
class CL(I.app_commands.Group):
  ...
clc = CL(name="cl", description="カテゴリリーダー用のコマンドグループ")


class Role(I.app_commands.Group):
  ...
R = Role(name="role",parent=clc, description="ロールの設定を変更するコマンドグループ")

