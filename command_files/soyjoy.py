import define as I
@I.tree.command(name="soyjoy")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def sj(ctx: I.discord.Interaction):

  sj = [
    "ストロベリー", "ブルーベリー", "3種のレーズン", "2種のアップル", "コーヒー&ナッツ", "抹茶&マカダミア",
    "アーモンド&チョコレート", "ピーナッツ", "ホワイトチョコ&レモン", "バナナ", "スコーンバープレーン"
  ]
  choice = I.random.choice(sj)
  await ctx.response.send_message(f"SOYJOY{choice}味を食え")