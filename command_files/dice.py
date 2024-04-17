import define_first as I
@I.tree.command(name="dice", description="サイコロを振ります。")
@I.discord.app_commands.describe(
  rolls="サイコロを何回振るか。",
  sides="何面サイコロを使用するか。",
  hope="何を考えながら振るか。オプションを付けない場合は時の流れに身を任せます。",
  secret="他人に見せないようにサイコロを振るか。オプションを付けない場合はFalse扱いになります。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def dice(ctx: I.discord.Interaction,
               rolls: int,
               sides: int,
               hope: str = None,
               secret: bool = None):
  await ctx.response.defer(thinking=True)

  if rolls == 0:
    await ctx.followup.send("サイコロも振れない人は一歩踏み出すこともできないんだよ")
  elif sides == 0:
    await ctx.followup.send("サイコロも振れない人は一歩踏み出すこともできないんだよ")
  elif sides == 1:
    await ctx.followup.send("ズルはよくないよ")
  else:
    I.random.seed(a= hope, version=2)
    rolling = I.discord.Embed(title=f"ダイスロール！ {rolls}D{sides}！！！", )
    if rolls == 1:
      rolling.add_field(name=f"{I.random.randint(1,sides)}",
                        value="",
                        inline=True)
    else:
      all = 0
      dl = []
      for _ in range(rolls):
        rl = _ + 1
        res = I.random.randint(1, sides)
        all = all + res
        dl.extend(f"**{rl}回目**\n{res}\n\n")

      if rolls <= 30:

        rolling.add_field(name="なにがでたかな", value=f"{''.join(dl)}", inline=True)
      elif rolls >= 31:
        rolling.add_field(name="なにがでたかな",
                          value="多すぎるので省略！\nいっぱい！",
                          inline=True)
      rolling.add_field(name="合計", value=f"{all}", inline=False)
    if secret == True:
      await ctx.followup.send(embed=rolling, ephemeral=True)
    else:
      await ctx.followup.send(embed=rolling, ephemeral=False)