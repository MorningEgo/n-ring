import define as I

@I.tree.command(name="test", description="テスト用")
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




	
	else:
		await ctx.followup.send(input)