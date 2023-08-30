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

	# 権限のチェック
  if cl_auth == 0:
    await ctx.followup.send("選択したロールの編集権限がありません。\n別のロールを選択するか、権限があるはずのロールを選択している場合は管理者に報告してください。")
  elif cl_auth == 1:
    if schedule is None:
      if user is None:
        
        list = []
        for _ in role.members:
          await _.remove_roles(role, reason=f"{ctx.user.name}による/cl removeの実行")
          list.append(_.mention)

        T = I.discord.Embed(
          color=0x5865f2,
          title=f"ロール：{role.mention}を空にしました。"
        )
        T.add_field(
          name = "削除したメンバー",
          value = '\n'.join(list)
        )
        
        await ctx.followup.send(embed=T)
        
      else:
        # 選択者のみ
        if role in user.roles:
          ...
          
    else:
      # 予約
      ...