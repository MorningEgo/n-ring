import define as I


####################################################################
# セットアップ
from command_files import _ready
_ready

####################################################################
# Test
from command_files import testcm
testcm

####################################################################
# ライブモード
from command_files import live
live

####################################################################
# 雑談
from command_files import talk
talk

####################################################################
# マップ選択
from command_files import map
map

####################################################################
# valo エージェント抽選, 武器抽選
from command_files.valorant import valo_agent, valo_weapons
valo_agent
valo_weapons

####################################################################
# ソイジョイ
from command_files import soyjoy
soyjoy

####################################################################
# イカブキ抽選
from command_files.splatoon import sp3_weapons
sp3_weapons

####################################################################
# team
from command_files import team
team

####################################################################
# サイコロ
from command_files import dice
dice

####################################################################
# CL用：ロール設定変更
from command_files.cl import cl
from command_files.cl.role import edit, delete, remove
cl
edit
delete
remove

####################################################################
# 初心者カスタム用
from command_files.beginner_custom import scteam, scmap
scteam
scmap

####################################################################
# エラー
#from command_files import _error
#_error

####################################################################
# token
try:
  I.keep_alive()
  I.client.run(I.token)
except Exception as e:
  print(str(e))
  I.os.system("kill 1")