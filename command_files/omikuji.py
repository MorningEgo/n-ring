import define_first as I
from define_first import json
from nring_storage import omikuji_list as o_list
from command_files.ngold.ngolds import *
from command_files.ngold.embed import *


@I.tree.command(name="ンゴみくじ", description="今日のンゴみくじを引くよ\nお布施してないんだから、当たらなくても文句言わないでよね！")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
@I.discord.app_commands.checks.cooldown(10, 300)
async def omikuji(ctx:I.discord.Interaction, ):
    await ctx.response.defer(thinking=False)
    ###################################################
    file_path = 'nring_storage/ngo_data.json'
    # 読み込み
    with open(file_path, 'r') as __e__:
        ngo_data = json.load(__e__)
    ###################################################
    
    Key_Scale = o_list.Key_Scale
    Lucky_Weight = o_list.Lucky_Weight
    Key_Items = o_list.Items
    Key_Names = o_list.Key_Names
    
    key_Wish = Key_Items['Wish']
    key_Lost = Key_Items['Lost']
    key_Travel = Key_Items['Travel']
    key_Business = Key_Items['Business']
    key_Study = Key_Items['Study']
    key_Dispute = Key_Items['Dispute']
    key_Draw = Key_Items['Draw']
    key_Aim = Key_Items['Aim']
    key_Direction = Key_Items['Direction']

    ngo_data['omikuji']['roll'] = ngo_data['omikuji']['roll'] + 1
    ngo_data['omikuji']['musubi']['target_number'] = ngo_data['omikuji']['musubi']['target_number'] - 1
    
    item_levels = []

    # 確定演出チェック
    if ngo_data['omikuji']['musubi']['target_number'] == 0:
        ngo_data['omikuji']['musubi']['musubi_count'] = ngo_data['omikuji']['musubi']['musubi_count'] + 1
        ngo_data['omikuji']['musubi']['target_number'] = I.random.randrange(start=30,stop=77)
        musubi = True
        choice = o_list.jack_ngo
        c = [0,0,5,10,10]
        jc = I.random.choice(c)
        item_levels = [jc,jc,jc,jc,jc,jc,jc,jc]
    else:
        musubi = False
        ngo = o_list.ngo
        choice = I.random.choice(ngo)
        c = range(0,11)
        item_levels = I.random.choices(c,k= 8, weights = Lucky_Weight)

    # 総評用合計
    key_score = 0
    for i in item_levels:
        key_score = key_score + i
    print(f"item_levels = {item_levels}")
    print(f"key_score = {key_score}")
    
    # 総評判定
    n = 0
    match_scale = 0
    for i in range(8):
        print(f"i = {i}")
        if Key_Scale[n][1] is -1:
            if key_score == Key_Scale[n][2]:
                Lack_scale = Key_Scale[n][0]
                match_scale = i
                print("ok")
                break
            else:
                print(1)
        elif Key_Scale[n][2] is -1:
            if Key_Scale[n][1] == key_score:
                Lack_scale = Key_Scale[n][0]
                match_scale = i
                break
            else:
                print(2)
                print(Key_Scale[n][0])
                print(match_scale)
        else:
            if Key_Scale[n][1] <= key_score <= Key_Scale[n][2]:
                Lack_scale = Key_Scale[n][0]
                match_scale = i
                break
            else:
                print(3)
        n = n + 1
    print(f"Lack_scale = {Lack_scale}")
    # 吉方追加
    item_levels.extend(I.random.choices(range(0,18)))
    
    # 各項目のカウント追加
    if match_scale == 0:
        ngo_data['omikuji']['Luck_00'] = ngo_data['omikuji']['Luck_00'] + 1
    elif match_scale == 1:
        ngo_data['omikuji']['Luck_01'] = ngo_data['omikuji']['Luck_01'] + 1
    elif match_scale == 2:
        ngo_data['omikuji']['Luck_02'] = ngo_data['omikuji']['Luck_02'] + 1
    elif match_scale == 3:
        ngo_data['omikuji']['Luck_03'] = ngo_data['omikuji']['Luck_03'] + 1
    elif match_scale == 4:
        ngo_data['omikuji']['Luck_04'] = ngo_data['omikuji']['Luck_04'] + 1
    elif match_scale == 5:
        ngo_data['omikuji']['Luck_05'] = ngo_data['omikuji']['Luck_05'] + 1
    elif match_scale == 6:
        ngo_data['omikuji']['Luck_06'] = ngo_data['omikuji']['Luck_06'] + 1
    elif match_scale == 7:
        ngo_data['omikuji']['Luck_07'] = ngo_data['omikuji']['Luck_07'] + 1
    
    # 各項目の内容書き込み
    omikuji_num = ""
    for i in item_levels:
        print(f"i ={i}")
        if int(i) < 10:
            omikuji_num = omikuji_num + str(f"0{i}")
        else:
            omikuji_num = omikuji_num + str(f"{i}")

    # 演出
    rolling = I.discord.Embed(
        title="おみくじを抽選中・",
        description = choice,
        color = 0xafed2f
        )
    await ctx.followup.send(embed=rolling)
    I.sleep(0.75)
    rolling = I.discord.Embed(
        title="おみくじを抽選中・・",
        description = choice,
        color = 0xafed2f
        )
    await ctx.edit_original_response(embed=rolling)
    I.sleep(0.75)
    rolling = I.discord.Embed(
        title="おみくじを抽選中・・・",
        description = choice,
        color = 0xafed2f
        )
    await ctx.edit_original_response(embed=rolling)
    I.sleep(0.75)


    # Embed
    # 確変チェック
    if musubi is False:
        roll = I.discord.Embed(
            title = f"˙ : .  お み【　{Lack_scale}　】く じ  . : ˙",
            description = f"第{ngo_data['omikuji']['roll']}番",
            color = 0xafed2f
        )
    else:
        roll = I.discord.Embed(
            title = f"˙ : .  お み【　{Lack_scale}　】く じ  . : ˙",
            description = f"第{ngo_data['omikuji']['roll']}番",
            color = 0xedeb2f
        )

    roll.add_field(
        name = Key_Names[0],
        value = key_Wish[item_levels[0]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[1],
        value = key_Lost[item_levels[1]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[2],
        value = key_Travel[item_levels[2]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[3],
        value = key_Business[item_levels[3]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[4],
        value = key_Study[item_levels[4]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[5],
        value = key_Dispute[item_levels[5]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[6],
        value = key_Draw[item_levels[6]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[7],
        value = key_Aim[item_levels[7]] + "\n\_\_\_\_\_\_"
    )
    roll.add_field(
        name = Key_Names[8],
        value = key_Direction[item_levels[8]] + "\n\_\_\_\_\_\_"
    )
    roll.set_author(
        name = ctx.user.display_name,
        icon_url = ctx.user.display_avatar.url
    )
    await ctx.edit_original_response(embed=roll)
    print(f"{omikuji_num}番")


    ng = Key_Scale[n][3]
    if ng > 0:
        ng_add(userid=ctx.user.id,supplier=I.client.user.id,ng=ng)
        ng_embed = ng_receive_embed(send=I.client.user,receive=ctx.user,value=ng)
    if ng < 0:
        ng_remove(userid=ctx.user.id,buyer=I.client.user.id,ng=-ng)
        ng_embed = ng_send_embed(send=ctx.user,receive=I.client.user,value=-ng)

    await ctx.followup.send(embed=ng_embed)
    

    ###################################################
    # 書き込み
    ngo_data.update(ngo_data)
    with open(file_path, 'w') as __e__:
        json.dump(ngo_data, __e__, indent=4)
    ###################################################