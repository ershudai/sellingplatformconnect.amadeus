#网络交互模块

from requests import *
import json

#post——获取指令反回参数
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
