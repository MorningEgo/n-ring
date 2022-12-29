import enum
import discord
from discord import app_commands
import random

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


#-------------------------------------------------------------------------------------------#
#サーバーid(んご、TestMain)
guildid = 1021500432578789557
#guildid = 760807298968322048
    
#メッセージ送信チャンネル(んご：登校動画・ライブ配信、test：チャンネル指定メッセージ)
send_ch = 1053725844448739398
#send_ch = 1022544579611856996

#名前更新チャンネル(んご：専用ステージ、最下層のボイス)
rename_ch = 1054417954038632578
#rename_ch = 1054419304155721858

cond_head = "`[ 条件："
cond_foot = "のみ ]`"
#-------------------------------------------------------------------------------------------#

#起動メッセージ
@client.event
async def on_ready():
    
    mode = [
        "アンレート",
        "コンペティティブ",
        "デスマッチ",
        "エスカレーション",
        "レプリケーション",
        "Splatoon3",
        "麻雀"
    ]
    choice = random.choice(mode)
    print("ンゴ～")
    print('------------------------------')
    print("discord.py Ver." + discord.__version__)# discord.pyのバージョン
    print('------------------------------')
    activity = discord.Activity(status=discord.Status.online, name= choice, type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)
    await tree.sync(guild=discord.Object(id=guildid))



    

###ライブモード
class LiveMode(enum.Enum):
    START = "START"
    END = "END"

@tree.command(
    name="live",
    description="ライブの設定をします。"
)
@discord.app_commands.describe(
    stream = "配信状態を変更します。"
)

@discord.app_commands.describe(
    url = "配信のURLを添付します。ライブスタート時のみ有効です。"
)
@discord.app_commands.checks.cooldown(
    2,
    600,
    key=None
)
@discord.app_commands.guilds(
    discord.Object(id = guildid)
)

async def live(ctx: discord.Interaction, stream:LiveMode, url:str = None):
    print("")
    print("[ live setting up... ]")

    #🔴
    uniemoji_RC = "\N{Large Red Circle}"
    print("live > Load: Emoji[RC] ")

    #⚫
    uniemoji_BC = "\N{Medium Black Circle}"
    print("live > Load: Emoji[BC] ")
    
    editchannel = client.get_channel(1054417954038632578)
    print("live > set: editchannel")

    sendchannel = client.get_channel(1053725844448739398)
    print("live > set: sendchannel")
    
    await ctx.response.defer()
    print("live > Defer ok.")

    print("= stream mode check ============================================")
    if stream == LiveMode.START:
        print("live > if : [START]")

        Cname = "𝗟𝗜𝗩𝗘：" + uniemoji_RC + "𝗢𝗡𝗟𝗜𝗡𝗘"
        print("live:START > 'Cname' wrote.")

        Cmes = f"{uniemoji_RC}：**{ctx.user}がライブ配信中！**\r\n{url}"
        print("live:START > 'Cmes' wrote.")

        mes = f"{uniemoji_RC}：サーバーの配信ステータスがオンラインになりました。"
        print("live:START > Live starting...")
        

    elif stream == LiveMode.END:
        print("live > if check ok : END")

        Cmes = f"{uniemoji_BC}：**{ctx.user}のライブは終了しました。**"
        print("live:END > 'Cmes' wrote.")

        Cname = "𝗟𝗜𝗩𝗘：" + uniemoji_BC + "𝗢𝗙𝗙𝗟𝗜𝗡𝗘"
        print("live:END > 'Cname' wrote.")

        mes = f"{uniemoji_BC}：サーバーの配信ステータスがオフラインになりました。"
        print("live:END > Live stopping...")
    
    else:
        mes = f"コマンド、もしくはシステムに問題があります。もう一度やり直すか、開発者に連絡してください。"
        print("live:failed > Command error detected.")
    
    print("================================================================")
    print("live > Live ready...")


    await sendchannel.send(f"{Cmes}")
    print("live > Info send ok.")

    await editchannel.edit(name=Cname)
    print("live > Ch-name edit ok.")

    await ctx.followup.send(f"{mes}")
    print("[ FollowUp ok. command is completed.]")
    print("")
    

