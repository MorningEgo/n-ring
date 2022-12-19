# coding: utf-8
import discord
from discord.ext import commands


intents = discord.Intents.all()
intents.message_content = True


client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix=".", intents=intents)
tree = discord.app_commands.CommandTree(client) 


guilds = [
    1021500432578789557,
    760807298968322048
    ]


send_ch = [
    1053725844448739398,
    1022544579611856996
]


@tree.command(
    name="live",
    description="ボイスチャンネルをライブ用に変え、専用チャンネルで告知します。"
)
@tree.commands.describe()
async def live(ctx: discord.Intraction, url, guild_ids=guilds):
    #通知を送るchを指定
    ch = client.get_channel(send_ch)
    #送信場所のvc名変更
    vc = client.get_channel()
    #🔴
    uniemoji_RC = "\N{Large Red Circle}"
    name = {ctx.message.author.name}
    await vc.edit(name = vc + "(live)")
    await ch.send("**" + uniemoji_RC + {ctx.message.author.name} + "がライブ配信中！**\n" + url)


@bot.event
async def on_ready():
    print("ンゴ～")
    print('------')
    print("discord.py Ver.")
    print(discord.__version__)  # discord.pyのバージョン
    activity = discord.Activity(status=discord.Status.online, name='アンレート', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)
    await tree.sync()


@bot.command(name="commands")
async def commands(ctx):
    embed_2 = discord.Embed(title="へるぷだよこれは！", description="へるぷなんだよなぁ", color=0xff4454)
    embed_2.add_field(name=".commands", value="これ", inline=False),
    embed_2.add_field(name=".map", value="まっぷをきめるよ", inline=False),
    embed_2.add_field(name=".agt", value="えーじぇんとをえらぶよ\n\nオプション：\n.d (デュエリストのみ)\n.i (イニシエーターのみ)\n.c (コントローラーのみ)\n.s ("
                                       "センチネルのみ)\n例：.agt.d", inline=False),
    embed_2.add_field(name=".wpn", value="ぶきをえらぶよ\n\nオプション：\n.s (セカンダリ武器のみ)\n.p (プライマリ武器のみ)\n例：.wpn.s", inline=False)
    embed_2.add_field(name=".soyjoy", value="なんだこれは", inline=False)
    await ctx.send(embed=embed_2),


@bot.command(name="ngo")
async def ngo(ctx):
    import random
    ngo = [
        "平気平気、全部想定済みだから。",
        "気づいたことは全部報告して！次の作戦に活かすから。",
        "エリアの制圧は私に任せて。その分、他で働いてよね。",
        "実力と、テクノロジーの差で圧倒していこう。",
        "みんな、装備に問題はない？チェックはしっかりね。",
        "仮に私が死んでも、動揺しないこと。あと、ハードディスクは絶対廃棄して。",
        "ドイツの家電は世界一？いやいや、兵器も世界一だよ！",
        "いい？銃はただの道具だよ。道具は考えて使わなきゃ。",
        "ﾎﾞｯﾄﾁｬﾝを信じて！一度しか誤動作したことないし、最悪指が飛ぶくらいだから。",
        "死んじゃだめだよ。方法なら教えてあげるからさ。",
        "まずは分析、次に改善。",
        "同じ作戦にいつまでもやられる私じゃないよ。",
        "ちょっとー！！！！なんで誰もパルスモニター着けてくれてないの？測定したいだけだってば！\nマッドサイエンティスト扱いしないでよね。",
        "悩んでるみたいw\n頭の回路が焼ける匂いがするw",
        "焦った時は私を見なよ！私はいつだって冷静だから。\nキュウリみたいにクール...って言うんだっけ？",
        "ここの戦場で使ってる武器は全部私が作ったんだー！危険だから気をつけてね！\n\n\n...なんで怒ってんの？",
        "ここ最近の戦闘6回分についてレポートをまとめておいたよ。\n読んでくれたよね？読んで...くれてないの？",
        "もしかしてあの人たち、私の技術に勝てると思ってる？w\nテストしてみようか？",
        "みんなー！バックアップは取ってあるから死んでも大丈夫だよ！！！！！！！！！\n\n\n\nいや、冗談だってば、冗談。うん。",
        "私の防衛プランを採用してればこんな戦い防げたのに...\nま、後始末も仕事の内か！",
        "クレジットとアビリティ、腐らせないようにね。",
        "偵察は「素早く」ね。",
        "考えるのは私に任せて。",
        "火力より、まずは作戦。",
        "フィールドテストを始めるよ～",
        "生き残りたいなら冷静にね！",
        "作戦を見直そう。",
        "大したことないね（笑）",
        "デブリーフィングやるよ～\n\n\nってあれ、やらないの？",
        "いつも通り完璧な計算！",
        "さぁみんな、試験管持って！\n家に帰るのはサンプル回収してからね！",
        "SOYJOY食べなよ！\n\n\n...食べないの？",
        "おススメの味は「2種のアップル」かな。",
        "ンゴ～",
        "ピピピピピ！！！！一旦止めます",
        "**Ｍ Ａ Ｃ Ｈ Ｏ**",
        "ジャッジなんだよねぇ！",
        "かまどなんだよなぁ",
        "ミニマかな～やっぱり",
        "ミニマとか使ってるやつおる？？？",
        "ﾋﾟﾛﾋﾟﾛﾘｰﾝ！ｷﾞｭｲﾝｷﾞｭｲﾝｷﾞｭｲﾝｷﾞｭｲﾝｷﾞｭｲｰｰｰﾝ！！！\nドン！(右から)\nドン！(左から)\nゴゴゴゴゴ！！！(奥から)\nス パ イ ク ラ ッ シ ュ 確 ☆ 定(極太明朝虹色文字)",
        "ヨルはイニシエーターだよ。",
        "ホウント「目が合ったな！これでお前とも縁ができた！(位置特定)」",
        "アラームボット展開！",
        "ボットを戻すよ",
        "セントリー設置！",
        "ﾎﾞｯﾄﾁｬﾝがやられた！",
        "カウントダウン開始！",
        "ﾎﾞｯﾄﾁｬﾝがやられた！\n...いや、なんでもない。",
        "マーシャルを信じなさい。",
        "マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。",
        "140カット！！！！！！！！！！！！！！！！！！！！！(キレ)",
        "ピュレグミうめ～",
        "俺がハンターだ！",
        "ワイがハンターや！",
        "俺がハンターか？",
        "俺がガンダムだ！",
        "お前がハンターだ！",
        "もうお前がハンターでいいよ",
        "ヌベヂョンヌゾジョンベルミッティスモゲロンボョｗｗｗｗｗｗイヒーｗｗイヒヒｗ└(՞ةڼ◔)」",
        "ンゴッ！？",
        "なるほどﾆｬﾝｷｬｯﾂ",
        "ンゴロンゴロ",
        "綾鷹 茶葉の甘みを飲みましょう。",
        "ンゴネミ",
        "3550カット！！！！！！！！！！！！！！",
        "夏はこれ使う笑"
    ]
    choice = random.choice(ngo)
    await ctx.reply(f"{choice}"),


