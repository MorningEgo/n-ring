import define_first as I
from define_first import pd
from .ngolds import *
from command_files.ngold.embed import *
import json



@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
class Ngold(I.app_commands.Group):
  ...
ngg = Ngold(name="ngold", description="Ngoldのコマンドグループ")


@ngg.command(name="transfer", description = "自身のNgoldを他のユーザーに譲渡します。")
@I.discord.app_commands.describe(
    to = "Ngoldを送るユーザー。",
    value = "相手に送るNgoldの数。"
)
async def transfer(ctx: I.discord.Interaction, to:I.discord.Member, value: int):
    print("=================")
    print("<< << << transfer >> >> >>")
    await ctx.response.defer(thinking=True)
    
    data = ng_read(ctx.user.id)
    ids = f"i{ctx.user.id}"
    
    if ctx.user.id == I.owner_id:
        check_id = True
    else:
        check_id = False
    
    if to.id == ctx.user.id or check_id is False:
        await ctx.followup.send(embed=ng_errormes(0))
    elif value <= 0:
        await ctx.followup.send(embed=ng_errormes(1))
    elif data.at[ids,'ng'] == 0 or check_id is False:
        await ctx.followup.send(embed=ng_errormes(2))
    elif data.at[ids,'ng'] <= -1 or check_id is False:
        await ctx.followup.send(embed=ng_errormes(3))
    elif data.at[ids,'ng'] < value or check_id is False:
        await ctx.followup.send(embed=ng_errormes(4))
    else:
        ng_add(userid=to.id, supplier=ctx.user.id, ng=value)
        ng_remove(userid=ctx.user.id, buyer=to.id, ng=value)
        
        send = ng_send_embed(send=ctx.user,receive=to,value=value)
        receive = ng_receive_embed(send=ctx.user,receive=to,value=value)

        await ctx.followup.send(embeds=[send,receive])
    print("=================")


@ngg.command(name="watch", description = "自身のNgoldの詳細を確認します。")
async def watch(ctx: I.discord.Interaction):
    print("=================")
    print("<< << << Watch >> >> >>")
    await ctx.response.defer(thinking=True)

    embed = ng_watch_embed(ctx.user)
    await ctx.followup.send(embed=embed)

    print("=================")


@ngg.command(name="add", description = "選択したユーザーのNgoldを増やします。管理者コマンド。")
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

@ngg.command(name="remove", description = "選択したユーザーのNgoldを減らします。管理者コマンド。")
async def remove(ctx: I.discord.Interaction, user:I.discord.Member, remove:int):
    print("=================")
    print("<< << << Remove >> >> >>")
    await ctx.response.defer(thinking=True)
    if ctx.user.id == I.owner_id:
        ng_remove(userid=user.id,buyer=I.client.user.id,ng=remove)
        embed = ng_send_embed(send=I.client.user,receive=user,value=remove)
    else:
        embed = ng_errormes(mes=7)
    await ctx.followup.send(embed=embed)

@ngg.command(name="reset", description = "選択したユーザーのNgoldをリセットします。管理者コマンド。")
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


@ngg.command(name="import", description="データを読み込みます。 管理者コマンド。")
async def import_csv(ctx: I.discord.Interaction, data:str):
    await ctx.response.defer(thinking=True)

    if ctx.user.id == I.owner_id:
        try:
            ng_read(None)
            data_json = json.loads(data)
            df = pd.DataFrame(data_json)
            ng_write(export_data=df)
            res = 0
        except:
            res = 1

        embed = ng_import(result=res)
    else:
        embed = ng_errormes(mes=7)
    await ctx.followup.send(embed=embed)



@ngg.command(name="export", description="データを出力します。 管理者コマンド。")
async def export_csv(ctx: I.discord.Interaction):
    await ctx.response.defer(thinking=True)

    if ctx.user.id == I.owner_id:
        df = ng_read(None)
        data = df.to_json()
        DB_PATH = I.client.get_channel(int(I.ngold_db))
        #await DB_PATH.send(f"```json\n{data}```")
        await DB_PATH.send(file=I.discord.File(FILE_PATH))
        mes = 0
        embed = ng_import(result=mes)
    else:
        embed = ng_errormes(mes=7)
    await ctx.followup.send(embed=embed)