import requests, json, time
from datetime import datetime, timedelta
from krx_crawler import krx_oneday_toojaja
import time, re
import os, glob, json
from ToolBox import dict_to_file
from telebot import bot




## 파일 날짜가 어제 보다 전인 경우
while True:
    try:
        list_0 = glob.glob(f'data/date/*')
        list = []
        for i in list_0:
            list.append(os.path.basename(i).replace('toojaja', '').replace('.csv', ''))  # 파일 이름에서 날짜만 추림
        latest = max(list)
        if datetime.strptime(latest,'%Y%m%d') < (datetime.today() - timedelta(days=1)).replace(hour=0,minute=0,second=0,microsecond=0):
            d_day = (datetime.strptime(latest,'%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')
            # print(datetime.strptime(latest, '%Y%m%d'))
            # print(datetime.today() - timedelta(days=1))
            # print(d_day)
            dics = krx_oneday_toojaja(d_day)
            # print(dics)
            # if dics != None:
            dict_to_file(dics, f"toojaja{d_day}")
            # else:
            #     print(f"{d_day} 없음")
            time.sleep(10)
        else:
            bot(message="시간 다됨. 봇 종료")
            break
    except:
        bot(message="오류발생")

bot(message="봇 종료")
# print(datetime.today() - timedelta(days=1))