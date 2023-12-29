import define_first as I
from define_first import json
from nring_storage.cl.cl_editable import cl_editable
from nring_storage.cl.cl_list import cl_list
from command_files.cl.cl import R

@R.command(name="delete_schedule", description = "予約を取り消します。")
async def delete(ctx: I.discord.Interaction, id: str):
  await ctx.response.defer(thinking=True)

  E = I.discord.Embed(
      color = 0xff0000,
      title = "エラー"
    )
  
  #### id確認 ####
  with open('nring_storage/cl/cl_schedule.json', 'r') as __e__:
      cl_scheduler = json.load(__e__)
	
  for _k, _v in list(cl_scheduler.items()):
    if id == _k:
      rawid = _v['user_id']

      user = I.client.fetch_user(rawid)
      
      myguild = I.client.get_guild(int(I.guildid))
      Owner = myguild.get_role(1038481824109842494)

      try:
        schedule_role = int(_v['schedule_role'])
        editrole = myguild.get_role(schedule_role)
        try:
          schedule_user = int(_v['schedule_user'])
          remove_user = myguild.get_role(schedule_user)
          all_TF = _v['remove_all']        
        
          if ctx.user == user or Owner in ctx.user.roles:  
            T = I.discord.Embed(
              color = 0x5865f2,
              title = "予約を削除しました。"
            )
            
            T.add_field(
              name = "予約ID:",
              value = _k
            )
            T.add_field(
              name = "実行タイプ",
              value= _v['data_type']
            )
            if _v['data_type'] == "edit":
              if _v['schedule_color'] is not None:
                C = I.discord.Embed(
                  color= _v['schedule_color'],
                  title= "削除した予約内容"
                )
              else:
                C = I.discord.Embed(
                  color= editrole.color,
                  title= "削除した予約内容"
                )
              
              C.add_field(
                name = "ロール：",
                value = editrole.mention,
                inline = False
              )
              if _v['schedule_name'] is not None:
                name = _v['schedule_name']
                C.add_field(
                  name = "ロール名：",
                  value = f"{editrole.name}　>>　{name}",
                  inline = False
                )
              else:
                C.add_field(
                  name = "ロール名(このバーの色です)：",
                  value = f"{editrole.name}",
                  inline = False
                )
              
              if _v['schedule_color'] is not None:
                color = _v['schedule_color']
                C.add_field(
                  name = "ロール色(このバーの色です)：",
                  value = f"{editrole.color}　>>　#{hex(int(color, 16))[2:]}",
                  inline = False
                )
              
              if _v['schedule_mentionable'] is not None:
                mentionable = _v['schedule_mentionable']
                C.add_field(
                  name = "メンションの可否",
                  value = f"{editrole.mentionable}　>>　{mentionable}",
                  inline = False
                )
                C.set_author(
                  name = user.name,
                  icon_url = user.avatar.url
                )
            elif _v['data_type'] == "remove":
              C = I.discord.Embed(
                  color= editrole.color,
                  title= "削除した予約内容"
              )
              C.add_field(
                name = "ロール名：",
                value = f"{schedule_role.name}",
                inline = False
              )
              if all_TF is True:
                C.add_field(
                  name = "除去対象",
                  value = "全てのユーザー"
                )
              else:
                C.add_field(
                  name = "除去対象",
                  value = "選択したユーザー"
                )
                C.add_field(
                  name = "対象のユーザー",
                  value = remove_user.mention
                )

            cl_scheduler.pop(_k)
            with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
              json.dump(cl_scheduler, __e__, indent=4)
            break
        
          else:
            T = E
            C = I.discord.Embed(
            color = 0xff0000,
            title = "予約したユーザーではないため、削除をキャンセルしました。"
            )
            break
        except:
          T = E
          C = I.discord.Embed(
            color = 0xff0000,
            title = "除去予定のロールが見つからないため、予約を削除しました。"
          )
            
          cl_scheduler.pop(_k)
          with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
            json.dump(cl_scheduler, __e__, indent=4)
          
          break
      except:
        T = E
        C = I.discord.Embed(
          color = 0xff0000,
          title = "変更予定のロールが見つからないため、予約を削除しました。"
        )
          
        cl_scheduler.pop(_k)
        with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
          json.dump(cl_scheduler, __e__, indent=4)
        
        break
        
  else:
    T = E
    C = I.discord.Embed(
          color = 0xff0000,
          title = "入力されたIDの予約が見つかりません。"
        )
    
    

  await ctx.followup.send(embed=[T,C])