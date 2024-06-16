import define_first as I
from define_first import pd
from .ngolds import *

def ng_send_embed(send:I.discord.User,receive:I.discord.User,value:int):
    id_send = f"i{send.id}"
    data = ng_read(send.id)
    new_send = data.at[id_send,'ng']
    old_send = int(new_send + value)
    

    remove_embed = I.discord.Embed(
        title = "Ngold 利用明細",
        description=f"{send.mention}",
        color= 0xed2f50
    )
    remove_embed.add_field(
        name = f"**{int(old_send)}**ng  >>  **{int(new_send)}**ng",
        value= f"**{receive.display_name}** へ **{value}**ng渡しました。"
    )
    return remove_embed


def ng_receive_embed(send:I.discord.User,receive:I.discord.User,value:int):
    id_receive = f"i{receive.id}"
    data = ng_read(receive.id)
    new_receive = data.loc[id_receive,'ng']
    old_receive = new_receive - value


    add_embed= I.discord.Embed(
        title = "Ngold 利用明細",
        description=f"{receive.mention}",
        color= 0xafed2f
    )
    add_embed.add_field(
        name = f"**{int(old_receive)}**ng  >>  **{int(new_receive)}**ng",
        value= f"**{send.display_name}** から **{value}**ng受け取りました。"
    )
    return add_embed


def ng_watch_embed(user:I.discord.User):
    watch_embed = I.discord.Embed(
        title = f"Ngold My Card : {user.display_name}",
        description="現在のng、最大獲得ng、取引履歴(最大3件まで)を確認します。",
        color= 0xafed2f
    )
    data = ng_watch(user.id)

    df_ng = int(data[0])
    df_max = int(data[1])
    df_deal01_0 = int(data[2][0])
    df_deal01_1 = int(data[2][1])
    df_deal02_0 = int(data[3][0])
    df_deal02_1 = int(data[3][1])
    df_deal03_0 = int(data[4][0])
    df_deal03_1 = int(data[4][1])

    watch_embed.add_field(
        name= "現在の**ng**",
        value= f"**{df_ng}**ng",
        inline=True
    )
    watch_embed.add_field(
        name= "最高記録",
        value= f"**{df_max}**ng",
        inline=True
    )

    if not df_deal01_0 == 0:
        df_deal01_user = I.client.get_user(df_deal01_0)
        watch_embed.add_field(
            name= "直近の取引履歴",
            value= f"取引相手：**{df_deal01_user.display_name}**\n取引額：**{int(df_deal01_1)}**ng",
            inline=False
        )
        if not df_deal02_0 == 0:
            df_deal02_user = I.client.get_user(df_deal02_0)
            watch_embed.add_field(
                name= "一つ前の取引履歴",
                value= f"取引相手：**{df_deal02_user.display_name}**\n取引額：**{df_deal02_1}**ng",
                inline=False
            )
            if not df_deal03_0 == 0:
                df_deal03_user = I.client.get_user(df_deal03_0)
                watch_embed.add_field(
                    name= "二つ前の取引履歴",
                    value= f"取引相手：**{df_deal03_user.display_name}**\n取引額：**{df_deal03_1}**ng",
                    inline=False
                )
            else:
                watch_embed.add_field(
                    name= "二つ前の取引履歴",
                    value= f"`取引がありません`",
                    inline=False
                )
        else:
            watch_embed.add_field(
                name= "一つ前の取引履歴",
                value= f"`取引がありません`",
                inline=False
            )
    else:
        watch_embed.add_field(
            name= "直近の取引履歴",
            value= f"`取引がありません`",
            inline=False
        )
    
    watch_embed.set_author(
        name=user.display_name,
        icon_url=user.avatar.url
    )

    return watch_embed


def ng_errormes(mes=int):
    meslist = [
        "取引相手に自分自身を指定することはできません。",
        "送るngの値は1以上でなければなりません。",
        "あなたはngを所持していません。",
        "負債がある状態でngを送ることはできません。",
        "自身の所持している以上のngを使用することはできません。",
        "ベットは0かそれ以上である必要があります。",
        "ngが足りません。",

    ]

    error = remove_embed = I.discord.Embed(
            title = "Ngold 取引拒否",
            description= meslist[mes],
            color= 0xed2f50
        )
    return error