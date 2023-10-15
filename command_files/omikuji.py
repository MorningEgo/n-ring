import define as I
from define import json
import random
from nring_storage import omikuji_list as NOL

@I.tree.command(name="ンゴみくじ", description="今日のンゴみくじを引くよ\nお布施してないんだから、当たらなくても文句言わないでよね！*")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def omikuji(ctx:I.discord.Interaction):
    ...