@live.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        retry_after_int = int(error.retry_after)
        retry_minute = retry_after_int // 60
        retry_second = retry_after_int % 60

        print(f"live > Cooldown now. End is [{retry_minute}:{retry_second}]")
        await interaction.response.send_message(f"＊んごりンゴは休憩中だよ。\n(レート制限回避用クールダウン終了まで残り **{retry_minute}分{retry_second}秒** )", ephemeral = True)
        


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
@discord.app_commands.guilds(
    discord.Object(id = guildid)
)
async def ngo(ctx: discord.Interaction):
    
    ngo = [
        f"平気平気、全部想定済みだから。",
        f"気づいたことは全部報告して！次の作戦に活かすから。",
        f"エリアの制圧は私に任せて。その分、他で働いてよね。",
        f"実力と、テクノロジーの差で圧倒していこう。",
        f"みんな、装備に問題はない？チェックはしっかりね。",
        f"仮に私が死んでも、動揺しないこと。あと、ハードディスクは絶対廃棄して。",
        f"ドイツの家電は世界一？いやいや、兵器も世界一だよ！",
        f"いい？銃はただの道具だよ。道具は考えて使わなきゃ。",
        f"ﾎﾞｯﾄﾁｬﾝを信じて！一度しか誤動作したことないし、最悪指が飛ぶくらいだから。",
        f"死んじゃだめだよ。方法なら教えてあげるからさ。",
        f"まずは分析、次に改善。",
        f"同じ作戦にいつまでもやられる私じゃないよ。",
        f"ちょっとー！！！！なんで誰もパルスモニター着けてくれてないの？測定したいだけだってば！\nマッドサイエンティスト扱いしないでよね。",
        f"悩んでるみたいw\n頭の回路が焼ける匂いがするw",
        f"焦った時は私を見なよ！私はいつだって冷静だから。\nキュウリみたいにクール...って言うんだっけ？",
        f"ここの戦場で使ってる武器は全部私が作ったんだー！危険だから気をつけてね！\n\n\n...なんで怒ってんの？",
        f"ここ最近の戦闘6回分についてレポートをまとめておいたよ。\n読んでくれたよね？読んで...くれてないの？",
        f"もしかしてあの人たち、私の技術に勝てると思ってる？w\nテストしてみようか？",
        f"みんなー！バックアップは取ってあるから死んでも大丈夫だよ！！！！！！！！！\n\n\n\nいや、冗談だってば、冗談。うん。",
        f"私の防衛プランを採用してればこんな戦い防げたのに...\nま、後始末も仕事の内か！",
        f"クレジットとアビリティ、腐らせないようにね。",
        f"偵察は「素早く」ね。",
        f"考えるのは私に任せて。",
        f"火力より、まずは作戦。",
        f"フィールドテストを始めるよ～",
        f"生き残りたいなら冷静にね！",
        f"作戦を見直そう。",
        f"大したことないね（笑）",
        f"デブリーフィングやるよ～\n\n\nってあれ、やらないの？",
        f"いつも通り完璧な計算！",
        f"さぁみんな、試験管持って！\n家に帰るのはサンプル回収してからね！",
        f"SOYJOY食べなよ！\n\n\n...食べないの？",
        f"おススメの味は「2種のアップル」かな。",
        f"ンゴ～",
        f"ピピピピピ！！！！一旦止めます",
        f"**Ｍ Ａ Ｃ Ｈ Ｏ**",
        f"ジャッジなんだよねぇ！",
        f"かまどなんだよなぁ",
        f"ミニマかな～やっぱり",
        f"ミニマとか使ってるやつおる？？？",
        f"ﾋﾟﾛﾋﾟﾛﾘｰﾝ！ｷﾞｭｲﾝｷﾞｭｲﾝｷﾞｭｲﾝｷﾞｭｲﾝｷﾞｭｲｰｰｰﾝ！！！\nドン！(右から)\nドン！(左から)\nゴゴゴゴゴ！！！(奥から)\nス パ イ ク ラ ッ シ ュ 確 ☆ 定(極太明朝虹色文字)",
        f"ヨルはイニシエーターだよ。",
        f"ホウント「目が合ったな！これでお前とも縁ができた！(位置特定)」",
        f"アラームボット展開！",
        f"ボットを戻すよ",
        f"セントリー設置！",
        f"ﾎﾞｯﾄﾁｬﾝがやられた！",
        f"カウントダウン開始！",
        f"ﾎﾞｯﾄﾁｬﾝがやられた！\n...いや、なんでもない。",
        f"マーシャルを信じなさい。",
        f"マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。マーシャルを信じなさい。",
        f"140カット！！！！！！！！！！！！！！！！！！！！！(キレ)",
        f"ピュレグミうめ～",
        f"俺がハンターだ！",
        f"ワイがハンターや！",
        f"俺がハンターか？",
        f"俺がガンダムだ！",
        f"お前がハンターだ！",
        f"もうお前がハンターでいいよ",
        f"ヌベヂョンヌゾジョンベルミッティスモゲロンボョｗｗｗｗｗｗイヒーｗｗイヒヒｗ└(՞ةڼ◔)」",
        f"ンゴッ！？",
        f"なるほどﾆｬﾝｷｬｯﾂ",
        f"ンゴロンゴロ",
        f"綾鷹 茶葉の甘みを飲みましょう。",
        f"ンゴネミ",
        f"3550カット！！！！！！！！！！！！！！",
        f"夏はこれ使う笑",
        f"タンヤオ"
    ]
    choice = random.choice(ngo)
    await ctx.response.send_message(f"{choice}"),


