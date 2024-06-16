import define_first as I
import random
from command_files.ngold.ngolds import *
from command_files.ngold.embed import *

@I.tree.command(name="ンゴチャレンジ", description="「んごりンゴ」の文字列を揃えるチャレンジです。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def challenge(ctx:I.discord.Interaction, hardmode: bool = None):
  await ctx.response.defer(thinking=True)
  N = ["ん","ご","り","ン","ゴ"]
  A = []
  if hardmode is True:
    for _ in range(random.randint(1, 20)):
      R = random.choice(N)
      A.append(R)
  elif hardmode is None or hardmode is False:
    for _ in range(random.randint(1, 10)):
      R = random.choice(N)
      A.append(R)
  
  _ = ''.join(A)
  match = ""
  addng = 0
  ## かんぺき ##
  if _ == "んごりンゴ":
    match = "\n\n\n\n# _Foo!!!!!!_"
    # 5000 ng
    addng = 5000
  
  ## おしい ##
  elif _ == "ンゴりんご":
    match = "\n\n......？"
    addng = 1000
  elif _ == "んごりんご":
    match = "\n\n......？"
    addng = 1000
  elif _ == "ンゴりンゴ":
    match = "\n\n......？"
    addng = 1000
  elif _ == "ゴンりごん":
    match = "\n\n\N{Clockwise Rightwards and Leftwards Open Circle Arrows}"
    addng = 1000
  elif _ == "んんごごりりンンゴゴ":
    match = "\n\n_`Glitch`_"
    addng = 1000
  
  ## えぐい ##
  elif _ == "んごりンゴんごりンゴ":
    match = "\n\n\n\n### D  O  U  B  L  E    N    G    O"
    # 50000 ng
    addng = 50000
  elif _ == "んごりンゴんごりンゴんごりンゴ":
    match = "\n\n\n\n## T  R  I  P  L  E    N    G    O"
    # 500000 ng
    addng = 500000
  elif _ == "んごりンゴんごりンゴんごりンゴんごりンゴ":
    match = "\n\n\n\n# _N  G  O      P  A  R  T  Y_"
    # 5000000 ng
    addng = 5000000

  ## ンゴ違い ##
  elif _ == "んご":
    match = "\n\n......。"
    addng = 50
    
  
  ## ンゴ ##
  elif _ == "ンゴ":
    match = "\n\nンゴ～"
    addng = 50
  elif _ == "ンゴンゴ":
    match = "\n\nンゴッ！？"
    addng = 50

  ## りんご ##
  elif _ == "りんご":
    match = "\n\n\N{Green Apple}"
    addng = 100
  elif _ == "ごんり":
    match = "\n\n\N{Red Apple}"
    addng = 100
  



  if hardmode is True:
    if not match == "":
      addng = addng *1.5
      ng_add(userid=ctx.user.id,supplier=I.client.user.id,ng=addng)
    mes = f"## {_}！！！{match}\n`ハードモード有効  報酬1.5倍`"
  elif hardmode is None or hardmode is False:
    if not match == "":
      ng_add(userid=ctx.user.id,supplier=I.client.user.id,ng=addng)
    mes = f"## {_}！！！{match}"


  await ctx.followup.send(mes)

  if addng > 0:
    embed = ng_receive_embed(send=I.client.user,receive=ctx.user,value=addng)
    await ctx.followup.send(embed=embed)
      
    