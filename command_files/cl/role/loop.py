import define as I
import json
from nring_storage.cl.cl_editable import cl_editable
from nring_storage.cl.cl_list import cl_list
from discord.ext import tasks
from command_files.cl.cl import R

@tasks.loop(seconds=60)
async def cl_loop():
	#channel = I.client.get_channel(1021687560436727808)
	JST = I.timezone(I.timedelta(hours=+9), 'JST')
	now = I.datetime.now(JST).strftime('%Y/%m/%d %H:%M:%S')
	time = I.datetime.utcnow()
	print(now)
	# 読み込み
	with open('nring_storage/cl/cl_schedule.json', 'r') as __e__:
		cl_scheduler = json.load(__e__)
	for _k, _v in list(cl_scheduler.items()):
		#scheduletime = str(_v['schedule_time'])
		#scheduletime = I.datetime.strptime(___, "%Y/%m/%d %H:%M")
		if now == _v['schedule_time'] and _v['data_type'] == "edit":
			print(f"execute: {_k}")
			gid = int(I.guildid)
			myguild = I.client.get_guild(gid)
			
			rawid = _v['user_id']
			schedule_role = int(_v['schedule_role'])
			
			try:
				channel = I.client.fetch_channel(1138096620370673705)
			except:
				try:
					channel = I.client.fetch_channel(1021687560436727808)
				except:
					cnl = False
				else:
					cnl = True
			else:
				cnl = True

			finally:
				try:
					editrole = myguild.get_role(schedule_role)
					
				except:
					print('\033[31m' + 'Error: Role Not Found' + '\033[0m')
					cl_scheduler.pop(_k)
					with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
						json.dump(cl_scheduler, __e__, indent=4)
						
				else:
					try:
						user = I.client.get_user(rawid)
						
					except:
						print('\033[31m' + 'Error: Missing User' + '\033[0m')
						cl_scheduler.pop(_k)
						with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
							json.dump(cl_scheduler, __e__, indent=4)
							
					else:
						oldname = editrole.name
						oldcolor = editrole.color
						oldmentionable = editrole.mentionable
						color = _v['schedule_color']
						if _v['schedule_color'] is not None:
							setcolor = int(color, 16)
						else:
							setcolor = oldcolor
	
						embed = I.discord.Embed(
							color= setcolor,
							title = "予約された変更を実行しました。",
							timestamp = time
						)
						embed.add_field(
							name = "実行タイプ",
							value= "edit"
						)
						embed.add_field(
							name = "変更されたロール：",
							value = editrole.mention
						)
						if _v['schedule_name'] is not None:
							name = _v['schedule_name']
							await editrole.edit(name = name)
							embed.add_field(
								name = "ロール名：",
								value = f"{oldname}　>>　{name}",
								inline = False
							)
						else:
							embed.add_field(
								name = "ロール名：",
								value = f"{oldname}",
								inline = False
							)
						if _v['schedule_color'] is not None:
							color = _v['schedule_color']
							await editrole.edit(color = int(color, 16))
							embed.add_field(
								name = "ロール色(変更後はこのバーの色です)：",
								value = f"{oldcolor}　>>　#{hex(int(color, 16))[2:]}",
								inline = False
							)
						if _v['schedule_mentionable'] is not None:
							mentionable = _v['schedule_mentionable']
							await editrole.edit(mentionable = mentionable)
							embed.add_field(
								name = "メンションの可否",
								value = f"{oldmentionable}　>>　{mentionable}",
								inline = False
							)
						embed.set_author(
							name = user.name,
							icon_url = user.avatar.url
						)
						embed.set_footer(
							text = f"ID：{_k}"
						)
						cl_scheduler.pop(_k)
						with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
							json.dump(cl_scheduler, __e__, indent=4)
	
						if cnl is True:
							await channel.send(embed = embed)
						print('\033[32m'+f'Success: Role Edited. {editrole.id}'+'\033[0m')
		elif now == _v['schedule_time'] and _v['data_type'] == "remove":
			print(f"execute: {_k}")
			gid = int(I.guildid)
			myguild = I.client.get_guild(gid)
			
			rawid = _v['user_id']
			schedule_role = int(_v['schedule_role'])
			
			try:
				channel = I.client.fetch_channel(1138096620370673705)
			except:
				try:
					channel = I.client.fetch_channel(1021687560436727808)
				except:
					cnl = False
				else:
					cnl = True
			else:
				cnl = True

			finally:
				try:
					editrole = myguild.get_role(schedule_role)
					
				except:
					print('\033[31m' + 'Error: Role Not Found' + '\033[0m')
					cl_scheduler.pop(_k)
					with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
						json.dump(cl_scheduler, __e__, indent=4)
						
				else:
					try:
						user = I.client.get_user(rawid)
						
					except:
						print('\033[31m' + 'Error: Missing User' + '\033[0m')
						cl_scheduler.pop(_k)
						with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
							json.dump(cl_scheduler, __e__, indent=4)
			