@tree.command(
    name = "map",
    description= "マップをランダムに選択します。"
)
@discord.app_commands.guilds(
    discord.Object(id = guildid)
)
#@discord.app_commands.describe(banmap = "除外するマップを選択します。")
#banmap:str = None
async def map(ctx: discord.Interaction):
    
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



class Mode(enum.Enum):
    デュエリストのみ = "デュエリスト"
    コントローラーのみ = "コントローラー"
    イニシエーターのみ = "イニシエーター"
    センチネルのみ = "センチネル"
    ロールで抽選 = "ロールで抽選"

@tree.command(
    name = "agent",
    description = "エージェントを抽選します。modeを使用してロール限定抽選、ロールの抽選が可能です。"
    )
@discord.app_commands.describe(
    mode="抽選モードを変更します。"
)
@discord.app_commands.guilds(
    discord.Object(id = guildid)
)
async def agt(ctx: discord.Interaction, mode:Mode = None):
    
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
    due = [ "ジェット", "ネオン", "フェニックス", "ヨル", "レイズ", "レイナ" ]
    con = [ "アストラ", "ヴァイパー", "オーメン", "ハーバー", "ブリムストーン" ]
    ini = [ "KAY/O", "スカイ", "ソーヴァ", "フェイド", "ブリーチ" ]
    sen = [ "キルジョイ", "サイファー", "セージ", "チェンバー" ]
    role = [ "デュエリスト", "イニシエーター", "コントローラー", "センチネル" ]

    if mode == Mode.デュエリストのみ:
        agt = due
        cond = cond_head + "デュエリスト" + cond_foot

    elif mode == Mode.コントローラーのみ:
        agt = con
        cond = cond_head + "コントローラー" + cond_foot

    elif mode == Mode.イニシエーターのみ:
        agt =ini
        cond = cond_head + "イニシエーター" + cond_foot

    elif mode == Mode.センチネルのみ:
        agt =sen
        cond = cond_head + "センチネル" + cond_foot
    else:
        agt =all
        cond = ""
    
    choice = random.choice(agt)
    r_role = random.choice(role)
    
    if mode == Mode.ロールで抽選:
        mes = f"次の{ctx.user.mention}のロールは「**{r_role}**」だよ！{cond}"
    else:
        mes = f"次の{ctx.user.mention}のエージェントは「**{choice}**」だよ！{cond}"

    await ctx.response.send_message(f"{mes}"),


@tree.command(
    name="wpn"
    )
@discord.app_commands.guilds(
discord.Object(id = guildid)
)
async def wpn(ctx: discord.Interaction):
    
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
    await ctx.response.send_message(f"次の{ctx.user.mention}の武器は「**{choice}**」だよ！"),


@tree.command(name="soyjoy")
async def sj(ctx: discord.Interaction):
    
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
#    
#    agtd = ["ジェット","ネオン","フェニックス","ヨル","レイズ","レイナ"]
#    choice = random.choice(agtd)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="agt.i")
#async def agt(ctx):
#    
#    agt = ["KAY/O","スカイ","ソーヴァ","フェイド","ブリーチ"]
#    choice = random.choice(agt)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="agt.c")
#async def agt(ctx):
#    
#    agt = ["アストラ","ヴァイパー","オーメン","ハーバー","ブリムストーン"]
#    choice = random.choice(agt)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="agt.s")
#async def agt(ctx):
#    
#    agt = ["キルジョイ","サイファー","セージ","チェンバー"]
#    choice = random.choice(agt)
#    await ctx.reply(f"次の{ctx.message.author.name}のエージェントは「**{choice}**」だよ！")

#@bot.command(name="wpn.s")
#async def wpns(ctx):
#    
#    wpns = ["クラシック","ショーティー","フレンジー","ゴースト","シェリフ"]
#    choice = random.choice(wpns)
#    await ctx.reply(f"次の{ctx.message.author.name}のセカンダリは「**{choice}**」だよ！"),


#@bot.command(name="wpn.p")
#async def wpnp(ctx):
#    
#    wpnp = ["スティンガー","スペクター","バッキー","ジャッジ","ブルドッグ","ガーディアン","ファントム","ヴァンダル","マーシャル","オペレーター","アレス","オーディン"]
#    choice = random.choice(wpnp)
#    await ctx.reply(f"次の{ctx.message.author.name}のプライマリは「**{choice}**」だよ！"),

client.run(token)
