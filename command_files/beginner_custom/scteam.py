import define as I
import os
@I.discord.app_commands.guilds(I.discord.Object(id=I.scguild))
class scT(I.app_commands.Group):
  ...

sct = scT(name="scteams", description="チームを設定します。")

@sct.command(name="set", description="チームの決定")
@I.discord.app_commands.describe(team1="メンションとメンションの間は空白1文字のみにしてください。",
                               team2="メンションとメンションの間は空白1文字のみにしてください。")
async def sc_set(ctx: I.discord.Interaction, team1: str, team2: str):
  await ctx.response.defer(thinking=True)
  # ロールid取得
  scguild = ctx.guild
  sc_team1 = scguild.get_role(1116950828322930708)
  sc_team2 = scguild.get_role(1116950852515659838)

  #sc_team1 = scguild.get_role(1117515183519178864)
  #sc_team2 = scguild.get_role(1117515234123460608)

  #いったんロールから全員削除
  sct1_users = []
  sct1_users = sc_team1.members
  for delsct1 in sct1_users:
    await delsct1.remove_roles(sc_team1)

  sct2_users = []
  sct2_users = sc_team2.members
  for delsct2 in sct2_users:
    await delsct2.remove_roles(sc_team2)

  # team1の割り当て
  t1_ulist = []
  t1_ulist = team1.split()

  for _1 in t1_ulist:
    t1_user = int(I.re.search(r'<@(.+)>', _1).group(1))
    t1_user_id = scguild.get_member(t1_user)
    await t1_user_id.add_roles(sc_team1)

  # team2の割り当て
  t2_ulist = []
  t2_ulist = team2.split()

  for _2 in t2_ulist:
    t2_user = int(I.re.search(r'<@(.+)>', _2).group(1))
    t2_user_id = scguild.get_member(t2_user)
    await t2_user_id.add_roles(sc_team2)

  #現在のロール付きユーザーを取得
  # team1
  t1_latest = []
  t1_latest_id = []
  t1_latest_id = sc_team1.members
  for t1l_ in t1_latest_id:
    t1_latest.append(t1l_.mention)
    t1_latest_mention = "\n".join(t1_latest)
  # team2
  t2_latest = []
  t2_latest_id = []
  t2_latest_id = sc_team2.members
  for t2l_ in t2_latest_id:
    t2_latest.append(t2l_.mention)
    t2_latest_mention = "\n".join(t2_latest)
  #####
  scteams_embed = I.discord.Embed(title="**チームが決定しました！**", color=0xff3b5a)
  scteams_embed.set_thumbnail(
    url= os.environ['SC_ICON']
  )
  scteams_embed.add_field(name="**チーム1**：",
                          value=f"{t1_latest_mention}",
                          inline=False)
  scteams_embed.add_field(name="─  ─  ─  ─  ─  **VS**  ─  ─  ─  ─  ─",
                          value="",
                          inline=False)
  scteams_embed.add_field(name="**チーム2**：",
                          value=f"{t2_latest_mention}",
                          inline=False)

  await ctx.followup.send(embed=scteams_embed, ephemeral=False)

@sct.command(name="remove", description="チームメンバーを削除します。")
async def sc_remove(ctx: I.discord.Interaction):
  await ctx.response.defer(thinking=True)
  # ロールid取得
  scguild = ctx.guild
  sc_team1 = scguild.get_role(1116950828322930708)
  sc_team2 = scguild.get_role(1116950852515659838)

  #sc_team1 = scguild.get_role(1117515183519178864)
  #sc_team2 = scguild.get_role(1117515234123460608)

  #ロールから全員削除
  sct1_users = []
  sct1_users = sc_team1.members
  for delsct1 in sct1_users:
    await delsct1.remove_roles(sc_team1)

  sct2_users = []
  sct2_users = sc_team2.members
  for delsct2 in sct2_users:
    await delsct2.remove_roles(sc_team2)

  await ctx.followup.send("チームからメンバーを削除しました。")