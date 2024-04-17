import define_first as I
@I.tree.command(name="チンチロ", description="チンチロをします。")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def ceelo(ctx: I.discord.Interaction):
    await ctx.response.defer(thinking=True)

    rolling = I.discord.Embed(title=f"チンチロ！！せーの！！", )
    ceelo_roll_a = I.random.randint(1, 6)
    ceelo_roll_b = I.random.randint(1, 6)
    ceelo_roll_c = I.random.randint(1, 6)
    ceelo_l = [ceelo_roll_a,ceelo_roll_b,ceelo_roll_c].sort()
    
    #| None=目無し | 1~6=目あり | 11~16=ゾロ目 | 0=ヒフミ | 9=シゴロ |#
    player = f""
    roll = 0
    player_try = {
        1:[],
        2:[],
        3:[],
    }
    while player is not None or roll==3:
        roll = roll + 1
        if ceelo_roll_a==ceelo_roll_b!=ceelo_roll_c:
            player = f"役あり！「**{ceelo_roll_c}**」！"
        elif ceelo_roll_b==ceelo_roll_c!=ceelo_roll_a:
            player = f"役あり！「**{ceelo_roll_a}**」！"
        elif ceelo_roll_a==ceelo_roll_c!=ceelo_roll_b:
            player = f"役あり！「**{ceelo_roll_b}**」！"
        elif ceelo_roll_a==ceelo_roll_b==ceelo_roll_c==1:
            player = f"「**ピンゾロ**」！！！！"
        elif ceelo_roll_a==ceelo_roll_b==ceelo_roll_c:
            player = f"ゾロ目！「{ceelo_roll_a}」！！！"
        elif ceelo_l==[1,2,3]:
            player = f"「**ヒフミ**」！よわ！！！！！"
        elif ceelo_l==[4,5,6]:
            player = f"「**シゴロ**」！！"
        else:
            player = None
        
        player_try[roll] = ceelo_l

    if roll == 1:
        dl = f"一回目！{'・'.join(str(player_try[1]))}！\n\n**{str(ceelo_l[0])}**！ **{str(ceelo_l[1])}**！！ **{str(ceelo_l[2])}**！！！\n{player}"
    elif roll == 2:
        dl = f"一回目！{'・'.join(str(player_try[1]))}！二回目！{'・'.join(str(player_try[2]))}！！\n\n**{str(ceelo_l[0])}**！ **{str(ceelo_l[1])}**！！ **{str(ceelo_l[2])}**！！！\n{player}"
    else:
        dl = f"一回目！{'・'.join(str(player_try[1]))}！二回目！{'・'.join(str(player_try[2]))}！！三回目！{'・'.join(str(player_try[3]))}！！！\n\n**{str(ceelo_l[0])}**！ **{str(ceelo_l[1])}**！！ **{str(ceelo_l[2])}**！！！\n{player}"
    
    rolling.add_field(name="なにがでたかな", value=f"{dl}", inline=True)

    await ctx.followup.send(embed=rolling)