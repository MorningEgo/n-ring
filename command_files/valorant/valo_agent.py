import define as I
from nring_storage.valorant.agents import r, d, i, c, s, a
class Mode(I.enum.Enum):
  デュエリストのみ = "デュエリスト"
  コントローラーのみ = "コントローラー"
  イニシエーターのみ = "イニシエーター"
  センチネルのみ = "センチネル"
  ロールで抽選 = "ロールで抽選"

cond_head = "`[ 条件："
cond_foot = "のみ ]`"

@I.tree.command(name="agent",
  description="エージェントを抽選します。modeを使用してロール限定抽選、ロールの抽選が可能です。")
@I.discord.app_commands.describe(mode="抽選モードを変更します。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def agt(ctx: I.discord.Interaction, mode: Mode = None):

  if mode == Mode.ロールで抽選:
    choice = I.random.choice(r)
    embed = I.discord.Embed(
      color=0xff3b5a,
      title="次のロールはコレだよ！"
    )
  else:
    if mode == Mode.デュエリストのみ:
      agt = d
      m = Mode.value

    elif mode == Mode.イニシエーターのみ:
      agt = i
      m = Mode.value
    elif mode == Mode.コントローラーのみ:
      agt = c
      m = Mode.value
    elif mode == Mode.センチネルのみ:
      agt = s
      m = Mode.value
    else:
      agt = a
      m = "すべてのエージェント"
      
    choice = I.random.choice(agt)

    embed = I.discord.Embed(
      color=0xff3b5a,
      title="次のエージェントはコイツだよ！"
    )

  embed.add_field(
    name= choice[1],
    value= choice[0]
  )
  
  embed.set_author(
    name= ctx.user.name,
    icon_url= ctx.user.avatar
  )
  embed.set_thumbnail(url=choice[2])
  embed.set_footer(
    text= f"条件：{m}"
  )
  await ctx.response.send_message(embed=embed)