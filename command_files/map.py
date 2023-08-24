import define as I
from storages.splatoon3 import maps as sp3_maps
from storages.valorant import maps as valo_maps

class Game(I.enum.Enum):
  VALORANT = "VALORANT"
  Splatoon3 = "Splatoon3"


@I.tree.command(name="map", description="マップをランダムに選択します。")
@I.discord.app_commands.describe(game="どのゲームのマップで抽選するかを選択します。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
#@discord.app_commands.describe(banmap = "除外するマップを選択します。")
#banmap:str = None
async def map(ctx: I.discord.Interaction, game: Game):

	if game == Game.VALORANT:
		
		choice = I.random.choice(valo_maps.map)
		vmap = I.discord.Embed(
			color=0xff3b5a,
      title=f"次のマップは{choice[0]}だよ！")
		vmap.set_image(url=f"{choice[1]}")
		await ctx.response.send_message(embed=vmap)
	elif game == Game.Splatoon3:
		
		choice = I.random.choice(sp3_maps.map)

		embed = I.discord.Embed(
      color=0xf0fc3c,
      title=f"次のマップは{choice[0]}だっ！",
		)
		embed.set_image(url=f"{choice[1]}")
		await ctx.response.send_message(embed=embed)