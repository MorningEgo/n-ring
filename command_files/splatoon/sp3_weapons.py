import define as I
from nring_storage.splatoon3 import _temp as t
from nring_storage.splatoon3 import weapons as w

class fil(I.enum.Enum):
  追加 = "追加"
  除外 = "除外"
  使わない = "使わない"
  一覧を表示 = "一覧を表示"

@I.tree.command(name="sp3_wpn", description="Splatoon3の武器の中から一つ武器を抽選します。")
@I.discord.app_commands.describe(
  filter_setting="フィルターを「追加・除外・使わない」のいずれかに設定してください。また、フィルター一覧も確認できます。",
  filters="ブキ種やサブ・スペシャルの名前を入れてください。複数入れる場合は半角空白で区切ってください。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def rwe(ctx: I.discord.Interaction,
              filter_setting: fil,
              filters: str = None):
  import random
  
  rwe = []
  error = 0
  await ctx.response.defer(thinking=True)

  if filter_setting == fil.使わない:
    rwe = w.sp3_wpn_all
    f = None

  elif filter_setting == fil.一覧を表示:
    l = []
    for _ in t.sp3_temp:
      l.append(_[3])
    strl = "\n* ".join(l)
    await ctx.followup.send(f"> **フィルター一覧**\n```md\n* {strl}```")
    print(f"> **フィルター一覧**\n```md\n* {strl}```")
    error = -1
  else:
    if not filters is None:  # フィルターが設定されているとき
      if " " in filters:
        f = filters.replace(" ", ",")
        sellects = filters.split()
        if filter_setting == fil.追加:  ## 追加
          for wpn_ph in sellects:
            for wpn_temp in t.sp3_temp:
              if wpn_ph == wpn_temp[3]:
                for wpn_ in w.sp3_wpn_all:
                  if wpn_ph == wpn_[0]:
                    rwe.append(wpn_)
                  elif wpn_ph == wpn_[2]:
                    rwe.append(wpn_)
                  elif wpn_ph == wpn_[3]:
                    rwe.append(wpn_)
          if rwe == []:
            error = 3
        elif filter_setting == fil.除外:  ## 除外
          rwe = w.sp3_wpn_all
          drwe = rwe
          for wpn_ph in sellects:
            for wpn_ in w.sp3_wpn_all:
              if wpn_ph == wpn_[0]:
                rwe.remove(wpn_)
              elif wpn_ph == wpn_[2]:
                rwe.remove(wpn_)
              elif wpn_ph == wpn_[3]:
                rwe.remove(wpn_)
          if rwe == drwe:
            error = 3
      else:
        f = filters
        wpn_ph = filters
        if filter_setting == fil.追加:
          for wpn_temp in t.sp3_temp:
            if wpn_ph == wpn_temp[3]:
              for wpn_ in w.sp3_wpn_all:
                if wpn_ph == wpn_[0]:
                  rwe.append(wpn_)
                elif wpn_ph == wpn_[2]:
                  rwe.append(wpn_)
                elif wpn_ph == wpn_[3]:
                  rwe.append(wpn_)
          if rwe == []:
            error = 3
        elif filter_setting == fil.除外:
          rwe = w.sp3_wpn_all
          drwe = rwe
          for wpn_ in w.sp3_wpn_all:
            if wpn_ph == wpn_[0]:
              rwe.remove(wpn_)
            elif wpn_ph == wpn_[2]:
              rwe.remove(wpn_)
            elif wpn_ph == wpn_[3]:
              rwe.remove(wpn_)

          if rwe == drwe:
            error = 3
    else:  # フィルターが設定されていないとき
      rwe = w.sp3_wpn_all

  #######################
  if error == 0:
    choice = random.choice(rwe)
    embed = I.discord.Embed(
      color=0xf0fc3c,
      title=f"次の{ctx.user.display_name}のブキは「**{choice[1]}**」だ！")
    embed.add_field(name="サブウェポン", value=f"{choice[2]}", inline=False)
    embed.add_field(name="スペシャル", value=f"{choice[3]}", inline=False)
    if f is not None:
      embed.set_footer(text=f"{filter_setting.value}：{f}")

    if I.urllib.request.urlopen(choice[4]):
      embed.set_thumbnail(url=f"{choice[4]}")
    else:
      print("Image not found" + choice[4])
    await ctx.followup.send(embed=embed)
  elif error == -1:
    pass
  else:
    if error == 1:
      _e = "フィルター設定が正しくないようです。コマンドをもう一度確認し、直らない場合は管理者を問い詰めてください。"
    elif error == 2:
      _e = "入力したブキ種・サブ・スペシャルウェポンのいずれかは存在しないか、正しくない名称です。コマンドをもう一度確認し、直らない場合は管理者を問い詰めてください。"
    elif error == 3:
      _e = "なんかうまくフィルターがかけられなかったみたい！！そのフィルター、ミスってたりしない？"
    elif error == 4:
      _e = "Bot内で処理に失敗しました。多分ブキ一覧が正しく設定されていないので管理者を問い詰めてください。"

    await ctx.followup.send(f"**Error：**{_e}")