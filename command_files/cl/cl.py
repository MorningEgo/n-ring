import define_first as I
from define_first import json
from nring_storage.cl.cl_editable import cl_editable
from nring_storage.cl.cl_list import cl_list
from discord.ext import tasks


@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
class CL(I.app_commands.Group):
  ...
clc = CL(name="cl", description="カテゴリリーダー用のコマンドグループ")


class Role(I.app_commands.Group):
  ...
R = Role(name="role",parent=clc, description="ロールの設定を変更するコマンドグループ")

