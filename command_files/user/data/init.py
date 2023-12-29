import define_first as I
import json
from activities import N_001

class n_userdata:
    def __init__(self, user_id, ):
        JST = I.timezone(I.timedelta(hours=+9), 'JST')
        raw_nowtime = I.datetime.now(JST)


        with open('nring_storage\n_users\user_data.json', 'r') as __e__:
            users_data = json.load(__e__)
        
        for _k, _v in list(users_data.items()):
            temp = _v["temp"]
            if user_id is not _k:
                data_imput = {id : temp}
                users_data.update(data_imput)
                with open('nring_storage\n_users\user_data.json', 'w') as __e__:
                    json.dump(data_imput, __e__, indent=4)

            ## 目と目が合ったので活動を記録
            N_001.set(id=id)
            
            break
    
    def open():
        with open('nring_storage\n_users\user_data.json', 'r') as __e__:
            users_data = json.load(__e__)

        for _k, _v in list(users_data.items()):
            temp = _v["temp"]
            if id is _k:
                ...

    def set():
        upd.update(ipt)
        with open('nring_storage\n_users\user_data.json', 'w') as __e__:
            json.dump(ipt, __e__, indent=4)


    
    