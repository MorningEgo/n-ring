import define_first as I
import json
from discord.ext import tasks
  
from command_files.cl.role.edit import cl_loop
JST = I.timezone(I.timedelta(hours=+9), 'JST')
  
  
@tasks.loop(seconds = 1)
async def loop_1s():
  now_s = I.datetime.now(JST).strftime('%S')
  
@tasks.loop(minutes = 1)
async def loop_1m():
  now_m = I.datetime.now(JST).strftime('%M')
  cl_loop
  
@tasks.loop(hours = 1)
async def loop_1h():
  now_h = I.datetime.now(JST).strftime('%H')
  ...