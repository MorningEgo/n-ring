import define as I
@I.tree.command(name="team",
              description="入力したチームのいずれかに割り当てます。半角空白で区切ってチーム名を入力してください。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def team(ctx: I.discord.Interaction, teams: str):
  teamset = teams.split()
  teamd = I.random.choice(teamset)
  await ctx.response.send_message(
    f"{ctx.user.mention}のチームは**{teamd}**だよ！！！\n```\nチーム一覧\n{teamset}```")