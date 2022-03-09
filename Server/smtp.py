#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
import threading
#def set_mail():
import time
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor

sender='root@smtpbooking.xyz'
mail_host="smtpdm.aliyun.com"             #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="root@smtpbooking.xyz"              #用户名
mail_pass="ROot123456"         #密码
mail_postfix="smtpbooking.xyz"               #邮箱的后缀，网易就是163.com

#mailto_list=['aikeke00003@163.com','5404225@qq.com']  #收件人(列表)

def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['From'] = sender
    msg['To'] = "115671525@QQ.COM"         #将收件人列表以‘；’分隔
    send_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msg['Subject'] = '测试邮件'+send_time
    try:
        server = smtplib.SMTP()
        server.connect(mail_host,25)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(sender, to_list, msg.as_string())
        server.close()
        print("发送成功！")
    except Exception as e:
        print(str(e))
        print("发送失败！")
                            #发送1封，上面的列表是几个人，这个就填几
# if send_mail(mailto_list,"你好呀，测试","这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信"):  #邮件主题和邮件内容
#     #这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
#     print ("done!")
# else:
#     print ("failed!")

def main_mail(text,head,):
    sed='root@smtpbooking.xyz'
    key="ROot123456"
    receivers=['fly593150222@163.com','aikeke1995@163.com']
    message=MIMEText(text,'plain','utf-8')
    message['From'] = sed
    #message['To'] = "115671525@QQ.COM"
    message['Subject']=Header(head,'utf-8')
    smtper=SMTP()
    smtper.connect("smtpdm.aliyun.com", 25)
    #smtper.ehlo()
    #smtper.starttls()
    smtper.login('root@smtpbooking.xyz',key)
    smtper.sendmail(sed,receivers,message.as_string())
    time.sleep(1)
    #print(str(time.time()))
    #print('发送完成')

#
# threads=[]
# for i in range(20):
#     main_mail(str(i)+"你好呀", str(i)+"并发线程"+str(i)+"---送1封，上面的列表是几个人，这个就填几")
# pool=ThreadPoolExecutor(max_workers=1)
# fut1=pool.submit(main_mail,"1测试", "1并发线程---送1封，上面的列表是几个人，这个就填几")
# fut2=pool.submit(main_mail,"2测试", "2并发线程---送1封，上面的列表是几个人，这个就填几")
# fut1=pool.submit(main_mail,"3测试", "3并发线程---送1封，上面的列表是几个人，这个就填几")
# fut2=pool.submit(main_mail,"4测试", "4并发线程---送1封，上面的列表是几个人，这个就填几")
# fut1=pool.submit(main_mail,"5测试", "5并发线程---送1封，上面的列表是几个人，这个就填几")
# fut2=pool.submit(main_mail,"6测试", "6并发线程---送1封，上面的列表是几个人，这个就填几")

#
# print("线程执行完毕")
