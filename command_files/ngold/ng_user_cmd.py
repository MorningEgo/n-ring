import define_first as I
from define_first import pd
from .ngolds import *

from command_files.ngold.embed import *


def errormes(mes=int):
    meslist = [
        "取引相手に自分自身を指定することはできません。",
        "送るngの値は1以上でなければなりません。",
        "あなたはngを所持していません。",
        "負債がある状態でngを送ることはできません。",
        "自身の所持している以上のngを送ることはできません。",

    ]

    error = remove_embed = I.discord.Embed(
            title = "Ngold 取引拒否",
            description= meslist[mes],
            color= 0xed2f50
        )
    return error


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
        await ctx.followup.send(embed=errormes(0))
    elif value <= 0:
        await ctx.followup.send(embed=errormes(1))
    elif data.at[ids,'ng'] == 0 or check_id is False:
        await ctx.followup.send(embed=errormes(2))
    elif data.at[ids,'ng'] <= -1 or check_id is False:
        await ctx.followup.send(embed=errormes(3))
    elif data.at[ids,'ng'] < value or check_id is False:
        await ctx.followup.send(embed=errormes(4))
    else:
        ng_add(userid=to.id, supplier=ctx.user.id, ng=value)
        ng_remove(userid=ctx.user.id, buyer=to.id, ng=value)
        
        send = ng_send_embed(send=ctx.user,receive=to,value=value)
        receive = ng_receive_embed(send=ctx.user,receive=to,value=value)

        await ctx.followup.send(embeds=[send,receive])
    print("=================")


@ngg.command(name="watch", description = "自身のNgoldの詳細を確認します。")
async def transfer(ctx: I.discord.Interaction):
    print("=================")
    print("<< << << Watch >> >> >>")
    await ctx.response.defer(thinking=True)

    embed = ng_watch_embed(ctx.user)

    await ctx.followup.send(embed=embed)

    print("=================")
    