@bot.command(name="map")
async def map(ctx):
    import random
    map = [
        "アセント",
        "アイスボックス",
        "スプリット",
        "バインド",
        "ブリーズ",
        "フラクチャー",
        "ヘイヴン",
        "パール"
    ]
    choice = random.choice(map)
    await ctx.reply(f"次のマップは「**{choice}**」だよ！"),


@bot.command(name="agt")
async def agt(ctx):
    import random
    agt = [
        "KAY/O",
        "アストラ",
        "ヴァイパー",
        "オーメン",
        "キルジョイ",
        "サイファー",
        "ジェット",
        "スカイ",
        "セージ",
        "ソーヴァ",
        "チェンバー",
        "ネオン",
        "ハーバー",
        "フェイド",
        "フェニックス",
        "ブリーチ",
        "ブリムストーン",
        "ヨル",
        "レイズ",
        "レイナ"
    ]
    choice = random.choice(agt)
    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！"),


@bot.command(name="agt.d")
async def agtd(ctx):
    import random
    agtd = [
        "ジェット",
        "ネオン",
        "フェニックス",
        "ヨル",
        "レイズ",
        "レイナ"
    ]
    choice = random.choice(agtd)
    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")


@bot.command(name="agt.i")
async def agt(ctx):
    import random
    agt = [
        "KAY/O",
        "スカイ",
        "ソーヴァ",
        "フェイド",
        "ブリーチ"
    ]
    choice = random.choice(agt)
    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")


@bot.command(name="agt.c")
async def agt(ctx):
    import random
    agt = [
        "アストラ",
        "ヴァイパー",
        "オーメン",
        "ハーバー",
        "ブリムストーン"
    ]
    choice = random.choice(agt)
    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")


@bot.command(name="agt.s")
async def agt(ctx):
    import random
    agt = [
        "キルジョイ",
        "サイファー",
        "セージ",
        "チェンバー"
    ]
    choice = random.choice(agt)
    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")


@bot.command(name="wpn")
async def wpn(ctx):
    import random
    wpn = [
        "クラシック",
        "ショーティー",
        "フレンジー",
        "ゴースト",
        "シェリフ",
        "スティンガー",
        "スペクター",
        "バッキー",
        "ジャッジ",
        "ブルドッグ",
        "ガーディアン",
        "ファントム",
        "ヴァンダル",
        "マーシャル",
        "オペレーター",
        "アレス",
        "オーディン",
        "ナイフ"
    ]
    choice = random.choice(wpn)
    await ctx.reply(f"次の{ctx.message.author.name}の武器は「**{choice}**」だよ！"),


@bot.command(name="wpn.s")
async def wpns(ctx):
    import random
    wpns = [
        "クラシック",
        "ショーティー",
        "フレンジー",
        "ゴースト",
        "シェリフ"
    ]
    choice = random.choice(wpns)
    await ctx.reply(f"次の{ctx.message.author.name}のセカンダリは「**{choice}**」だよ！"),


@bot.command(name="wpn.p")
async def wpnp(ctx):
    import random
    wpnp = [
        "スティンガー",
        "スペクター",
        "バッキー",
        "ジャッジ",
        "ブルドッグ",
        "ガーディアン",
        "ファントム",
        "ヴァンダル",
        "マーシャル",
        "オペレーター",
        "アレス",
        "オーディン"
    ]
    choice = random.choice(wpnp)
    await ctx.reply(f"次の{ctx.message.author.name}のプライマリは「**{choice}**」だよ！"),


@bot.command(name="soyjoy")
async def sj(ctx):
    import random
    sj = [
        "ストロベリー",
        "ブルーベリー",
        "3種のレーズン",
        "2種のアップル",
        "コーヒー&ナッツ",
        "抹茶&マカダミア",
        "アーモンド&チョコレート",
        "ピーナッツ",
        "ホワイトチョコ&レモン",
        "バナナ",
        "スコーンバープレーン"
    ]
    choice = random.choice(sj)
    await ctx.reply(f"SOYJOY{choice}味を食え")


bot.run('OTc1NzA5NzgzNTYwNjk1ODQ4.G-Bww3.cNVDFIKCUlSez31_hqbSOq-CqQqDL0-Aaxzvf0')
