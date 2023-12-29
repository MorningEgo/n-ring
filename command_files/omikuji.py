import define as I
from define import json
from nring_storage import omikuji_list as o_list



@I.tree.command(name="ンゴみくじ", description="今日のンゴみくじを引くよ\nお布施してないんだから、当たらなくても文句言わないでよね！*")
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
@I.discord.app_commands.checks.cooldown(1, 10.0, key=None)
async def omikuji(ctx:I.discord.Interaction, view:int = None):
    await ctx.response.defer(thinking=True)

    Key_Scale = o_list.Key_Scale
    Lucky_Weight = o_list.Lucky_Weight
    Key_Items = o_list.Items.values()
    Key_Names = o_list.Key_Names

    ngo = o_list.ngo
    choice = I.random.choice(ngo)
    rolling = I.discord.Embed(
        title="おみくじを抽選中・",
        description = choice,
        color = 0xafed2f
        )
    mes = await ctx.followup.send(embed=rolling)
    I.sleep(1)
    rolling = I.discord.Embed(
        title="おみくじを抽選中・・",
        description = choice,
        color = 0xafed2f
        )
    await ctx.edit_original_response(embed=rolling)
    I.sleep(1)
    rolling = I.discord.Embed(
        title="おみくじを抽選中・・・",
        description = choice,
        color = 0xafed2f
        )
    await ctx.edit_original_response(embed=rolling)
    I.sleep(1)

    item_levels = []
    for i in range(7):
        item_levels.append(I.random.choices(range(0,10), weights = Lucky_Weight))
    
    key_score = sum(item_levels)

    item_levels.append(I.random.choices(range(0,18)))

    key_Wish = Key_Items[0][item_levels[0]]
    key_Lost = Key_Items[1][item_levels[1]]
    key_Travel = Key_Items[2][item_levels[2]]
    key_Business = Key_Items[3][item_levels[3]]
    key_Study = Key_Items[4][item_levels[4]]
    key_Dispute = Key_Items[5][item_levels[5]]
    key_Draw = Key_Items[6][item_levels[6]]
    key_Aim = Key_Items[7][item_levels[7]]
    key_Direction = Key_Items[8][item_levels[8]]

    n = 0
    for i in range(7):
        if Key_Scale[n][1] is None:
            if key_score == Key_Scale[n][2]:
                Lack_scale = Key_Scale[n][0]

        elif Key_Scale[n][2] is None:
            if Key_Scale[n][1] == key_score:
                Lack_scale = Key_Scale[n][0]

        else:
            if Key_Scale[n][1] <= key_score <= Key_Scale[n][2]:
                Lack_scale = Key_Scale[n][0]
        n = n + 1


    for i in item_levels:
        if i < 10:
            omikuji_num = omikuji_num + str(f"0{i}")
        else:
            omikuji_num = omikuji_num + str(f"{i}")


    roll = I.discord.Embed(
        title = f"˙ : .  神【　{Lack_scale}　】籤  . : ˙",
        description = f"{omikuji_num}番",
        color = 0xafed2f
    )
    roll.add_field(
        name = Key_Names[0],
        value = key_Wish
    )
    roll.add_field(
        name = Key_Names[1],
        value = key_Lost
    )
    roll.add_field(
        name = Key_Names[2],
        value = key_Travel
    )
    roll.add_field(
        name = Key_Names[3],
        value = key_Business
    )
    roll.add_field(
        name = Key_Names[4],
        value = key_Study
    )
    roll.add_field(
        name = Key_Names[5],
        value = key_Dispute
    )
    roll.add_field(
        name = Key_Names[6],
        value = key_Draw
    )
    roll.add_field(
        name = Key_Names[7],
        value = key_Aim
    )
    roll.add_field(
        name = Key_Names[8],
        value = key_Direction
    )

    await ctx.edit_original_response(embed=roll)