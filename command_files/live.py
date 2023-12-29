import define_first as I

class LiveMode(I.enum.Enum):
  START = "START"
  END = "END"


@I.tree.command(name="live", description="ライブの設定をします。")
@I.discord.app_commands.describe(stream="配信状態を変更します。",
                               url="配信のURLを添付します。ライブスタート時のみ有効です。")
@I.discord.app_commands.checks.cooldown(2, 600, key=None)
@I.discord.app_commands.guilds(I.discord.Object(id=I.guildid))
async def live(ctx: I.discord.Interaction, stream: LiveMode, url: str = None):
  print("")
  print(f"=== send by {ctx.user} ===")
  print("[ live setting up... ]")

  #🔴
  uniemoji_RC = "\N{Large Red Circle}"
  print("live > Load: Emoji[RC] ")

  #⚫
  uniemoji_BC = "\N{Medium Black Circle}"
  print("live > Load: Emoji[BC] ")

  editchannel = I.client.get_channel(1054417954038632578)
  print("live > set: editchannel")

  sendchannel = I.client.get_channel(1053725844448739398)
  print("live > set: sendchannel")

  topic = I.client.get_stage_instance(1054417954038632578)
  print("live > set: topic")

  C_START = f"𝗟𝗜𝗩𝗘：{uniemoji_RC}ONLINE"
  C_END = f"𝗟𝗜𝗩𝗘：{uniemoji_BC}𝗢𝗙𝗙𝗟𝗜𝗡𝗘"

  if url == None:
    CommandName = f"/live stream:{stream.name}"
  else:
    CommandName = f"/live stream:{stream.name} url:{url}"

  if url == "//debug":
    print("[[[ debug mode ]]]")

    if stream == LiveMode.START:
      print("LiveMode.START")

      if editchannel.name == C_START:
        CmdState = False
        print(f"CmdState:{CmdState}")

      elif editchannel.name == C_END:  #success
        CmdState = True
        print(f"CmdState:{CmdState}")

    elif stream == LiveMode.END:
      print("LiveMode.END")

      if editchannel.name == C_START:  #success
        CmdState = True
        print(f"CmdState:{CmdState}")

      elif editchannel.name == C_END:
        CmdState = False
        print(f"CmdState:{CmdState}")

    livedev = I.discord.Embed(title="Debug Mode",
                            description=f"CMD: {CommandName}",
                            color=0xffff00)
    print("embed create 10%")
    livedev.add_field(name="LiveMode:", value=f"{stream.name}", inline=False)
    print("embed create 20%")
    livedev.add_field(name="Now Status Channel Name:",
                      value=f"{editchannel.name}",
                      inline=False)
    print("embed create 30%")
    livedev.add_field(name="Status Channel ID:",
                      value=f"{editchannel.id}",
                      inline=False)
    print("embed create 40%")
    livedev.add_field(name="Notification Channel Name:",
                      value=f"{sendchannel.name}",
                      inline=False)
    print("embed create 50%")
    livedev.add_field(name="Notification Channel ID:",
                      value=f"{sendchannel.id}",
                      inline=False)
    print("embed create 60%")
    if topic == None:
      livedev.add_field(name="Now Instance:", value="None")
    else:
      livedev.add_field(name="Now Instance:", value=f"{topic.topic}")
    print("embed create 70%")
    livedev.add_field(name="This Channel Name is:",
                      value=f"{ctx.channel.name}",
                      inline=False)
    print("embed create 80%")
    livedev.add_field(name="This Channel ID is:",
                      value=f"{ctx.channel.id}",
                      inline=False)
    print("embed create 90%")
    livedev.add_field(name="Edit Result Prediction: ",
                      value=f"{CmdState}",
                      inline=False)
    print("embed create 100%")

    await ctx.response.send_message(embed=livedev, ephemeral=True)
    print("embed send")

  else:
    print("= stream mode check ============================================")
    # START ######################################################################
    if stream == LiveMode.START:
      print("live > if : [START]")

      Cname = f"{C_START}"
      print("live:START > 'Cname' wrote.")

      if editchannel.name == Cname:
        liveError = 1
        print("live > error : 1")
      else:
        await ctx.response.defer()
        print("live > Defer ok.")

        if url == None:
          Cmes = f"{uniemoji_RC}：**{ctx.user.mention}がライブ配信中！**"
          print(f"live:START > 'Cmes' wrote. Message:{url}")
        else:
          Cmes = f"{uniemoji_RC}：**{ctx.user.mention}がライブ配信中！**\r\n{url}"
          print(f"live:START > 'Cmes' wrote. Message:{url}")

        mes = f"{uniemoji_RC}：サーバーの配信ステータスがオンラインになりました。"
        print("live:START > Live starting...")

        if topic == None:
          await editchannel.create_instance(topic=(f"{ctx.user.nick}のライブ"))
          print("live:START > topic edited.")
          liveError = -1
        else:
          return

    # END ######################################################################
    elif stream == LiveMode.END:
      print("live > if check ok : END")

      Cname = f"{C_END}"
      print("live:END > 'Cname' wrote.")

      if editchannel.name == Cname:
        liveError = 2
        print("live > error : 2")
      else:
        await ctx.response.defer()
        print("live > Defer ok.")

        if topic == None:
          Cmes = f"{uniemoji_BC}：**ライブは終了しました。**"
          print(f"live:END > 'Cmes' wrote.(topic:{topic})")
        else:
          Cmes = f"{uniemoji_BC}：**{topic.topic}は終了しました。**"
          print(f"live:END > 'Cmes' wrote.(topic:{topic})")

        mes = f"{uniemoji_BC}：サーバーの配信ステータスがオフラインになりました。"
        print("live:END > Live stopping...")

        if not topic == None:
          await topic.delete()
          print("live:END > Topic deleted.")
          liveError = -1
        else:
          print(
            "live:END > This command was ignored because the topic was None.")

    # Other ######################################################################
    else:
      liveError = 0
      print("live > error : 3")

  if 0 <= liveError <= 2:
    if liveError == 0:
      ErrorType = "コマンドに誤りがあるか、システムに異常があります。"
    elif liveError == 1:
      ErrorType = "既に配信ステータスがオンラインになっています。"
    elif liveError == 2:
      ErrorType = "既に配信ステータスがオフラインになっています。"

    await ctx.followup.send(f"{ErrorType}")

  else:
    print("================================================================")
    print("live > Live ready...")

    await ctx.followup.send(f"{mes}")
    print("live > FollowUp ok.")

    await sendchannel.send(f"{Cmes}")
    print("live > Info send ok.")

    if not editchannel.name == Cname:
      await editchannel.edit(name=Cname)
      print("live > Ch-name edit ok.")
    else:
      print("live > Ch-name passed.")

  print("[Command is completed.]")
  print("")