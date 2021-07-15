import requests, json, time
from datetime import datetime, timedelta


def krx_oneday_toojaja(date_0):
    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '129',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '__smVisitorID=zzDMa_7xp6J; JSESSIONID=RHjpVKktcBKWIba0B25ECPabNdp4mqUFWr1Pg3T3YV5W5tteJ0wGrAcO1S9voLZb.bWRjX2RvbWFpbi9tZGNvd2FwMS1tZGNhcHAxMQ==',
        'Host': 'data.krx.co.kr',
        'Origin': 'http://data.krx.co.kr',
        'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020301',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # date_0 = '202107011'
    strtDd= endDd = date_0
    # print(strtDd)
    # print(endDd)
    data = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT02401',
        'mktId': 'ALL',
        'invstTpCd': '6000',
        'strtDd': strtDd,
        'endDd': endDd,
        'share': '1',
        'money': '1',
        'csvxls_isNo': 'false'
    }
    temp = requests.post(url, data=data, headers = header)
    temp = json.loads(temp.content.decode('utf-8'))['output']
    if temp != []:
        dics = {}
        for i in temp:
            corp_cd = i['ISU_SRT_CD']
            corp_nm = i['ISU_NM']
            am_medo = i['ASK_TRDVOL']
            am_mesu = i['BID_TRDVOL']
            am_sunmesu = i['NETBID_TRDVOL']
            num_medo = i['ASK_TRDVAL']
            num_mesu = i['BID_TRDVAL']
            num_sunmesu = i['NETBID_TRDVAL']
            dics[corp_cd] = {}
            dics[corp_cd]['corp_cd'] = corp_cd
            dics[corp_cd]['corp_nm'] = corp_nm
            dics[corp_cd]['am_medo'] = am_medo.replace(',','')
            dics[corp_cd]['am_mesu'] = am_mesu.replace(',','')
            dics[corp_cd]['am_sunmesu'] = am_sunmesu.replace(',','')
            dics[corp_cd]['num_medo'] = num_medo.replace(',','')
            dics[corp_cd]['num_mesu'] = num_mesu.replace(',','')
            dics[corp_cd]['num_sunmesu'] = num_sunmesu.replace(',','')

        return dics


