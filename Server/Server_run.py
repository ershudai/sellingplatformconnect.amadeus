import threading
import time
from SingleTask import *
from fastapi import FastAPI
import uvicorn
from DataProcessing import *
from pydantic import BaseModel
import sys
import os
import uvicorn
from fastapi.responses import JSONResponse
app=FastAPI()
app_get=FastAPI()

Thr_list=[]

class People(BaseModel):
    name:str
    data:dict

@app.get('/test/a={a}/b={b}')
def app_run(a: int=None,b: int=None):
    c=a+b
    res={"res":c}
    return  res

@app.post('/api/add')
def api_add(people: People):
    try:
        if people.name not in AccountInformation:
            AccountInformation[people.name]=people.data
            #Post_Shakedown(people.name)
            thr_add=threading.Thread(name=people.name, target=Post_Shakedown,args=(people.name,))
            thr_add.start()
            #print("开启线程---"+people.name)
            Thr_list.append(thr_add)
            return {"return":True,"text":"线程正常添加，服务器开始运行！"}
        else:
            return {"return": False, "text": "已有相关参数！删除后再进行添加！"}
    except:
        return {"return": False, "text": "添加出错了！"}

@app.get('/api/get/{uid}')
def api_get_user(uid):
    try:
        try:
            return json.dumps(AccountInformation[uid]['data_bool'])
        except:
            return False
    except:
        return False

@app.get('/api/set/{uid}/key={key}')
def api_set_user(uid,key):
    try:
        AccountInformation[uid]['data_bool'][key]=True
        return True
    except:
        return False

@app.get('/api/delete/{uid}')
def api_delete_user(uid):
    try:
        if uid in AccountInformation:
            AccountInformation.pop(uid)
            return {"return":True,"text":"删除成功！"}
        return {"return":False,"text":"未能找到你的信息！"}
    except:
        return {"return":False,"text":"删除出错了！"}
if __name__=='__main__':
    duankou=0
    try:
        if len(sys.argv)>=1:
            arg1 = sys.argv[1]
            duankou=int(arg1)
    except:
    # arg2=sys.argv[2]
    # if arg2 != None:
    #     print(arg2)
        try:
            duankou=input("输入端口号（空白表示默认,建议8080~9999之间）：")
            if duankou=="" or int(duankou)==0:
                print('输入空或0默认8080端口！')
                duankou=8080
            else:
                duankou=int(duankou)
        except:
            print('检查输入是否正确！')

    # dir_log = "logs"
    # path_log = os.path.join(dir_log, '日志文件.log')
    # # 路径，每日分割时间，是否异步记录，日志是否序列化，编码格式，最长保存日志时间
    # logger.add(path_log, rotation='0:00', enqueue=True, serialize=False, encoding="utf-8", retention="10 days")
    # logger.debug("服务器重启！")

    kk=uvicorn.run(app=app,host="127.0.0.1",port=duankou,workers=1)

    print("设置端口为:"+str(duankou))
