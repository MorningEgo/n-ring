import define_first as I
@I.client.event
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def on_message(message):
	if message.author.bot:
		return
	elif I.client.user in message.mentions:
		if "おはよう" in message.content or "ohayou" in message.content:
			await message.reply(f"おは～")
		elif "おやすみ" in message.content or "oyasumi" in message.content:
			await message.reply(f"おや～")
		elif "カス" in message.content or "かす" in message.content or "kasu" in message.content:
			await message.reply(f"今カスって言った！？！？！？！？！？！？！？？！！？？！？！？！？？？！？！？！？！？！？！？！？？！")
		elif "ばか" in message.content or "バカ" in message.content or "baka" in message.content:
			await message.reply(f"今バカって言った！？！？？！？！？！？？！？！？！？？！？！？！？！？！？！？！？！？！？！？！？？！")
		elif "しね" in message.content or "死ね" in message.content or "タヒね" in message.content or "ﾀﾋね" in message.content:
			await message.reply(f"そっか")
		elif "ンゴ" in message.content or "んご" in message.content or "ngo" in message.content:
			await message.reply(f"ンゴ～")
		elif "んごりンゴ" in message.content:
			ngo = [
			"ンゴだよ～",
			"ンゴで～す",
			"ンゴいるンゴ",
			"ンゴ～",
			"ンゴですが、なにか",
			"はいンゴです",
			"やっほ～",
			f"{message.author.nick}じゃん、どしたの",
			"呼んだ？",
			"よっす～",
			]
		
		else:
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
			choice_games2 = I.random.choice(games)
			choice_games3 = I.random.choice(games)

			ngo = [
			"ンゴだよ～",
			"ンゴで～す",
			"ンゴいるンゴ",
			"ンゴ～",
			"ンゴですが、なにか",
			"はいンゴです",
			f"{message.author.nick}じゃん、どしたの",
			f"{message.author.nick}のンボムﾐｮミの部分",
			f"{message.author.nick}・D・ロジャーじゃん、どこに置いてきたの",
			f"{message.content}だァ？そんなもの知らないよ！",
			f"たしかに、{message.author.nick}はそうだよな",
			f"{message.content}についての情報は多分ない...いやあるかも...ちょっと探しとく",
			f"{message.content}か～～そこになければないよ",
			"うるさーい！！！",
			"Chillして",
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
			"ﾋﾟﾖ～～",
			f"うーんゲームスロットチャレンジ！！！！！！！！！\n\n{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！",
			"え、それ明日じゃダメ...？",
			"おっけ～",
			]
			choice = I.random.choice(ngo)
			await message.reply(f"{choice}")