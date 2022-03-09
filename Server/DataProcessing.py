#数据处理模块

import urllib.parse
import json

def get_login_cookies(wd):
    ck=wd.get_cookies()
    ck=get_ck(ck)
    return ck

#将cookies转为字典类型
def get_ck(ck):
    cook={}
    for oneCK in ck:
        cook[oneCK['name']]=oneCK['value']
    return cook
#将cookies转换为str类型
def get_cookies(dcit):
    cookies=''
    for key,value in dcit.items():
        cookies+=key+r"="+value+";"
    return cookies

#分析票数量，定义返回提交所需参数
def get_post_result(rt):
    try:
        ret=""
        rt_list=rt.split("\n")
        piao=str(rt_list[2]).split(r"  ")
        p_id=piao[0]
        p_type=piao[1]
        p_votes=piao[2]
        votes=p_votes.split(r' ')
        votes_pd=False
        votes_dcit={}
        for vt in votes:
            try:
                if int(vt[1])>0:
                    votes_pd=True
                    votes_dcit[vt[0:1]]=int(vt[1])
            except:
                pass
        if votes_pd==False:
            return False,p_id+p_type+p_votes
        print(rt_list)
        #定义优先级
        piao_votes=""
        if 'Y' in votes_dcit.keys():
            piao_votes='Y'
        if 'W' in votes_dcit.keys():
            piao_votes='W'
        if 'J' in votes_dcit.keys():
            piao_votes='J'
        if piao_votes=="":
            for key in votes_dcit:
                piao_votes=key
                break
        #print(piao_votes,votes_dcit[piao_votes])
        if votes_dcit[piao_votes]>5:
            post2_dt = "SS" + str(5) + piao_votes + "1"
        else:
            post2_dt = "SS" + str(votes_dcit[piao_votes]) + piao_votes + "1"
        return True,post2_dt
    except:
        return False,"未能识别到票"

def get_data(log):
    requests = []
    for log in log:
        x = json.loads(log['message'])['message']
        if x["method"] == "Network.requestWillBeSent":
            if x["params"]["request"]["url"]=="""https://www.booking4.sellingplatformconnect.amadeus.com/cryptic/apfplus/modules/cryptic/cryptic?&LANGUAGE=CN&SITE=AMERGSTD""":
                requests.append(x["params"])
        else:
            pass
    # if 'params' in message and 'documentURL' in message['params']:
    #     if message['params']['documentURL']=="https://www.booking4.sellingplatformconnect.amadeus.com/cryptic/apfplus/modules/cryptic/cryptic?&LANGUAGE=CN&SITE=AMERGSTD":
    #         lists.append(message)
    return requests

#返回data参数解析
def get_data_decode(lists):
    dcits={}
    for ls in lists:
        data_str=ls['request']['postData']
        list = str(data_str).split("=")
        data_str = urllib.parse.unquote(list[1])
        data_json=json.loads(data_str)
        dcits[data_json['tasks'][0]['command']['command']]=data_json
        print(str(json.dumps(data_json)))
    return dcits

#提交data中插入指令
def set_instruct(dcit,instruct):
    dcit['tasks'][0]['command']['command']=instruct
    data="data="+urllib.parse.quote(str(json.dumps(dcit)))
    return data

# def update_data(list1,list2):
#     lists=[]
#     lists1=list1
#     for lt2 in list2:
#         id=lt2['tasks'][0]['command']['command']
#         lt2_add=True
#         for lt1 in range(0,len(list1)):
#             if list1[lt1]['tasks'][0]['command']['command']==id:
#                 lt2_add=False
#
#                 break
#         if lt2_add==True:
#             list1.app
'  1  SU 208 W 24FEB 4 SVOPVG HK4        C   755P 950A+1 77W E0 D'
def get_post_win(rt):
    try:
        ret=""
        rt_list=rt.split("\n")
        piao=str(rt_list[1]).split(r"  ")
        p_id=piao[0]
        p_type=piao[1]
        p_votes=piao[2]
        votes=p_votes.split(r' ')
        votes_pd=''
        votes_dcit={}
        for vt in votes:
            if len(vt)>=2:
                if vt[0:2]=="HK":
                    votes_pd=True
                    break
                if vt[0:2] == "DK":
                    votes_pd = True
                    break
                if vt[0:2]=="UC" or vt[0:2]=="KL":
                    votes_pd=False
                    break
        return votes_pd



    except:
        print("判断订票信息错误！---get_post_win")

def pd_ss(rt):
    try:
        if 'SS' in rt:
            return True
        return False
    except:
        print("判断订票信息错误！---get_post_win")


def SS_get_post_result(rt):
    try:
        ret = ""
        rt_list = rt.split("\n")
        piao = str(rt_list[1]).split(r"  ")
        p_id = piao[0]
        p_type = piao[1]
        p_votes = piao[2]
        votes = p_votes.split(r' ')
        votes_pd = ''
        votes_dcit = {}
        for vt in votes:
            if len(vt) >= 2:
                if vt[0:2] == "HK":
                    votes_pd = True
                    break
                if vt[0:2] == "DK":
                    votes_pd = True
                    break
                if vt[0:2] == "UC" or vt[0:2] == "KL" or vt[0:2] == "KL" or vt[0:2] == "KL" or vt[0:2] == "KL" :
                    votes_pd = False
                    break
        return votes_pd
    except:
        return False
        print("判断订票信息错误！---get_post_win")



id="  SU 208 Y 11NOV 4 SVOPVG NOT AVAILABLE AND WAITLIST CLOSED\nAD11NOVSVOPVG1955\n** GTT AVAILABILITY - AD ** PVG PUDONG INTL.CN                15 TH 11NOV  755P\n 1   SU 208  J0 C0 D0 I0 Z0 W0 S0  SVO C PVG 2  755P    950A+1E0/77W       8:55\n             A0 Y0 B0 M0 U0 K0 H0 L0 Q0 T0 E0 N0 R0 G0 V0\n 2   SU 272  J2 C2 D2 I2 Z4 W4 S4  SVO C BKK    945P   1040A+1E0/77W\n             A2 Y4 B4 M4 U4 K4 H4 L4 Q4 T4 E4 N4 R4 G0 V0\n  TG:WE5638  Y9 B9 M9 H9 Q9 T9 K9 /BKK   HKG 1  200P+1  545P+1E0/359\n             S9 V9 W9\n     MU 508  F0 U0 J9 C6 D3 Q0 I0 /HKG 1 PVG 2  325P+2  550P+2E0.321      39:05\n             W0 P0 Y9 B9 M9 E9 H9 K9 L9 N9 R9 S9 V9 T9 G0\n 3   SU 272  J2 C2 D2 I2 Z4 W4 S4  SVO C BKK    945P   1040A+1E0/77W\n             A2 Y4 B4 M4 U4 K4 H4 L4 Q4 T4 E4 N4 R4 G0 V0\n     EK 384  F4 A4 J7 C7 I7 O7 H7 /BKK   HKG 1  145P+1  540P+1E0/77W\n             Y9 E9 R9 W9 M9 B9 U9 K9 Q9 L9 T9 V9 X9\n     MU 508  F0 U0 J9 C6 D3 Q0 I0 /HKG 1 PVG 2  325P+2  550P+2E0.321      39:05\n             W0 P0 Y9 B9 M9 E9 H9 K9 L9 N9 R9 S9 V9 T9 G0\n>"
SS_get_post_result(id)
#pd_ss(id)