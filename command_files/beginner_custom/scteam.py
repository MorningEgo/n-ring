import define as I
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
    url=
    "https://lh3.googleusercontent.com/fife/APg5EObGWXHtDdmrLVRtgypwv87EzWFuBTMr6IspHFVCVvVhedztnFl8-SiAR4t8iX_Pd_EE8uvK0yurIbAYuu0cVjaplvqwSvXw_mhOzBQ4982UIe-hzxKtkpe-rFCh4gms2bgyP-VAu6UBaAaTPkzvzVp7immitXkTQjFlb_pgNFV30BHuSKLPoTAeUCUVSIoz1LCGfve9qXC1n7Ai7w_y9S10Y5bSDgaqUDroqq6w10e9n4zu6YXowgy96IY2yuyANQ-FGWm87yCPDbgjP-6Y54k5Xm5JjLo5L5sSlYbjkjtcqNTHcNcOtsC0JiVESvHSKs6h9HgWRaVZEfQlhF_9dOJxxjHX581DHdRyiRG98ZXjKUjRTHWcoOa1QfGZTcmk05lGvymTkxT6csdUULaGNXYXIBwigw2ucwVW5_vgi3Xm61jRDZ1bvmi6LwNCS4dUPzTm06XHLb9LqrzKzRI9tpVD_fQf6KDqVeV3og8sl3zQistpVwX-8XVOQkbE5PAF6-IJF0pXh9GMtCkXMm_kBYB7_mjqL2mDVNPGxAtGV_5tfXEnNI3Fkuik5ImuHkuKrxF7h2aWPDM7VUnbXg2nPeAY-a40ANsnbOFWeq5dYHXLO3Q9WUjAil8y8LuaqNQ43nXZb0LbUaC73kvim1Pum3oPkYLJEdu0EK2tICcUj-DZabzXLXmqFKgByHUNFcyGBvYF08WgUlRKwpUvZg9hi0n-D3vBFgVP--1lSwUfiK-UXKw5_XgHnMOOmzEY-W5T-I3L6GTbAfd2r0alZBtlxejYVJT0Eson1jV44LNLyo45PoKuSmbCig4wSyUHbIw3XjSbZF87GO3VLBM8hyO28APvo1FIMDe2JEhvyOF_MKjm_-Cpj3DDtmhREPXUrTpsfRU6HlA5ABrm-kZe6tZaQpYCOOjVKZuZOwW1gkhNOl_oQhXstjSmYuzGF1u3wsmeePZrmY5qK6M_3UjEiO1bDCufNmdyqooc1W5Y_7AaV26ZoHy0YO9RmU0MJKtnDW5Vq58n-enSbjC7WPFTtCcx8mpesK6d2L80ZA2pDh7TkJES5N4CzTjdwuxN2UsAta2EISt-CHnkz3k3NIuf71bHlBBy9YQOoaMXMIpoJzvGxR9-xOF5s4b-AJ9Ne_ZjWEp2Flbs0M5KFIzOmWeBgfO7Csqc3n4d4HHZY0Ue9_xS1P8TXZYkXiIqvRYEzrW0CPOnuhB7hXrPHVg9eIEbTo_QLgSL8SDCHvVL3Z1l1a7dpsgZLzl26TiXUWQOmEiauXnVUQgigzhMbF9dDZFrKZPe5tncsdO9Ttc2jVvaD8BqqjVsD7M8cPatHUoFnFBnZMz8hP50VxsTuVg-lBjFp4Veugjt2xVYpKJQxPXazFN4xlu_PtzEYPfdhHvDrwNTBRtZAW-9rDBMPjmQAGt1B_qACABzITiZ5k-j5DBq4Mh_MQ774KPa6JD8Cj2SSQyGyxN6mSmxk5sK1UImqiMzVk_X_ZesAp-wdSv9s0EQARq4IMMMXLNKLPuZk5vyaHDQ6IZ6N7P2MHH2SqrmSEJ9fafKoxmrO4CQ6xv87MZ2gDK5rc_9lCDj1A7-zcWxETztX0He4N0GEaUupLXR2tsfyCsdDkt-I4EoMcPXfagw4BXr7vqFD-7SPGikE56zHdJqX0hiuOR0ZDEMEv0fKq4-RK64em5Yt3Oz3LlbCcpzOAg3XZAu_jSqfZsv1pA"
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