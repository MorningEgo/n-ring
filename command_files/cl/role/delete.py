import define as I
from define import json
from nring_storage.cl.cl_editable import cl_editable
from nring_storage.cl.cl_list import cl_list
from discord.ext import tasks
from command_files.cl.cl import R

@R.command(name="delete_schedule", description = "予約した変更を取り消します。")
async def delete(ctx: I.discord.Interaction, id: str):
	await ctx.response.defer(thinking=True)
	#### id確認 ####
	with open('nring_storage/cl/cl_schedule.json', 'r') as __e__:
			cl_scheduler = json.load(__e__)
	
	for _k, _v in list(cl_scheduler.items()):
		if id == _k:
			rawid = _v['user_id']
			if I.client.fetch_user(rawid):
				user = I.client.fetch_user(rawid)

				if ctx.user == user:
					T = I.discord.Embed(
						color = 0x0000ff,
						title = "予約を削除しました。"
					)
					# 予約してた内容を表示 C =
					cl_scheduler.pop(_k)
					with open('nring_storage/cl/cl_schedule.json', 'w') as __e__:
						json.dump(cl_scheduler, __e__, indent=4)
	
	await ctx.followup.send("ンゴ～")