import define_first as I
import json
from nring_storage.cl.cl_editable import cl_editable
from nring_storage.cl.cl_list import cl_list
from discord.ext import tasks
from command_files.cl.cl import R

@R.command(name="edit", description="ロールの編集、編集予約")
@I.discord.app_commands.describe(
	editrole = "編集するロールを選択",
	name = "ロール名の変更(100字まで)",
	color = "ロール色の変更(【0xffffff】の形)",
	mentionable = "ロールに対するメンションの可否を変更",
	schedule = "変更を予約(【2023/01/01 00:00】の形) 存在しない日付と前の日付を入れないでください、ぶっ飛ばします"
)
async def edit(ctx: I.discord.Interaction, editrole: I.discord.Role, name: str = None, color: int = None, mentionable: bool = None, schedule: str = None):
	await ctx.response.defer(thinking=True)
	JST = I.timezone(I.timedelta(hours=+9), 'JST')
	now = I.datetime.now(JST)
	oldname = editrole.name
	oldcolor = editrole.color
	oldmentionable = editrole.mentionable
	
	
	
	# CLかどうかチェック
	cl_auth = 0
	for clr in cl_list:
		for urole in ctx.user.roles:
			if urole.id == clr[1]:
				cl_auth = 1
				
	# さてはオメー、権限持ってないな？
	if cl_auth == 0:
		await ctx.followup.send("コマンドの使用権限がありません。使用するには[カテゴリリーダーに立候補](https://discord.com/channels/1021500432578789557/1091440978482700349)してください。")
	
	elif cl_auth == 1:
		#ロールが編集できるかチェック
		for _cle in cl_editable:
			for urole in ctx.user.roles:
				if int(_cle[0]) == urole.id:
					cl_auth = 2
			
			if cl_auth == 2:
				for _cle_r in _cle[1]:
					if editrole.id == int(_cle_r):
						cl_auth = 3
		
		for urole in ctx.user.roles:
			if 1038481824109842494 == urole.id:
				#cl_auth = 3
				print("owner auth.")
				
		# 権限のチェック
		if cl_auth == 1:
			await ctx.followup.send(f"認証に失敗しました`(cl_auth({cl_auth})の通過に失敗しました)`。")
		elif cl_auth == 2:
			await ctx.followup.send("選択したロールの編集権限がありません。\n別のロールを選択するか、権限があるはずのロールを選択している場合は管理者に報告してください。")
		elif cl_auth == 3:
			editer = []
			# 内容の有無
			if name is not None:
				editer.append("n")
				print("1")
			if color is not None:
				editer.append("c")
				setcolor = color
				print("2")
			else:
				setcolor = oldcolor
			if mentionable is not None:
				editer.append("m")
				print("3")
			# 何も変更せんのかい
			if editer is None:
				await ctx.followup.send("変更内容を設定してください。")
				print("4")
			# 変更するっぽい
			else:
				print("5")
				# 即時実行
				if schedule is None:
					day_error = 0
					print("6")
					
				# 予約登録
				else:
					print("6-1")
					
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
					if schedule is None:
						if "n" in editer:
							await editrole.edit(name = name)
							print("7")
						if "c" in editer:
							await editrole.edit(color = color)
							print("8")
						if "m" in editer:
							await editrole.edit(mentionable = mentionable)
							print("9")
						print("11")
						embed = I.discord.Embed(
							color = setcolor,
							title = "ロールの設定を変更しました！",
							description = "必ず入力した内容を確認してください。\nミスがあった場合はもう一度設定してください。",
							timestamp = now
						)
					else:
						nowtimestamp = I.datetime.now(JST).strftime('%Y%m%d%H%M%S%f')
						print("12")
						# データ入力
						schedule_data = {
							nowtimestamp : {
								'data_type' :"edit",
								'user_id' : ctx.user.id,
								'schedule_time' : schedule,
								'schedule_role' : editrole.id,
								'schedule_name' : None,
								'schedule_color' : None,
								'schedule_mentionable' : None
							}
						}
						print("13")
						# 置換
						if "n" in editer:
							schedule_data[nowtimestamp]['schedule_name'] = name
							print("14")
						if "c" in editer:
							schedule_data[nowtimestamp]['schedule_color'] = format(color, '#x')
							print("15")
						if "m" in editer:
							schedule_data[nowtimestamp]['schedule_mentionable'] = mentionable
							print("16")
						# 読み込み
						with open('nring_storage/cl/cl_schedule.json', 'r') as __e__:
							cl_scheduler = json.load(__e__)
							print("17")
						# 書き込み
						cl_scheduler.update(schedule_data)
						print("18")
						with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
							json.dump(cl_scheduler, __e__, indent=4)
							print("19")
						print("20")
						embed = I.discord.Embed(
							color = setcolor,
							title = "変更を予約しました！",
							description = "必ず入力した内容を確認してください。\nミスがあった場合は[</cl role delete_schedule:1137310779033526302>]で予約を削除してください。",
							timestamp = now
						)
						embed.add_field(
							name = "実行タイプ",
							value= "edit"
						)
						embed.add_field(
							name = "実行日時",
							value = schedule,
							inline = False
						)
						embed.set_footer(
							text = f"ID：{nowtimestamp}"
						)
					if name is not None:
						print("21")
						embed.add_field(
							name = "ロール名：",
							value = f"{oldname}　>>　{name}",
							inline = False
						)
					else:
						print("22")
						embed.add_field(
							name = "ロール名：",
							value = f"{oldname}",
							inline = False
						)
					if color is not None:
						print("23")
						embed.add_field(
							name = "ロール色(このバーの色です)：",
							value = f"{oldcolor}　>>　#{hex(color)[2:]}",
							inline = False
						)
					if mentionable is not None:
						print("24")
						embed.add_field(
							name = "メンションの可否",
							value = f"{oldmentionable}　>>　{mentionable}",
							inline = False
						)
					print("25")
					embed.set_author(
						name = ctx.user.name,
						icon_url = ctx.user.avatar.url
					)
					print("26")
					await ctx.followup.send(embed=embed)

				
				elif day_error > 0:
					embed = I.discord.Embed(
							color = 0xff0000,
							title = "エラー",
							description = "入力された予約日時が正しくないようです。ぶっ飛ばすって言わなかった？",
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
						color = setcolor,	
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
					if name is not None:
						embed2.add_field(
							name = "ロール名：",
							value = f"{oldname}　>>　{name}",
							inline = False
						)
					else:
						embed2.add_field(
							name = "ロール名：",
							value = f"{oldname}",
							inline = False
						)
					if color is not None:
						embed2.add_field(
							name = "ロール色(このバーの色です)：",
							value = f"{oldcolor}　>>　#{hex(color)[2:]}",
							inline = False
						)
					if mentionable is not None:
						embed2.add_field(
							name = "メンションの可否",
							value = f"{oldmentionable}　>>　{mentionable}",
							inline = False
						)
					await ctx.followup.send(embeds=[embed,embed2])


