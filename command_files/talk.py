import define_first as I
from command_files.ngold.ngolds import *
from command_files.ngold.embed import *

@I.client.event
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def on_message(message:I.discord.message.Message):
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
		if ("？" in message.content or "?" in message.content) and ("しってる" in message.content or "知ってる" in message.content or "しらない" in message.content or "知らない" in message.content):
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
			await message.reply(f"{choice}")

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
			await message.reply(f"{choice}")

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
			await message.reply(f"{choice}")

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
		elif "お小遣いください" in message.content or "おこづかいください" in message.content:
			data = ng_watch(userid=message.author.id)
			if I.random.randint(1,16) == 1 and data[0] < 2000:
				ngo = [
					"仕方ないな～",
					"しゃーなしだぞ",
					"文句言うなよ～",
					"わがまま言いやがってヨ～～",
					"はい",
					"どうぞ～",
					"ｲｲﾖ～"
				]
				choice = I.random.choice(ngo)
				await message.reply(f"{choice}")
				ng = I.random.randint(1,1000)
				ng_add(userid=message.author.id,supplier=I.client.user.id,ng=ng)
				embed = ng_receive_embed(send=I.client.user,receive=message.author,value=ng)
				await message.reply(embed=embed)
			elif data[0] >= 2000:
				ngo = [
					"オメェNgold持ってんだろ！！！",
					"やだよ～ん",
					"Ngoldありますよね？",
					"やだ",
					"お前は払う側になれ",
					"持ってんだろ！自力で増やしてこい！！！！"
				]
				choice = I.random.choice(ngo)
				await message.reply(f"{choice}")
			else:
				ngo = [
					"そっか",
					"あーげない",
					"誠意が足りない",
					"ハハ",
					"お金ないの？",
					"どうしよっかな～",
					"お前にやるNgoldはない",
					"みくじでも回してな",
					"やだ",
					"え～"
				]
				choice = I.random.choice(ngo)
				await message.reply(f"{choice}")

		elif "スロット" in message.content:
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

		elif "じゃんけん" in message.content:
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

		elif "チンチロ" in message.content:
			entry = I.random.randint(0,1)

			if entry == 1:
				entry_mes = [
					"OK！！！！じゃあ最初にンゴが振るね",
					"しかたないな～\n先に振るね",
					"行くぞ！先に振らせろ！！！！！！！！！！！"
					"振るよ～",
					"行くよ～～",
				]
				choice = I.random.choice(entry_mes)
				await message.reply(f"{choice}")
				I.time.sleep(3)
				## ダイス
				rolling = I.discord.Embed(title=f"チンチロ！！せーの！！", )
				#| None=目無し | 1~6=目あり | 11~16=ゾロ目 | 0=ヒフミ | 9=シゴロ |#
				dealer = f""
				roll = 0
				dealer_try = {
					1:[],
					2:[],
					3:[],
				}
				for i in range(2):
					roll = i + 1
					ceelo_roll_a = I.random.randint(1, 6)
					ceelo_roll_b = I.random.randint(1, 6)
					ceelo_roll_c = I.random.randint(1, 6)
					ceelo_l = [ceelo_roll_a,ceelo_roll_b,ceelo_roll_c]
					ceelo_l.sort()
					print(ceelo_l)

					dealer_try[roll] = []
					for i in range(3):
						dealer_try[roll].append(str(ceelo_l[i]))
					print(str(dealer_try[roll]))
					
					if ceelo_roll_a==ceelo_roll_b!=ceelo_roll_c:
						dealer = f"役あり「**{ceelo_roll_c}**」！"
						ngo_mes = f"役ありの「`{ceelo_roll_c}`」"
						break
					elif ceelo_roll_b==ceelo_roll_c!=ceelo_roll_a:
						dealer = f"役あり「**{ceelo_roll_a}**」！"
						ngo_mes = f"役ありの「`{ceelo_roll_a}`」"
						break
					elif ceelo_roll_a==ceelo_roll_c!=ceelo_roll_b:
						dealer = f"役あり「**{ceelo_roll_b}**」！"
						ngo_mes = f"役ありの「`{ceelo_roll_b}`」"
						break
					elif ceelo_roll_a==ceelo_roll_b==ceelo_roll_c==1:
						dealer = f"「**ピンゾロ**」！！！！"
						ngo_mes = f"ピンゾロ"
						break
					elif ceelo_roll_a==ceelo_roll_b==ceelo_roll_c:
						dealer = f"ゾロ目！「{ceelo_roll_a}」！！！"
						ngo_mes = f"`{ceelo_roll_a}`のゾロ目"
						break
					elif ceelo_l==[1,2,3]:
						dealer = f"「**ヒフミ**」！よわ！！！！！"
						ngo_mes = f"ヒフミ"
						break
					elif ceelo_l==[4,5,6]:
						dealer = f"「**シゴロ**」！！"
						ngo_mes = f"シゴロ"
						break
					else:
						dealer = "「**役なし**」！よわ！！"
						ngo_mes = f"役なし"
					
				try_1 = '・'.join(dealer_try[1])
				if roll == 1:
					dl = f"一回目！「`{try_1}`」！\n\n\n{dealer}"
				elif roll == 2:
					try_2 = '・'.join(dealer_try[2])
					dl = f"一回目！「`{try_1}`」！\n二回目！「`{try_2}`」！！\n\n\n{dealer}"
				else:
					try_2 = '・'.join(dealer_try[2])
					try_3 = '・'.join(dealer_try[3])
					dl = f"一回目！「`{try_1}`」！\n二回目！「`{try_2}`」！！\n三回目！「`{try_3}`」！！！\n\n\n{dealer}"
				
				rolling.add_field(name="なにがでたかな", value=f"{''.join(dl)}", inline=True)
				await message.channel.send(embed=rolling)
				I.sleep(1)
				await message.channel.send(f"ンゴは{ngo_mes}だったよ、そっちは？")
			else:
				entry_mes = [
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
				]
				choice = I.random.choice(entry_mes)
				await message.reply(f"{choice}")

		elif message.content == f"{I.client.user.mention} 人に成る":
			#しきさいのすうじたせ
			ms_reply = await message.reply(f"ンゴのデータにアクセスしようとしてる？\nこっちはこれだけアクセスしてるんだけど、名前が分からないんだよね、教えてくれない？\nもうちょいで消すからスクショかコピーでメモってね\n```\n〇〇〇〇７〇〇〇\n〇４〇〇〇〇〇〇〇〇〇〇〇〇〇〇９〇〇、〇〇〇〇〇〇〇〇〇〇〇〇１〇〇。\n〇〇〇〇５\n〇〇〇〇〇〇〇〇〇〇〇〇３〇〇〇〇８〇〇、〇〇〇〇〇〇〇〇・〇〇０〇〇〇〇〇〇〇〇〇〇〇。\n〇〇〇６\n〇〇２〇〇〇〇〇〇〇、〇〇〇〇〇〇〇〇、〇〇〇〇〇〇、〇〇〇〇〇〇〇〇〇〇〇〇。\n\n5つの０１２３４５６７８９。\nその先で1が無いもの。これはバグ。```")
			await message.delete()
			await ms_reply.delete(delay=10)
		elif message.content == f"{I.client.user.mention} Confetti":
			role = message.guild.get_role(1223022775715893368)
			await message.author.add_roles(role)
			await message.reply(f"ようやく  みつけた")
			if role in message.author.roles:
				ng = 10000000
				ng_add(userid=message.author.id,supplier=I.client.user.id,ng=ng)
				#embed = ng_receive_embed(send=I.client.user,receive=message.author,value=ng)
				#await message.reply(embed=embed)
			await message.delete()
		else:
			ngo = [
			# さらなる飯テロ無法地帯・おこのみ鯖https://discord.gg/bDDJF88Mjk 
			# 8MFDkみる
			"上から7番目、後ろから、4、3、6、9、1、1行目、> 。。。2。。。。。。。・。。。1。",
			"お主ラッキーだな、褒美をやろう",
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
			
			if choice == "お主ラッキーだな、褒美をやろう":
				ng = 5000
				ng_add(userid=message.author.id,supplier=I.client.user.id,ng=ng)
				embed = ng_receive_embed(send=I.client.user,receive=message.author,value=ng)
				await message.reply(embed=embed)
			await message.reply(f"{choice}")
		
		