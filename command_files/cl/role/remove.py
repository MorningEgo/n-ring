import define as I
from define import json
from nring_storage.cl.cl_editable import cl_editable
from nring_storage.cl.cl_list import cl_list
from discord.ext import tasks
from command_files.cl.cl import R

@R.command(name="remove_user", description="全てのユーザーから指定したロールを外します。ユーザーを指定すると、そのユーザーのロールのみを外します。")
async def remove(ctx: I.discord.Interaction, role: I.discord.Role, user: I.discord.Member = None, schedule: str = None):
  await ctx.response.defer(thinking=True)
  JST = I.timezone(I.timedelta(hours=+9), 'JST')
  time = I.datetime.utcnow()
  now = I.datetime.now(JST)
  myguild = I.client.get_guild(int(I.guildid))
  Owner = myguild.get_role(1038481824109842494)
  
  #ロールが編集できるかチェック
  cl_auth = 0
  for _cle in cl_editable:
    if myguild.get_role(int(_cle[0])) in ctx.user.roles:
      if role.id in int(_cle[1]):
        cl_auth = 1
        break
    if Owner in ctx.user.roles:
      cl_auth = 1
      break
  
	# 権限のチェック
  if cl_auth == 0:
    await ctx.followup.send("選択したロールの編集権限がありません。\n別のロールを選択するか、権限があるはずのロールを選択している場合は管理者に報告してください。")
  elif cl_auth == 1:
    if schedule is None:
      list = []
      if user is None:
        for _ in role.members:
          await _.remove_roles(role, reason=f"{ctx.user.name}による/cl remove allの実行")
          list.append(_.mention)
      else: ## 選択者のみ
        if role in user.roles:
          await user.remove_roles(role, reason=f"{ctx.user.name}による/cl remove user_onlyの実行")
          list.append(user.mention)

      T = I.discord.Embed(
          color=0x5865f2,
          title=f"ロール：{role.name}を空にしました。"
        )
      T.add_field(
        name = "削除したメンバー",
        value = '\n'.join(list)
      )
      await ctx.followup.send(embed=T)

    else:  ## 予約
      # 日付が存在しているか
      pt = r'^(?!([02468][1235679]|[13579][01345789])00/02/29)(([0-9]{4}/(01|03|05|07|08|10|12)/(0[1-9]|[12][0-9]|3[01]))|([0-9]{4}/(04|06|09|11)/(0[1-9]|[12][0-9]|30))|([0-9]{4}/02/(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}([02468][048]|[13579][26])/02/29)) ([01][0-9]|2[0-3]):[0-5][0-9]$'
      if I.re.match(pt, schedule):
        scheduletime = I.datetime.strptime(schedule, '%Y/%m/%d %H:%M')
        scheduletime_tz = I.datetime.strptime(schedule + '+0900', '%Y/%m/%d %H:%M%z')
        if now < scheduletime_tz:
          day_error = 0
        else:
          day_error = 2
      else:
        day_error = 1

      # 出力
      if day_error == 0:
        
        nowtimestamp = I.datetime.now(JST).strftime('%Y%m%d%H%M%S%f')
        list = []
        if user is None:
          all_TF = True
        else:
          all_TF = False
        # データ入力
        schedule_data = {
          nowtimestamp : {
            'data_type' :"remove",
            'user_id' : ctx.user.id,
            'schedule_time' : schedule,
            'schedule_role' : role.id,
            'remove_all' : all_TF,
            'schedule_user' : None,
          }
        }
        if user is not None:
          schedule_data[nowtimestamp]['schedule_user'] = user.id
        # 読み込み
        with open('nring_storage/cl/cl_schedule.json', 'r') as __e__:
          cl_scheduler = json.load(__e__)
        # 書き込み
        cl_scheduler.update(schedule_data)
        with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
          json.dump(cl_scheduler, __e__, indent=4)

        embed = I.discord.Embed(
          color = 0xff8aac,
          title = "除去を予約しました！",
          description = "必ず入力した内容を確認してください。\nミスがあった場合は[</cl role delete_schedule:1137310779033526302>]で予約を削除してください。",
          timestamp = time
        )
        embed.set_footer(
          text = f"ID：{nowtimestamp}"
        )
        embed.add_field(
          name = "実行タイプ",
          value = "remove",
          inline = False
        )

        embed.add_field(
          name = "実行日時",
          value = schedule,
          inline = False
        )
        embed.add_field(
          name = "ロール名：",
          value = f"{role.name}",
          inline = False
        )
        if all_TF is True:
          embed.add_field(
            name = "除去対象",
            value = "全てのユーザー"
          )
        else:
          embed.add_field(
            name = "除去対象",
            value = "選択したユーザー"
          )
          embed.add_field(
            name = "対象のユーザー",
            value = user.mention
          )
        await ctx.followup.send(embed=embed)

      elif day_error > 0:
        embed = I.discord.Embed(
            color = 0xff0000,
            title = "エラー",
            description = "入力された予約日時が正しくないようです。",
        )
        if day_error == 1:
          val = "形式とは違う日付・時刻、または存在しない日付・時刻を入力しています。"
        elif day_error == 2:
          val = "現在より前の日付・時刻を入力しています。"
        embed.add_field(
          name = "？・。・？",
          value = val
        )
        embed.set_footer(
          text = ctx.user.name,
          icon_url = ctx.user.avatar.url
        )
        ############# 2 #############
        embed2 = I.discord.Embed(
          color = 0xff0000
        )
        embed2.add_field(
          name = "実行タイプ",
          value= "edit"
        )
        embed2.add_field(
            name = "**[ ! ]** 入力された日時：",
            value = f"{schedule}",
            inline = False
        )
        embed.add_field(
          name = "ロール名：",
          value = f"{role.name}",
          inline = False
        )
        if all_TF is True:
          embed.add_field(
            name = "除去対象",
            value = "全てのユーザー"
          )
        else:
          embed.add_field(
            name = "除去対象",
            value = "選択したユーザー"
          )
          embed.add_field(
            name = "対象のユーザー",
            value = user.mention
          )
        await ctx.followup.send(embeds=[embed,embed2])