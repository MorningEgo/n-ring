import define as I
import random

@I.tree.command(name="ンゴチャレンジ", description="「んごりンゴ」の文字列を揃えるチャレンジです。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def challenge(ctx:I.discord.Interaction):
  await ctx.response.defer(thinking=True)
  N = ["ん","ご","り","ン","ゴ"]
  A = []
  for _ in range(random.randint(1, 20)):
    R = random.choice(N)
    A.append(R)
  
  _ = ''.join(A)
  match = ""
  if _ == "んごりンゴ":
    match = "\n\n**Foo！！！**"
    #2000NP
  elif _ == "ンゴりんご":
    match = "\n\n......？"
  elif _ == "んごりんご":
    match = "\n\n......？"
  elif _ == "ンゴりンゴ":
    match = "\n\n......？"
  elif _ == "んごりンゴんごりンゴ":
    match = "\n\n\n\n### D  O  U  B  L  E    N    G    O"
  elif _ == "んごりンゴんごりンゴんごりンゴ":
    match = "\n\n\n\n### T  R  I  P  L  E    N    G    O"
  elif _ == "んごりンゴんごりンゴんごりンゴんごりンゴ":
    match = "\n\n\n\n# _N  G  O      P  A  R  T  Y_"
  elif _ == "ンゴ":
    match = "\n\nンゴ〜"
  elif _ == "りんご":
    match = "\n\n\N{Green Apple}"
  
  await ctx.followup.send(f"## {_}！！！{match}")