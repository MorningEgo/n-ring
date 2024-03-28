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
		choice_games2 = I.random.choice(games)
		choice_games3 = I.random.choice(games)
		choice_games4 = I.random.choice(games)
		choice_games5 = I.random.choice(games)

		rps_raw = [
			"グー",
			"チョキ",
			"パー",
		]
		rps = I.random.choice(rps_raw)
		if ("？" in message.content or "?" in message.content) and "しってる" in message.content or "知ってる" in message.content or "しらない" in message.content or "知らない" in message.content:
			ngo = [
				"知ってるよ",
				"知ってるかも",
				"知ってるに決まってんだろ！！！！！！",
				"知っ.....てる",
				"聞いたことなら",
				"どっかできいた",
				"どっかでみた",
				"だれかにきいた",
				"それすき",
				"それきらい",
				"知らんな",
				"しらないかも",
				"しらん",
				"しるか",
				"知ってるわけないだろ！！！！！！！！"
			]
			choice = I.random.choice(ngo)
			await message.reply(f"choice")

		elif "おはよう" in message.content or "ohayou" in message.content:
			ngo = [
				"おは～",
				"おはよ～",
				"おはも～にん～",
				"朝...朝か...？",
				"まだねかせて",
				"今日も一日ってやつか",
				"今日は何するの",
			]
			choice = I.random.choice(ngo)
			await message.reply(f"choice")

		elif "おやすみ" in message.content or "oyasumi" in message.content:
			ngo = [
				"おや～",
				"おやすみ～",
				"はよねろ",
				"まだねるな",
				"もうねるの？",
				"おつかれさま",
				"今日はどうだった？",
			]
			choice = I.random.choice(ngo)
			await message.reply(f"choice")

		elif "カス" in message.content or "かす" in message.content or "kasu" in message.content:
			await message.reply(f"今カスって言った！？！？！？！？！？！？！？？！！？？！？！？！？？？！？！？！？！？！？！？！？？！")

		elif "ばか" in message.content or "バカ" in message.content or "baka" in message.content:
			await message.reply(f"今バカって言った！？！？？！？！？！？？！？！？！？？！？！？！？！？！？！？！？！？！？！？！？？！")

		elif "しね" in message.content or "死ね" in message.content or "タヒね" in message.content or "ﾀﾋね" in message.content:
			await message.reply(f"そっか")

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
			choice = I.random.choice(ngo)
			await message.reply(f"{choice}")

		elif "ンゴ" == message.content or "んご" == message.content or "ngo" == message.content:
			await message.reply(f"ンゴ～")

		elif "つらい" in message.content or "辛い" in message.content:
			ngo = [
				"むりしないで",
				"がんばれ",
				"なんとかなれ",
				"ねよう",
				"つらいか",
				"話なら適当に聞くよ",
				"ずっとみてるよ",
				"なるほど",
			]
			choice = I.random.choice(ngo)
			await message.reply(f"{choice}")

		elif "たのしい" in message.content or "楽しい" in message.content:
			ngo = [
				"それはよかった",
				"そうか",
				"いいね～",
				"楽しいのが一番よ",
				"ほんまか",
				"なるほど",
				"楽しければ何でもいいとか思ってないよね？思ってないか",
				"ほえ～"
			]
			choice = I.random.choice(ngo)
			await message.reply(f"{choice}")

		elif "スロットやらせて" in message.content or "スロットやりたい" in message.content or "スロット頼む" in message.content or "スロットやろ" in message.content or "スロットやる" in message.content or "スロットしたい" in message.content or "スロットしよ" in message.content:
			ngo = [
				f"OK！！！！ゲームスロットチャレンジ！！！！！！！！！\n\n{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！",
				f"しかたないな～\n\n{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！",
				f"はい！！！！\n\n{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！",
				f"ゲームスロットチャrrrrrrrrrrrrrレンジ！！！！！！！！！\n\n{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！",
				f"{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！",
				f"{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！\n{choice_games4}！！！！",
				f"{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！\n{choice_games4}！！！！\n{choice_games5}！！！！！",
				f"{choice_games}、はい",
				"今はちょっと...",
				"明日ならいいよ",
				"もうちょいまって！",
				"だる",
				"だめ",
				"霞でも食ってろ",
				"さっきやったでしょ！",
				"ねむ～い",
				"あとでね",
				"おとといきやがれください",
				f"じゃんけんならいいよ、{rps}出せオラ",
			]
			choice = I.random.choice(ngo)
			await message.reply(f"{choice}")

		elif "じゃんけんやらせて" in message.content or "じゃんけんやりたい" in message.content or "じゃんけん頼む" in message.content or "じゃんけんやろ" in message.content or "じゃんけんやる" in message.content or "じゃんけんしたい" in message.content or "じゃんけんしよ" in message.content:
			ngo = [
				f"OK！！！！最初はグー！！！！！！！！！じゃんけんポン！！！！！！！！！！！\n\n...ンゴは{rps}を出したぞ",
				f"しかたないな～\n\n最初はグー！！！！！！！！！じゃんけんポン！！！！！！！！！！！\n\n...ンゴは{rps}を出したぞ",
				f"はい！！！！\n\n最初はグー！！！！！！！！！じゃんけんポン！！！！！！！！！！！\n\n...ンゴは{rps}を出したぞ",
				f"行くぞ！！！！！！！！！！！！！最初はグー！！！！！！！！！じゃんけんポン！！！！！！！！！！！\n\n...ンゴは{rps}を出したぞ",
				f"最初はグー！！！！！！！！！じゃんけんポン！！！！！！！！！！！\n\n...ンゴは{rps}を出したぞ",
				f"じゃんけんポン！！！！！！！！！！！\n\n...ンゴは{rps}を出したぞ",
				f"ポン！！！！！！！！！！！\n\n...ンゴは{rps}を出したぞ",
				f"...ンゴは{rps}を出したぞ",
				f"{rps}！！！！",
				f"{rps}出したよ",
				f"{rps}。",
				"今はちょっと...",
				"明日ならいいよ",
				"もうちょいまって！",
				"だる",
				"だめ",
				"霞でも食ってろ",
				"さっきやったでしょ！",
				"ねむ～い",
				"あとでね",
				"おとといきやがれください",
				f"{choice_games}でもやってろ",
			]
			choice = I.random.choice(ngo)
			await message.reply(f"{choice}")

		
		elif message.content == f"{I.client.user.mention} 人に成る":
			#しきさいのすうじたせ
			await message.reply(f"ンゴにアクセスしようとしてる？\nこっちはこれだけアクセスしてるんだけど、名前が分からないんだよね、教えてくれない？\n```\n〇〇〇〇７〇〇〇\n〇４〇〇〇〇〇〇〇〇〇〇〇〇〇〇９〇〇、〇〇〇〇〇〇〇〇〇〇〇〇１〇〇。\n〇〇〇〇５\n〇〇〇〇〇〇〇〇〇〇〇〇３〇〇〇〇８〇〇、〇〇〇〇〇〇〇〇・〇〇０〇〇〇〇〇〇〇〇〇〇〇。\n〇〇〇６\n〇〇２〇〇〇〇〇〇〇、〇〇〇〇〇〇〇〇、〇〇〇〇〇〇、〇〇〇〇〇〇〇〇〇〇〇〇。\n\n０１２３４５６７８９。\nその先で1が無いもの。これはバグ。```")
			await message.delete()
		elif message.content == f"{I.client.user.mention} #E6D263":
			role = message.guild.get_role(1223022775715893368)
			await message.author.add_roles(role)
			await message.reply(f"ようやくみつけた")
			await message.delete()
		else:
			ngo = [
			# さらなる飯テロ無法地帯・おこのみ鯖https://discord.gg/bDDJF88Mjk 
			# 8MFDkみる
			"上から7番目、後ろから、4、3、6、9、1、1行目、> 。。。2。。。。。。。・。。。1。",
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
			f"知らん！！唐突なゲームスロットチャレンジ！！！！！！！！！\n\n{choice_games}！\n{choice_games2}！！\n{choice_games3}！！！",
			"え、それ明日じゃダメ...？",
			"おっけ～",
			f"うるさい！{choice_games}でもやってろ！！！！！",
			f"わかる、ところで{choice_games}やらない？{choice_games2}でもいい",
			"わからん",
			"なるほど",
			"すごい",
			"えらい",
			"何が？",
			"バグって見えない",
			"霞でも食ってろ",
			"ンゴになら何してもいいと思ってるな？",
			"嘘だろ",
			"ほう",
			"ok",
			"知らんな",
			"わからん、もうちょい詳しく",
			"いいね",
			"それきらい",
			"それすき",
			"なるほど、[これ](<https://www.youtube.com/watch?v=dQw4w9WgXcQ>)が近いかもな",
			"サーバー規約読んだ？",
			f"{message.content}って言われてもな～",
			"ひえ～",
			"こわ",
			"お前がな",
			"貴様がな",
			"お主がな",
			]
			choice = I.random.choice(ngo)
			await message.reply(f"{choice}")
		
		