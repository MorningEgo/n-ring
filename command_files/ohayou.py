import define as I
import locale
@I.tree.command(name="おはよう", description="起きます")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def challenge(ctx:I.discord.Interaction, comment:str = None):
    
    weekjp = ["月","火","水","木","金","土","日"]
    JST = I.timezone(I.timedelta(hours=+9), 'JST')
    now = I.datetime.now(JST)
    Week = I.datetime.date.weekday()
    weekday = weekjp[Week]
    nowstr = I.datetime.strptime(now, f'%B%d日({weekday}) %H時%M分%S秒')
    E = I.discord.Embed(
        title = "おきました",
        description = f"{nowstr}に起きました"
    )
    E.set_thumbnail(url="https://cdn.discordapp.com/attachments/1071319610550399036/1167499500722597908/646_20220307080036.png")
    
    if comment is not None:
        E.add_field(
            name = "ひとこと",
            value = comment
        )
    ##### user_data #####
    # # 読み込み
    #   with open('nring_storage/n_users/user_data.json', 'r') as __e__:
    #        = json.load(__e__)
    #   ohayou_count = _v[ohayou_count] + 1
    # 書き込み #
    #####################
    await ctx.response.send_message(embed=E)