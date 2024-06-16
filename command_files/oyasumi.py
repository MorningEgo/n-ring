import define_first as I
from command_files.ngold.ngolds import *
from command_files.ngold.embed import *

@I.tree.command(name="おやすみ", description="寝ます　はよ寝ろ")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
@I.discord.app_commands.checks.cooldown(1, 3600)
async def oyasumi(ctx:I.discord.Interaction, comment: str = None):
	await ctx.response.defer(thinking=True)
	
	file = I.discord.File("pictures/cmd_oyasumi.png", filename="image.png")
	
	weekjp = ["月", "火", "水", "木", "金", "土", "日"]
	JST = I.timezone(I.timedelta(hours=+9), 'JST')
	now = I.datetime.now(JST)
	Week = I.datetime.weekday(now)
	weekday = weekjp[Week]
	nowstr = I.datetime.strftime(now, f'%m月%d日({weekday}) %H時%M分%S秒')
	E = I.discord.Embed(title="ねます", description=f"{nowstr}に一日を終えました",color=0x1810c7)
	E.set_thumbnail(url="attachment://image.png")
	username = ctx.user.nick
	if username is None:
		username = ctx.user.name
	E.set_author(name=username, icon_url=ctx.user.display_avatar.url)
	if comment is not None:
		E.add_field(name="ひとこと", value=comment)
	##### user_data #####
	# # 読み込み
	#   with open('nring_storage/n_users/user_data.json', 'r') as __e__:
	#        = json.load(__e__)
	#   oyasumi_count = _v[oyasumi_count] + 1
	# 書き込み #
	#####################
	await ctx.followup.send(file=file, embed=E)

	ng_add(userid=ctx.user.id,supplier=I.client.user.id,ng=30)