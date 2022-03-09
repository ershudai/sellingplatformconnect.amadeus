from selenium import webdriver
from requests import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib.parse
import re
import threading
import time
import os
import configparser
import json
import getpass

#chromeOption启动函数
def chromedriver():
    driver_path=r'.\chromedriver.exe'
    chromeOptions = webdriver.ChromeOptions()
    try:
        a1=r"--user-data-dir=C:\Users\\"
        a2=getpass.getuser()
        a3=r'\AppData\Local\Google\Chrome\User Data'
        path=a1+a2+a3
        chromeOptions.add_argument(path)  # 设置成用户自己的数据目录
        chromeOptions.add_argument('disable-infobars')
        chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation']);
        chromeOptions.add_experimental_option('w3c', False)
    except:
        print("请关闭相关浏览器")
    caps = DesiredCapabilities.CHROME
    caps = {
        'loggingPrefs': {
            'performance': 'ALL',
        }
    }

    wd=webdriver.Chrome(executable_path=driver_path,chrome_options=chromeOptions,desired_capabilities=caps)
    return wd

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



def select_post_1(data,cookies):
    url="""https://www.booking4.sellingplatformconnect.amadeus.com/cryptic/apfplus/modules/cryptic/cryptic?&LANGUAGE=CN&SITE=AMERGSTD"""

    headers=\
    {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "967",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": cookies,
        "origin": "https://www.booking4.sellingplatformconnect.amadeus.com",
        "referer": "https://www.booking4.sellingplatformconnect.amadeus.com/app_sell2.0/apf/init/login?SITE=LOGINURL&LANGUAGE=CN&refreshOnError=true",
        "sec-ch-ua": r'''Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"''',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    res=post(url=url,data=data,headers=headers)
    rt = json.loads(res.text)
    try:
        rt=rt['model']['output']['crypticResponse']['response']
    except:
        return False,""
    return True,rt


#分析票数量，定义返回提交所需参数
def get_post_result(rt):

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
        if int(vt[1])>0:
            votes_pd=True
            votes_dcit[vt[0:1]]=int(vt[1])
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
    print(piao_votes,votes_dcit[piao_votes])
    if votes_dcit[piao_votes]>5:
        post2_dt = "SS" + str(5) + piao_votes + "1"
    else:
        post2_dt = "SS" + str(votes_dcit[piao_votes]) + piao_votes + "1"
    return True,post2_dt

def get_data(log):
    requests = []
    url=[]
    url1="""https://www.booking4.sellingplatformconnect.amadeus.com/cryptic/apfplus/modules/cryptic/cryptic?&LANGUAGE=CN&SITE=AMERGSTD"""
    url2="""https://www.booking3.sellingplatformconnect.amadeus.com/cryptic/apfplus/modules/cryptic/cryptic?&LANGUAGE=CN&SITE=SELWAABP"""
    for log in log:
        x = json.loads(log['message'])['message']
        if x["method"] == "Network.requestWillBeSent":
            if url1 in x["params"]["request"]["url"]:
                requests.append(x["params"])
            if url2 in x["params"]["request"]["url"]:
                requests.append(x["params"])
        else:
            pass

    return requests
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

def set_instruct(dcit,instruct):
    dcit['tasks'][0]['command']['command']=instruct
    data="data="+urllib.parse.quote(str(json.dumps(dcit)))
    return data

import win32con
import win32api
import time

def key_down(key):
    """
    函数功能：按下按键
    参    数：key:按键值
    """
    #key = key.upper()
    #vk_code = key_map[key]
    vk_code = key
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), 0, 0)


def key_up(key):
    """
    函数功能：抬起按键
    参    数：key:按键值
    """
    #key = key.upper()
    #vk_code = key_map[key]
    vk_code = key
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)


def key_press():
    """
    函数功能：模拟器按键ctrl+pgdn ctrl+pgup
    参    数：无
    """
    ctrl=17
    pgup=33
    pgdn=34
    key_down(ctrl)
    time.sleep(0.2)

    key_down(pgdn)
    time.sleep(0.05)
    key_up(pgdn)

    time.sleep(0.5)

    key_down(pgup)
    time.sleep(0.05)
    key_up(pgup)

    time.sleep(0.1)
    key_up(ctrl)

