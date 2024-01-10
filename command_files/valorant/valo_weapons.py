import define_first as I


class WeaponType(I.enum.Enum):
  全ての武器 = "全ての武器"
  セカンダリ = "セカンダリ"
  プライマリ = "プライマリ"
  ナイフとセカンダリ = "ナイフとセカンダリ"
  ナイフとプライマリ = "ナイフとプライマリ"


@I.tree.command(name="v_wpn", description="VALORANTの武器の中から一つ武器を抽選します。")
@I.discord.app_commands.describe(weapontype="抽選モードを変更します。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def wpn(ctx: I.discord.Interaction, weapontype: WeaponType):

  v_sec = [
    "クラシック", 
    "ショーティー", 
    "フレンジー", 
    "ゴースト", 
    "シェリフ"
  ]

  v_pri = [
    "スティンガー", 
    "スペクター", 
    "バッキー", 
    "ジャッジ", 
    "ブルドッグ", 
    "ガーディアン", 
    "ファントム", 
    "ヴァンダル",
    "マーシャル", 
    "アウトロー",
    "オペレーター", 
    "アレス", 
    "オーディン"
  ]

  v_kni = ["ナイフ"]

  if weapontype == WeaponType.全ての武器:
    wpn = v_sec + v_pri + v_kni
  elif weapontype == WeaponType.セカンダリ:
    wpn = v_sec
  elif weapontype == WeaponType.ナイフとセカンダリ:
    wpn = v_sec + v_kni
  elif weapontype == WeaponType.プライマリ:
    wpn = v_pri
  elif weapontype == WeaponType.ナイフとプライマリ:
    wpn = v_pri + v_kni

  choice = I.random.choice(wpn)
  embed = I.discord.Embed(
    color=0xff3b5a,
    title=f"次の{ctx.user.name}の武器は**{choice}**だよ！"
  )
  embed.set_footer(text=f"抽選タイプ：{weapontype.value}")
  await ctx.response.send_message(embed=embed)
