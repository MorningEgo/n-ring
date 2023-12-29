import define_first as I
from nring_storage.valorant import maps

@I.tree.command(name="map", description="マップをランダムに選択します。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.scguild))
async def map(ctx: I.discord.Interaction):
	
	choice = I.random.choice(maps.map)
	vmap = I.discord.Embed(
		color=0xff3b5a,
    title=f"次のマップは{choice[0]}だよ！")
	vmap.set_image(url=f"{choice[1]}")
	await ctx.response.send_message(embed=vmap)