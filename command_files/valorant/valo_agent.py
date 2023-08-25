import define as I
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

  all = [
    "KAY/O", "アストラ", "ヴァイパー", "オーメン", "キルジョイ", "ゲッコー", "サイファー", "ジェット", "スカイ",
    "セージ", "ソーヴァ", "チェンバー", "ネオン", "ハーバー", "フェイド", "フェニックス", "ブリーチ", "ブリムストーン",
    "ヨル", "レイズ", "レイナ"
  ]
  due = ["ジェット", "ネオン", "フェニックス", "ヨル", "レイズ", "レイナ"]
  con = ["アストラ", "ヴァイパー", "オーメン", "ハーバー", "ブリムストーン"]
  ini = ["KAY/O", "ゲッコー", "スカイ", "ソーヴァ", "フェイド", "ブリーチ"]
  sen = ["キルジョイ", "サイファー", "セージ", "チェンバー"]
  role = ["デュエリスト", "イニシエーター", "コントローラー", "センチネル"]

  if mode == Mode.デュエリストのみ:
    agt = due
    cond = cond_head + "デュエリスト" + cond_foot

  elif mode == Mode.コントローラーのみ:
    agt = con
    cond = cond_head + "コントローラー" + cond_foot

  elif mode == Mode.イニシエーターのみ:
    agt = ini
    cond = cond_head + "イニシエーター" + cond_foot

  elif mode == Mode.センチネルのみ:
    agt = sen
    cond = cond_head + "センチネル" + cond_foot
  else:
    agt = all
    cond = ""

  choice = I.random.choice(agt)
  r_role = I.random.choice(role)

  if mode == Mode.ロールで抽選:
    mes = f"次の{ctx.user.mention}のロールは「**{r_role}**」だよ！{cond}"
  else:
    mes = f"次の{ctx.user.mention}のエージェントは「**{choice}**」だよ！{cond}"

  await ctx.response.send_message(f"{mes}")