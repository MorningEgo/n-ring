import define_first as I
from define_first import pd
from typing import *

FILE_PATH = 'nring_storage/n_users/ng_storage.csv'

def ng_read(userid : int|list[int]|None):
    """
    CSVデータを読み込む。

    Parameters
    ----------
    userid : `int`
        データを作成するユーザーのID。
    """
    from define_first import pd
    print(f"\033[32m<<[ Ngolds ]>>\033[0m loading csv...")
    try:
        df = pd.read_csv(FILE_PATH, encoding="utf-8", index_col= 'ids', header = 0)
        print(f"\033[32m<<[ Ngolds ]>>\033[0m Successfully loaded.")
        print(df)
        if not userid is None:
            print(f"\033[32m<<[ Ngolds ]>>\033[0m userid Checking now...")
            if type(userid) == list:
                print(f"\033[32m<<[ Ngolds ]>>\033[0m userid is list.")
                size = userid
            elif type(userid) == int:
                print(f"\033[32m<<[ Ngolds ]>>\033[0m userid is int.")
                size = [userid]
            for i in size:
                print(f"\033[32m<<[ Ngolds ]>>\033[0m Checking id {i}.")
                ids_i = f"i{i}"
                if not ids_i in df.index.values:
                    print(f"\033[33m<<[ Ngolds ]>>\033[0m {i} does not exist in the database. Create data.")
                    ids = f"i{i}"
                    print(f"\033[32m<<[ Ngolds ]>>\033[0m {ids}")
                    new_row = pd.DataFrame({'userid':i,'ng':100,'maxng':100,'deal01':0,'deal01val':0,'deal02':0,'deal02val':0,'deal03':0,'deal03val':0}, index=[ids],dtype='i8')
                    print(f"\033[32m<<[ Ngolds ]>>\033[0m new_row created.")
                    df = pd.concat([df,new_row], ignore_index=False)
                    print(f"\033[32m<<[ Ngolds ]>>\033[0m concated.\n{df}")
                else:
                    print(f"\033[32m<<[ Ngolds ]>>\033[0m id {i} has already been created.")
            try:
                ng_write(export_data=df)
                print(f"\033[32m<<[ Ngolds ]>>\033[0m Successfully created: \n{df}")
            except:
                print(f"\033[31m<<[ Ngolds ]>>\033[0m Failed to Create data.")
        return pd.read_csv(FILE_PATH, encoding="utf-8", index_col= 'ids', header = 0)
    except:
        print(f"\033[31m<<[ Ngolds ]>>\033[0m Failed to load.")
        return pd.read_csv(FILE_PATH, encoding="utf-8", index_col= 'ids', header = 0)


def ng_write(export_data = pd.DataFrame):
    """
    CSVデータを書き込む。

    Parameters
    ----------
    export_data : `dataframe`
        書き込むデータ。
    """
    from define_first import pd
    print(f"\033[32m<<[ Ngolds ]>>\033[0m Exporting csv...")
    print(export_data)
    try:
        export_data.to_csv(FILE_PATH,index_label='ids')
        print(f"\033[32m<<[ Ngolds ]>>\033[0m Exported:\n{export_data}")
    except:
        print(f"\033[33m<<[ Ngolds ]>>\033[0m Export failed:\n{export_data}")
        return ng_read()
    

def ng_add(userid = int, supplier = int, ng = int):
    """
    選択したユーザーのNgoldを増加させる。
    
    Parameters
    ----------
    userid : `int`
        対象のユーザーのユーザーID。
    supplier : `int`
        Ngoldを取引したユーザーID。
    np : `int`
        増加させるNgoldの量。
    """
    from define_first import pd
    # 読み込み
    df = ng_read(userid=userid)
    ids = f"i{userid}"
    
    # データを加算して更新
    df.at[ids,'ng'] += ng
    

    # もし加算後の値が過去一だったら更新
    if df.at[ids,'maxng'] < df.at[ids,'ng']:
        df.at[ids,'maxng'] = df.at[ids,'ng']

    # 書き込み
    ng_write(export_data=df)
    ng_deal_update(userid=userid,new=supplier,value=ng)

    return ng_read(None)


def ng_remove(userid = int, buyer = int, ng = int):
    """
    選択したユーザーのNgoldを減少させる。

    Parameters
    ----------
    userid : `int`
        対象のユーザーのユーザーID。
    buyer : `int`
        Ngoldを取引したユーザーID。
    np : `int`
        減少させるNgoldの量。
    """
    from define_first import pd
    # 読み込み
    df = ng_read(userid=userid)
    ids = f"i{userid}"
    
    # データを減算して更新
    df.at[ids,'ng'] -= ng

    # 書き込み
    ng_write(export_data=df)
    ng_deal_update(userid=userid,new=buyer,value=-ng)

    return ng_read(None)


def ng_reset(userid = int):
    """
    選択したユーザーのNgoldを初期値に戻す。
    (初期値: 1000)

    Parameters
    ----------
    userid : `int`
        対象のユーザーのユーザーID。
    """
    from define_first import pd

    df = ng_read(userid=userid)
    ids = f"i{userid}"
    if userid != I.owner_id:
        df.at[ids,'ng'] == 1000
    else:
        df.at[ids,'ng'] == 99999999999999

    # 書き込み
    ng_write(df)
    return ng_read(None)


def ng_deal_update(userid=int,new=int,value=int):
    """
    選択したユーザーのNgold取引履歴を更新する。

    Parameters
    ----------
    userid : `int`
        対象のユーザーのユーザーID。

    new : `int`
        新たに行った取引の相手のユーザーID。

    value : `int`
        新たに行った取引の額。
        ex. 相手に100ng渡した場合: -100

    """
    from define_first import pd
    df = ng_read(userid=userid)

    ids = f"i{userid}"
    print(f"\033[32m<<[ Ngolds ]>>\033[0m Deal updating...")

    df.at[ids,'deal03'] = df.at[ids,'deal02']
    df.at[ids,'deal03val'] = df.at[ids,'deal02']
    df.at[ids,'deal02'] = df.at[ids,'deal01']
    df.at[ids,'deal02val'] = df.at[ids,'deal01val']
    df.at[ids,'deal01'] = new
    df.at[ids,'deal01val'] = value

    print(f"\033[32m<<[ Ngolds ]>>\033[0m Deal updated:\n{df}")
    # 書き込み
    ng_write(df)
    return ng_read(None)


def ng_watch(userid = int):
    """
    選択したユーザーのNgoldを確認する。

    Parameters
    ----------
    userid : `int`
        対象のユーザーのユーザーID。
    """
    from define_first import pd

    df = ng_read(userid=userid)
    ids = f"i{userid}"
    
    df_ng = df.at[ids,'ng']
    df_max = df.at[ids,'maxng']
    df_deal01 = [df.at[ids,'deal01'],df.at[ids,'deal01val']]
    df_deal02 = [df.at[ids,'deal02'],df.at[ids,'deal02val']]
    df_deal03 = [df.at[ids,'deal03'],df.at[ids,'deal03val']]

    return [df_ng,df_max,df_deal01,df_deal02,df_deal03]