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
    addng = 500000
  
  ## おしい ##
  elif _ == "ンゴりんご":
    match = "\n\n......？"
    addng = 25000
  elif _ == "んごりんご":
    match = "\n\n......？"
    addng = 25000
  elif _ == "ンゴりンゴ":
    match = "\n\n......？"
    addng = 25000
  elif _ == "ゴンりごん":
    match = "\n\n\N{Clockwise Rightwards and Leftwards Open Circle Arrows}"
    addng = 25000
  elif _ == "んんごごりりンンゴゴ":
    match = "\n\n_`Glitch`_"
    addng = 1000000
  
  ## えぐい ##
  elif _ == "んごりンゴんごりンゴ":
    match = "\n\n\n\n### D  O  U  B  L  E    N    G    O"
    addng = 5000000
  elif _ == "んごりンゴんごりンゴんごりンゴ":
    match = "\n\n\n\n## T  R  I  P  L  E    N    G    O"
    addng = 17000000
  elif _ == "んごりンゴんごりンゴんごりンゴんごりンゴ":
    match = "\n\n\n\n# _N  G  O      P  A  R  T  Y_"
    addng = 340000000

  ## ンゴ違い ##
  elif _ == "んご":
    match = "\n\n......。"
    addng = 500
    
  
  ## ンゴ ##
  elif _ == "ンゴ":
    match = "\n\nンゴ～"
    addng = 500
  elif _ == "ンゴンゴ":
    match = "\n\nンゴッ！？"
    addng = 5000
  
  ## その他 ##
  elif _ == "ゴンゴン":
    match = "\n\nｺﾞｰﾝ..."
    addng = 2500
  elif _ == "ゴ":
    match = "\n\nゴ！"
    addng = 5
  elif _ == "ゴゴ":
    match = "\n\nゴゴ！"
    match = 55
  elif _ == "ゴゴゴ":
    match = "\n\nゴゴゴゴゴゴゴゴ..."
    addng = 555
  elif _ == "りんりん":
    if random.randint(1,20) == 1:
      match = "\n\nプレゼントが欲しいか"
      addng = 7777
    else:
      match = "\n\nクリスマスじゃないよ"
      addng = 2000
  elif _ == "リンリン":
    match = "\n\nスズムシ？"
    addng = 4000

  elif _ == "んんん":
    match = "\n\nう～ん..."
    addng = 1000

  ## りんご ##
  elif _ == "りんご":
    match = "\n\n\N{Green Apple}"
    addng = 1000
  elif _ == "ごんり":
    match = "\n\n\N{Red Apple}"
    addng = 1000
  

  



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
      
    