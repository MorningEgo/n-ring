import define_first as I
from define_first import pd
from .ngolds import *
from command_files.ngold.embed import *
import json


@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
class NgoldSystem(I.app_commands.Group):
  ...
ngsys = NgoldSystem(name="ngsys", description="Ngoldの管理コマンドグループ")

@ngsys.command(name="add", description = "選択したユーザーのNgoldを増やします。管理者コマンド。")
async def add(ctx: I.discord.Interaction, user:I.discord.Member, add:int):
    print("=================")
    print("<< << << Add >> >> >>")
    await ctx.response.defer(thinking=True)
    
    if ctx.user.id == I.owner_id:
        ng_add(userid=user.id,supplier=I.client.user.id,ng=add)
        embed = ng_receive_embed(send=I.client.user,receive=user,value=add)
    else:
        embed = ng_errormes(mes=7)
    await ctx.followup.send(embed=embed)


@ngsys.command(name="remove", description = "選択したユーザーのNgoldを減らします。管理者コマンド。")
async def remove(ctx: I.discord.Interaction, user:I.discord.Member, remove:int):
    print("=================")
    print("<< << << Remove >> >> >>")
    await ctx.response.defer(thinking=True)
    if ctx.user.id == I.owner_id:
        ng_remove(userid=user.id,buyer=I.client.user.id,ng=remove)
        embed = ng_send_embed(send=user,receive=I.client.user,value=remove)
    else:
        embed = ng_errormes(mes=7)
    await ctx.followup.send(embed=embed)


@ngsys.command(name="reset", description = "選択したユーザーのNgoldをリセットします。管理者コマンド。")
async def reset(ctx: I.discord.Interaction, user:I.discord.Member):
    print("=================")
    print("<< << << Reset >> >> >>")
    await ctx.response.defer(thinking=True)
    if ctx.user.id == I.owner_id:
        ng_reset(userid=user.id)
        embed = ng_watch_embed(user=user)
    else:
        embed = ng_errormes(mes=7)
    await ctx.followup.send(embed=embed)


@ngsys.command(name="export", description="データを出力します。 管理者コマンド。")
async def export_csv(ctx: I.discord.Interaction):
    await ctx.response.defer(thinking=True)

    if ctx.user.id == I.owner_id:
        df = ng_read(None)
        data = df.to_json()
        DB_PATH = I.client.get_channel(int(I.ngold_db))
        await DB_PATH.send(file=I.discord.File(FILE_PATH))
        mes = 0
        embed = ng_import(result=mes)
    else:
        embed = ng_errormes(mes=7)
    await ctx.followup.send(embed=embed)