import define as I

@I.tree.error
async def o_e(ctx: I.discord.Interaction, error: I.app_commands.AppCommandError):
	if isinstance(error, I.app_commands.CommandOnCooldown):
		retry_after_int = int(error.retry_after)
		retry_hour = retry_after_int // 3600
		retry_minute = retry_after_int // 60
		retry_second = retry_after_int % 60
		
		print(f"live > Cooldown now. End is [{retry_hour}:{retry_minute}:{retry_second}]")
		
		_ = [
			"んごりンゴは寝ているようだ。",
			"んごりンゴはなぜか拗ねているようだ。",
			"んごりンゴはカレーを食べているようだ。",
			"んごりンゴはテンションブチアゲで曲を聴いているようだ。",
			"しかし だれもこなかった。",
			"んごりンゴはお疲れのようだ。",
			"「旅に出ています  探さないでください」と書かれた看板がある。...どうやら居留守のようだ。",
			"あっっっっっっっコラッッッッッッッッッッッ！！！！！！！！！！！！！！！\n\n\n\n\n...うざいイヌがコマンドをくわえてどこかへ行ってしまった。",
			"瞑想をする時間だ。瞑想をしてから",
			"んごりンゴは金庫にリンゴとパン粉を入れたバンドの簡素なハンコが何個か参考にしている。は？\nそれはともかく、",
			"Just Ngoringo.  ",
			"んごりンゴという現象は、仮定された有機交流電燈のひとつの緑色の照明です(あらゆる透明な情報の複合体)。つまるところ、",
			"「　　　　　」は落とした名前を探している。",
			"クールタイムのようだ。"
		]
		c = I.random.choice(_)
		await ctx.followup.send(f"({c}{str(retry_hour)}時間{str(retry_minute)}分{str(retry_second)}秒後にまた訪ねてみよう...")
		
	else:
		await ctx.followup.send(f"なんかエラーが起きたみたい。\n```\nError:\n{str(error)}```")
		