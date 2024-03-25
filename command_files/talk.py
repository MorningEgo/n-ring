import define_first as I
@I.client.event
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def on_message(message):
	if message.author.bot:
		return
	elif I.client.user in message.mentions:
		games = [
			"VALORANT",
			"OverWatch",
			"Apex",
			"マイクラ",
			"ざ森",
			"原神",
			"スプラ",
			"リーサル",
			"スマブラ",
			"GTA",
			"ぷよテト",
			"ボドゲ",
			"カタン",
			"タルコフ",
			"ンゴチャレンジ"
		]
		choice_games = I.random.choice(games)

		ngo = [
		"ンゴだよ～",
		"ンゴで～す",
		"ンゴいるンゴ",
		"ンゴ～",
		""
		f"{message.author.nick}じゃん、どしたの",
		f""
		"やっほ～",
		"むむ",
		"なんだァ...？テメェ...",
		f"{choice_games}やらない？やらんか...",
		f"{choice_games}、最近ハマってるんだよね",
		"わかる",
		"呼んだ？",
		"呼ばれた気がしたんだよね、ココで",
		"見てるよ",
		"眠い！！！！！！！！！！！寝かせろ！！！！！！！！！！！！！！！！！！！！！！！！！！",
		"＠ ～＠)?",

		]
		choice = I.random.choice(ngo)
		await message.reply(f"{choice}")