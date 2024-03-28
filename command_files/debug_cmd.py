import define_first as I

@I.tree.command(name="debug", description="デバッグ用")
@I.discord.app_commands.guilds(
  I.discord.Object(id=I.guildid))
async def test(ctx: I.discord.Interaction,type: str = None , input: str = None):
	if input == "#E6D263":
		await ctx.response.defer(thinking=True,ephemeral=True)
	else:
		await ctx.response.defer(thinking=True,ephemeral=False)

		
	if input is None:
		await ctx.followup.send("ンゴ〜")
	elif input == "20220920":
		await ctx.followup.send(f"Nring!")
	elif input == "面白くない":
		await ctx.followup.send(f"はい")


	elif input == "ping":
		# Ping値を秒単位で取得
		raw_ping = I.client.latency
		# ミリ秒に変換して丸める
		ping = round(raw_ping * 1000)
		await ctx.followup.send(f"pong! {ping}ms")


	elif input == "ngo_data read":
		import json
		file_path = 'nring_storage/ngo_data.json'
		# 読み込み
		with open(file_path, 'r') as __e__:
			ngo_data = json.load(__e__)
		
		await ctx.followup.send(f"```json\n{ngo_data}```")
	

	elif type == "embed":
		input_list = [t.split("===") for t in input.split(',')]
		input_dic = dict(list)
		
		if input_dic["title"]:
			i_title = input_dic["title"]
		else:
			i_title = "None"
		if input_dic["description"]:
			i_description = input_dic["description"]
		else:
			i_description = "None"

		if input_dic["color"]:
			i_color = input_dic["color"]
		else:
			i_color = 0xffffff
		
		embed = I.discord.Embed(
			title = i_title,
			description = i_description,
			color = i_color,
		)

		if input_dic["image"]:
			embed.set_image(url={input_dic["image"]})
		
		if input_dic["thumbnail"]:
			embed.set_thumbnail(url={input_dic["thumbnail"]})

		if input_dic["author"]:
			embed.set_author(url={input_dic["author"]})
		if input_dic[""]:
			embed
		
		await ctx.followup.send(embed=embed)
	
	elif input == "#E6D263":
		await ctx.followup.send("https://colorbase.app/ja/colors/e6d263", ephemeral=True)
	else:
		await ctx.followup.send(input)
