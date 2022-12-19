import enum
import discord
from discord import app_commands
from discord.ext import commands

token = "OTc1NzA5NzgzNTYwNjk1ODQ4.G-Bww3.cNVDFIKCUlSez31_hqbSOq-CqQqDL0-Aaxzvf0" 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=token))
            self.synced = True

client = aclient()
tree = app_commands.CommandTree(client) 


#サーバーid(んご、TestMain)
guilds = 1021500432578789557
#guilds = 760807298968322048
    
#メッセージ送信チャンネル(んご：登校動画・ライブ配信、test：チャンネル指定メッセージ)
send_ch = 1053725844448739398
#send_ch = 1022544579611856996

#名前更新チャンネル(んご：専用ステージ、最下層のボイス)
rename_ch = 1054417954038632578
#rename_ch = 1054419304155721858


@client.event
async def on_ready():
    print("ンゴ～")
    print('------')
    print("discord.py Ver." + discord.__version__)# discord.pyのバージョン
    activity = discord.Activity(status=discord.Status.online, name='コンペティティブ', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)
    await tree.sync(guild=discord.Object(id=guilds))




###オンライン
@tree.command(
    name="live",
    description="配信告知とステータス表示の変更をします。"
)

@discord.app_commands.describe(
    url = "配信のURLを入力してください。"
)

@discord.app_commands.checks.cooldown(
    1,
    600,
    key=None
)

@discord.app_commands.guilds(
    discord.Object(id = guilds)
)

async def live(ctx: discord.Interaction, url:str):
    #🔴
    uniemoji_RC = "\N{Large Red Circle}"
    await ctx.response.defer(ephemeral = True)

    #通知を送るchを指定
    channel = client.get_channel(1053725844448739398)
    await channel.send(f"{uniemoji_RC}：**{ctx.user}がライブ配信中！**\n{url}")

    #名前を変えるvcを指定
    channel = client.get_channel(1054417954038632578)
    await channel.edit(name =f"𝗟𝗜𝗩𝗘：{uniemoji_RC}𝗢𝗡𝗟𝗜𝗡𝗘")

    await ctx.followup.send(f"{uniemoji_RC}：サーバーの配信ステータスがオンラインになりました。\n配信終了時には__必ず__**「/end」**を実行してください。")

@live.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        retry_after_int = int(error.retry_after)
        retry_minute = retry_after_int // 60
        retry_second = retry_after_int % 60

        await interaction.response.send_message(f"＊んごりンゴは必死にサーバーを冷やしている。\n(レート制限回避用クールダウン終了まで残り **{retry_minute}分{retry_second}秒** )", ephemeral = True)


###オフライン
@tree.command(
    name="end",
    description="ステータスをオフラインに変更します。"
)

@discord.app_commands.checks.cooldown(
    1,
    600,
    key=None
)

@discord.app_commands.guilds(
    discord.Object(id = guilds)
)

async def end(ctx: discord.Interaction):
    await ctx.response.defer(ephemeral = True)
        #⚫
    uniemoji_BC = "\N{Medium Black Circle}"
    
    #vc名変更
    channel = client.get_channel(1054417954038632578)
    await channel.edit(name =f"𝗟𝗜𝗩𝗘：{uniemoji_BC}𝗢𝗙𝗙𝗟𝗜𝗡𝗘")

    await ctx.followup.send(f"{uniemoji_BC}：サーバーの配信ステータスがオフラインになりました。")


@end.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        retry_after_int = int(error.retry_after)
        retry_minute = retry_after_int // 60
        retry_second = retry_after_int % 60

        await interaction.response.send_message(f"＊まだライブは始まったばかりだ。\n(レート制限回避用クールダウン終了まで残り **{retry_minute}分{retry_second}秒** )", ephemeral = True)


#@tree.command(
#    name="help"
#    )
#async def commands(ctx: discord.Interaction):
#    embed_2 = discord.Embed(title="へるぷだよこれは！", description="へるぷなんだよなぁ", color=0xff4454)
#    embed_2.add_field(name=".commands", value="これ", inline=False),
#    embed_2.add_field(name=".map", value="まっぷをきめるよ", inline=False),
#    embed_2.add_field(name=".agt", value="えーじぇんとをえらぶよ\n\nオプション：\n.d (デュエリストのみ)\n.i (イニシエーターのみ)\n.c (コントローラーのみ)\n.s ("
#                                       "センチネルのみ)\n例：.agt.d", inline=False),
#    embed_2.add_field(name=".wpn", value="ぶきをえらぶよ\n\nオプション：\n.s (セカンダリ武器のみ)\n.p (プライマリ武器のみ)\n例：.wpn.s", inline=False)
#    embed_2.add_field(name=".soyjoy", value="なんだこれは", inline=False)
#    await ctx.send(embed=embed_2),


@tree.command(
    name = "ngo",
    description = "てきと～に話すよ"
)
async def ngo(ctx: discord.Interaction):
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
    await ctx.response.send_message(f"{choice}"),


@tree.command(
    name = "map",
    description= "マップをランダムに選択します。"
)
#@discord.app_commands.describe(banmap = "除外するマップを選択します。")
#banmap:str = None
async def map(ctx: discord.Interaction):
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
    await ctx.response.send_message(f"次のマップは「**{choice}**」だよ！"),


@tree.command(name="agt")
async def agt(ctx: discord.Interaction):
    import random
    all = [
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


    agt = {}
    choice = random.choice(agt)
    await ctx.response.send_message(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！"),


@tree.command(name="wpn")
async def wpn(ctx: discord.Interaction):
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
    await ctx.response.send_message(f"次の{ctx.message.author.name}の武器は「**{choice}**」だよ！"),


@tree.command(name="soyjoy")
async def sj(ctx: discord.Interaction):
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
    await ctx.response.send_message(f"SOYJOY{choice}味を食え")




#@bot.command(name="agt.d")
#async def agtd(ctx):
#    import random
#    agtd = ["ジェット","ネオン","フェニックス","ヨル","レイズ","レイナ"]
#    choice = random.choice(agtd)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="agt.i")
#async def agt(ctx):
#    import random
#    agt = ["KAY/O","スカイ","ソーヴァ","フェイド","ブリーチ"]
#    choice = random.choice(agt)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="agt.c")
#async def agt(ctx):
#    import random
#    agt = ["アストラ","ヴァイパー","オーメン","ハーバー","ブリムストーン"]
#    choice = random.choice(agt)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="agt.s")
#async def agt(ctx):
#    import random
#    agt = ["キルジョイ","サイファー","セージ","チェンバー"]
#    choice = random.choice(agt)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="wpn.s")
#async def wpns(ctx):
#    import random
#    wpns = ["クラシック","ショーティー","フレンジー","ゴースト","シェリフ"]
#    choice = random.choice(wpns)
#    await ctx.reply(f"次の{ctx.message.author.name}のセカンダリは「**{choice}**」だよ！"),


#@bot.command(name="wpn.p")
#async def wpnp(ctx):
#    import random
#    wpnp = ["スティンガー","スペクター","バッキー","ジャッジ","ブルドッグ","ガーディアン","ファントム","ヴァンダル","マーシャル","オペレーター","アレス","オーディン"]
#    choice = random.choice(wpnp)
#    await ctx.reply(f"次の{ctx.message.author.name}のプライマリは「**{choice}**」だよ！"),

client.run(token)
