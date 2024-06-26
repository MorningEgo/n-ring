import define_first as I
from command_files.ngold.ngolds import *
from command_files.ngold.embed import *

@I.tree.command(
        name="チンチロ",
        description="チンチロをします。"
        # サイコロを3つ振って役を狙うゲームです。
        # ＝＝＝＝＝＝＝＝｝出　　目　　一　　覧｛＝＝＝＝＝＝＝＝＝ #
        # 　役　名　：　　　　　　出　　目　　　　　　：　配　当　　 #
        # 強～～～～～～～～～～～～～～～～～～～～～～～～～～～強 #
        # ｜ピンゾロ：全て１の目　　　　　　　　　　　：５倍もらう｜ #
        # ｜ゾロ目　：全て１以外の同じ目　　　　　　　：３倍もらう｜ #
        # ｜シゴロ　：４５６　　　　　　　　　　　　　：２倍もらう｜ #
        # ｜役あり　：同じ目が２つ（残りの１つが出目）：等倍もらう｜ #
        # ｜役なし　：全て違う目　　　　　　　　　　　：等倍はらう｜ #
        # ｜ヒフミ　：１、２、３　　　　　　　　　　　：２倍はらう｜ #
        # 弱～～～～～～～～～～～～～～～～～～～～～～～～～～～弱 #
        # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ #
)
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
@I.discord.app_commands.checks.cooldown(1, 5)
@I.discord.app_commands.describe(bet = "賭けるNgoldの数。0で賭けずにプレイします。")
async def ceelo(ctx: I.discord.Interaction, bet: int):
    await ctx.response.defer(thinking=True)
    data = ng_watch(userid=ctx.user.id)
    ngcheck = int(0)

    bet_min = int(0)
    bet_max = int(1000000)
    
    ng_errormes()
    errorcheck = True
    
    if bet < bet_min:
        result = ng_errormes(5,"bet",bet_min)
        errorcheck = True
    elif bet > 0:
        if data[0] == 0:
            result = ng_errormes(2)
            errorcheck = True
        elif data[0] < 0:
            result = ng_errormes(3)
            errorcheck = True
        elif data[0] < bet:
            result = ng_errormes(4)
            errorcheck = True
        elif bet_max < bet:
            result = ng_errormes(8,"bet",bet_max)
            errorcheck = True
        else:
            errorcheck = False
    else:
        errorcheck = False
        
    if errorcheck is False:
        result = I.discord.Embed(title=f"チンチロ！！せーの！！", )
        #| None=目無し | 1~6=目あり | 11~16=ゾロ目 | 0=ヒフミ | 9=シゴロ |#
        player = f""
        roll = 0
        player_try = {
            1:[],
            2:[],
            3:[],
        }
        for i in range(3):
            roll = i + 1
            ceelo_roll_a = I.random.randint(1, 6)
            ceelo_roll_b = I.random.randint(1, 6)
            ceelo_roll_c = I.random.randint(1, 6)
            ceelo_l = [ceelo_roll_a,ceelo_roll_b,ceelo_roll_c]
            ceelo_l.sort()
            print(ceelo_l)

            player_try[roll] = []
            for i in range(3):
                player_try[roll].append(str(ceelo_l[i]))
            print(str(player_try[roll]))
            

            if ceelo_roll_a==ceelo_roll_b!=ceelo_roll_c:
                player = f"役あり「**{ceelo_roll_c}**」！"
                if not bet == 0:
                    ngcheck = 0
                break
            elif ceelo_roll_b==ceelo_roll_c!=ceelo_roll_a:
                player = f"役あり「**{ceelo_roll_a}**」！"
                if not bet == 0:
                    ngcheck = 0
                break
            elif ceelo_roll_a==ceelo_roll_c!=ceelo_roll_b:
                player = f"役あり「**{ceelo_roll_b}**」！"
                if not bet == 0:
                    ngcheck = 0
                break
            elif ceelo_roll_a==ceelo_roll_b==ceelo_roll_c==1:
                player = f"「**ピンゾロ**」！！！！"
                if not bet == 0:
                    ngcheck = bet*5
                break
            elif ceelo_roll_a==ceelo_roll_b==ceelo_roll_c:
                player = f"ゾロ目！「{ceelo_roll_a}」！！！"
                if not bet == 0:
                    ngcheck = bet*3
                break
            elif ceelo_l==[1,2,3]:
                player = f"「**ヒフミ**」！よわ！！！！！"
                if not bet == 0:
                    ngcheck = -bet*2
                
                break
            elif ceelo_l==[4,5,6]:
                player = f"「**シゴロ**」！！"
                if not bet == 0:
                    ngcheck = bet*2
                break
            else:
                player = "「**役なし**」！よわ！！"
                if not bet == 0:
                    ngcheck = -bet
            

        try_1 = '・'.join(player_try[1])
        if roll == 1:
            dl = f"一回目！「`{try_1}`」！\n\n\n{player}"
        elif roll == 2:
            try_2 = '・'.join(player_try[2])
            dl = f"一回目！「`{try_1}`」！\n二回目！「`{try_2}`」！！\n\n\n{player}"
        else:
            try_2 = '・'.join(player_try[2])
            try_3 = '・'.join(player_try[3])
            dl = f"一回目！「`{try_1}`」！\n二回目！「`{try_2}`」！！\n三回目！「`{try_3}`」！！！\n\n\n{player}"
        
        if bet > 0:
            result.set_footer(text=f"ベット額：{bet} ng")
        result.add_field(name="なにがでたかな", value=f"{dl}", inline=True)
    

    await ctx.followup.send(embed=result)
    ngcheck == int(ngcheck)
    if not ngcheck == 0:
        if ngcheck > 0:
            ng_add(userid=ctx.user.id,supplier=I.client.user.id,ng=ngcheck)
            ng_embed = ng_receive_embed(send=I.client.user,receive=ctx.user,value=ngcheck)
            
        elif ngcheck < 0:
            ng_remove(userid=ctx.user.id,buyer=I.client.user.id,ng=-ngcheck)
            ng_embed = ng_send_embed(send=ctx.user,receive=I.client.user,value=-ngcheck)
        
        await ctx.followup.send(embed=ng_embed)