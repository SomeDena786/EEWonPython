#モジュールの読み込み
import datetime
from os import defpath
import requests
import json
import time

#URL用時刻の取得
def timegene():
    dt = datetime.datetime.now()
    date_time_url_int = dt.second + dt.minute*100+dt.hour*10000+dt.day*1000000+dt.month*100000000+dt.year*10000000000 
    date_time_url=str(date_time_url_int)
    return date_time_url


#URLの生成
def urlgene():
    url="http://www.kmoni.bosai.go.jp/webservice/hypo/eew/"  + timegene() + ".json"
    return url

#jsonの取得
def jsons ():
    response = requests.get(urlgene())
    res = requests.get(urlgene())
    data = res.json()
    return data



#jsonのステータスを確認
def jsonmessage():
    data=jsons()
    result_data = data["result"]
    result_status_data=result_data["message"]
    return result_status_data

#緊急地震速報の詳細を取得するひな形
def quakestadef(status):
    data=jsons()
    return_data=data[status]
    return return_data



def quakesta():
    #グローバル変数宣言
    global origin_time
    global magunitude
    global latitude
    global longitude
    global region_name
    global report_num
    global depth 
    global is_final
    #ステータスを変数に代入
    origin_time=quakestadef("origin_time")
    magunitude=quakestadef("magunitude")
    latitude=quakestadef("latitude")
    longitude=quakestadef("longitude")
    region_name=quakestadef("region_name")
    report_num=quakestadef("report_num")
    depth=quakestadef("depth")
    is_final=quakestadef("is_final")

quakesta()
print(origin_time)

#緊急地震速報が発表されているか(メッセージが「データがありません」でないか)
def EEWdoing():
    if jsonmessage() != "データがありません":
        print("緊急地震速報が発表されました")
        print("マグニチュードは"+str(magunitude)+"です")

while True:
    jsonmessage()
    EEWdoing()



