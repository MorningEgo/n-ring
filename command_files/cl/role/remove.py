import define as I
from define import json
from storages.cl.cl_editable import cl_editable
from storages.cl.cl_list import cl_list
from discord.ext import tasks
from command_files.cl.cl import R

@R.command(name="remove_user", description="全てのユーザーから指定したロールを外します。ユーザーを指定すると、そのユーザーのロールのみを外します。")
async def remove(ctx: I.discord.Interaction, role: I.discord.Role, user: I.discord.User = None, schedule: str = None):
	...