# T1={}
# T1_name="JZHAO2"
# T1['cookies']="prxCookie=!FW7FXq1ibu7ycCDPUK3QNIFO+llyZ38iuCThU5eLwaQZv6CD9xDO1mj5uHmzENnAn8OO6PTm/xUxzIrOWiyQckvMUT1SJ8RIZWt0eOw=;7b668bde72e14b25feba017b89192736=2aebdeee1f3ad4ba16bb3e679c87ce41;incap_ses_463_2643603=hZrrCcCyaw0wxb90eehsBhr6b2EAAAAADaUPyCbLKwcU6Pzktj2Nnw==;visid_incap_2643603=1wLflzyrRZilvduPMrG0Lxn6b2EAAAAAQUIPAAAAAADuGnXDCtyCyrcsJ/E1zjD1;JSID=false;021f86550161f006c3fbcc6be65c6eaa=1a9a8aeb0824bcd2ecfbfe73a5fe5067;lss_loc_id=99D04A9E2DF5DE6E6088A09A9692F97BFD9780292A71BA19B6A2D130A765F121;um_jst=4747AC1AA15CCDE0AFE35D79E05668774A9F6A301B5CABAC1A3C5362A7711347;"
# T1['data']=\
#     {
#         '1':{'jSessionId': '_F5xU2THIrC0cwNWHdHDUiizw9VL_wp1wVQ7GeeQ!1634728472714', 'contextId': '4747ac1aa15ceea7ffd3153eb107594707d95b034208e1e1436d0332f5554176', 'userId': 'JZHAO2', 'organization': 'NMC-US', 'officeId': 'IAHG32415', 'gds': 'AMADEUS', 'isStatelessCloneRequired': False, 'tasks': [{'type': 'CRY', 'command': {'command': '1', 'prohibitedList': 'SITE_JCPCRYPTIC_PROHIBITED_COMMANDS_LIST_2'}}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'pnr.PnrParser'}]},
#         '2':{'jSessionId': 'UjMJL1OuIABPpgmtXGNsExQC91JhA__276gmFNFZ!1634728481670', 'contextId': '4747ac1aa15cfcb7f6ad7923d710514719dc5b034208e1e1436d0332f5554176', 'userId': 'JZHAO2', 'organization': 'NMC-US', 'officeId': 'IAHG32415', 'gds': 'AMADEUS', 'isStatelessCloneRequired': False, 'tasks': [{'type': 'CRY', 'command': {'command': '2', 'prohibitedList': 'SITE_JCPCRYPTIC_PROHIBITED_COMMANDS_LIST_2'}}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'pnr.PnrParser'}]},
#         '3':{'jSessionId': '3ybSOs46iprxwUqggTkIBvdHFhnoJ-olp4Y3ONyW!1634728483978', 'contextId': '4747ac1aa15cfbd7ebaa134eb562223904af5a034208e1e1436d0332f5554176', 'userId': 'JZHAO2', 'organization': 'NMC-US', 'officeId': 'IAHG32415', 'gds': 'AMADEUS', 'isStatelessCloneRequired': False, 'tasks': [{'type': 'CRY', 'command': {'command': '3', 'prohibitedList': 'SITE_JCPCRYPTIC_PROHIBITED_COMMANDS_LIST_2'}}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'pnr.PnrParser'}]},
#         '4':{'jSessionId': 'o2VUt_0ktczJRQYTTpo04Lvbd7CTaX4s_m1R7kXc!1634728485676', 'contextId': '4747ac1aa15c9fb0fdb56937a56622211ddc5b034208e1e1436d0332f5554176', 'userId': 'JZHAO2', 'organization': 'NMC-US', 'officeId': 'IAHG32415', 'gds': 'AMADEUS', 'isStatelessCloneRequired': False, 'tasks': [{'type': 'CRY', 'command': {'command': '4', 'prohibitedList': 'SITE_JCPCRYPTIC_PROHIBITED_COMMANDS_LIST_2'}}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'screens.ScreenTypeParser'}, {'type': 'PAR', 'parserType': 'pnr.PnrParser'}]},
#     }
# T1['data_Instruct']=\
#     {
#         '1':"AD24FEBSVOPVG/ASU/CW,Y",
#         '2':"AD28octSVOPVG/ASU/CW,Y",
#         '3':"AD28octSVOPVG/ASU/CW,Y",
#         '4':"AD28octSVOPVG/ASU/CW,Y",
#     }
# AccountInformation[T1_name]=T1
#
#
# t1="第一个线程"
# t2="第二个线程"
# thr = threading.Thread(name=T1_name, target=Post_Shakedown,args=(T1_name,))
# #thr1 = threading.Thread(target=Post_Shakedown,args=())
# print(str(thr))
# thr.start()
# print(str(thr))
# #thr1.start()
# print(thr)


