import define_first as I

@I.tree.command(name="debug", description="デバッグ用")
@I.discord.app_commands.guilds(
  I.discord.Object(id=I.guildid))
async def test(ctx: I.discord.Interaction, input: str = None):
	await ctx.response.defer(thinking=True)
	
	if input is None:
		await ctx.followup.send("ンゴ〜")

	elif input == "ping":
		# Ping値を秒単位で取得
		raw_ping = I.client.latency
		# ミリ秒に変換して丸める
		ping = round(raw_ping * 1000)
		await ctx.followup.send(f"pong! {ping}ms")

	elif input == "ngo_data":
		import json
		file_path = 'nring_storage/ngo_data.json'
		# 読み込み
		with open(file_path, 'r') as __e__:
			ngo_data = json.load(__e__)
		
		await ctx.followup.send(f"```json\n{ngo_data}```")

	elif input == "20220920":
		await ctx.followup.send(f"覚えてくれていてありがとう！")
	elif input == "面白くない":
		await ctx.followup.send(f"覚えてろよ")
	else:
		await ctx.followup.send(input)
