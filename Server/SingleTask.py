#引入数据处理模块和网络交互模块
from DataProcessing import *
from NetWork import *
import time
import threading
from smtp import *

pool=ThreadPoolExecutor(max_workers=1)
#fut1=pool.submit(main_mail,"1你好呀", "1并发线程---送1封，上面的列表是几个人，这个就填几")
AccountInformation={}

def req_post(dt,value,T1_name,cook):
    stop_true = 0
    while True:
        try:
            global AccountInformation
            while True:
                if T1_name not in AccountInformation.keys():
                    stop_true=1
                    break
                try:
                    t = int(round(time.time() * 1000))
                    if AccountInformation[T1_name]['data_bool'][dt]:
                        try:
                            id = value['tasks'][0]['command']['command']
                        except:
                            print("取出命令框编号失败")
                            pass
                        order=AccountInformation[T1_name]['data_Instruct'][dt]
                        if "SS" in order:

                            data = set_instruct(value, order)
                            bool_rt, return_text = select_post_1(data, cook)
                            if bool_rt == True:
                                #检查是否有订票成功
                                bools=SS_get_post_result(return_text)
                                if bools:
                                    print(str(T1_name) + "---" + str(dt) + "------SS订票成功")
                                    AccountInformation[T1_name]['data_bool'][dt] = False
                                    fut1 = pool.submit(main_mail,return_text,str(T1_name)+"---"+str(dt))
                                else:
                                    data = set_instruct(value, "IG")
                                    bool_rt, return_text = select_post_1(data, cook)
                            pass
                        else:
                            data = set_instruct(value, order)
                            bool_rt, return_text = select_post_1(data, cook)
                            if bool_rt == True:
                                # 查票
                                re_bool, post_command = get_post_result(return_text)
                                # print(id+"---"+post_command)
                                if re_bool == True:
                                    # 抢票节点
                                    data = set_instruct(value, post_command)
                                    text_bool, get_text = select_post_1(data, cook)
                                    if text_bool:
                                        if get_post_win(get_text):
                                            # if send_mail(mailto_list, "你好呀，测试", get_text):
                                            #     print(str(T1_name) + "---" + str(dt) + "------已经发送邮件！")
                                            print(str(T1_name) + "---" + str(dt) + "------SD订票成功")
                                            AccountInformation[T1_name]['data_bool'][dt] = False
                                            fut2 = pool.submit(main_mail,return_text,str(T1_name)+"---"+str(dt))
                                        else:
                                            data = set_instruct(value, "IG")
                                            bool_rt, return_text = select_post_1(data, cook)
                                else:
                                    pass
                                    # print(str(dt) + "---无票可用!--" + post_command)
                            else:
                                pass
                    time_int = int(round(time.time() * 1000)) - t

                    order = AccountInformation[T1_name]['data_Instruct'][dt]
                    time_stop=0
                    if time_int<=500:
                        time_stop=0.001*(500-time_int)
                    else:
                        time_stop=0

                    if AccountInformation[T1_name]['data_bool'][dt] != False:
                        if "SS" in order:
                            print(str(T1_name) + "---" + str(dt) + "---SS一次订票结束---" + str(time_int) + "毫秒---延时：" + str(time_stop) + "秒")
                        else:
                            print(str(T1_name) + "---" + str(dt) + "---SD一次查票结束---" + str(time_int) + "毫秒---延时：" + str(time_stop) + "秒")
                                    # print(str(dt) + "---查票失败!")
                    time.sleep(time_stop)
                except:
                    print(str(T1_name) + "---" + str(dt) + "------已经关闭" )
                    break
        except:
            print(str(T1_name) + "---" + str(dt) + "------意外结束运行，正在重新开启！")
        if stop_true == 1:
            print(str(T1_name) + "---" + str(dt) + "------数据以删除，结束运行")
            break



def Post_Shakedown(T1_name):
    global AccountInformation
    cook=AccountInformation[T1_name]['cookies']
    AccountInformation[T1_name]['data_bool']={}
    for dt, value in AccountInformation[T1_name]['data'].items():
        AccountInformation[T1_name]['data_bool'][dt]=True
    threads=[]
    for dt, value in AccountInformation[T1_name]['data'].items():
        thr=threading.Thread(target=req_post,args=(dt,value,T1_name,cook))
        thr.start()
        threads.append(thr)
    for thread in threads:
        thread.join()
    #print(str(T1_name) + "------所有线程创建完毕！")

def set(Acc_key,Acc_value,Thr_key,Thr_value):
    global AccountInformation
    global Threading_control
    AccountInformation[Acc_key]=Acc_value
    Threading_control[Thr_key]=Thr_value
    print("111")



