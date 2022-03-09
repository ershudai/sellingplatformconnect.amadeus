from select_post import *
from selenium import webdriver
import browsermobproxy
import threading
import json
global instruct
global driver
global cook
global data_list
global judge
from playsound import playsound
from pygame import mixer
from selenium.webdriver.common.keys import Keys

server_ip="47.254.121.4:8080"
driver=""
cook=""
data_list=[]
judge=True
dt={}
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    #from Tkinter import *
    #from tkFont import Font
    #from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    #from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()
def mix():
    mixer.init()
    mixer.music.load('14430.mp3')
    mixer.music.play()
    time.sleep(18)
    mixer.music.stop()

#监听是否已经定到票
def get_Instruct(self):
    global dt
    global server_ip
    mp3 = False
    global judge
    while judge:
        try:
            kk = get("http://"+server_ip+"/api/get/" + dt['name'])
            kk = json.loads(kk.text)
            kk = json.loads(kk)
            i=0
            for k, v in kk.items():
                if v is False:
                    if mp3 is False:
                        cmd = threading.Thread(target=mix, args=())
                        cmd.run()
                        mp3=True
                    break
                i+=1
            for k, v in kk.items():
                if self.Label1['text']==k:
                    if v is False:
                        self.Label1.configure(foreground="red")
                    elif v is True :
                        self.Label1.configure(foreground="green")

                if self.Label2['text']==k:
                    if v is False:
                        self.Label2.configure(foreground="red")
                    elif v is True:
                        self.Label2.configure(foreground="green")

                if self.Label3['text']==k:
                    if v is False:
                        self.Label3.configure(foreground="red")
                    elif v is True:
                        self.Label3.configure(foreground="green")

                if self.Label4['text']==k:
                    if v is False:
                        self.Label4.configure(foreground="red")
                    elif v is True:
                        self.Label4.configure(foreground="green")

                if self.Label5['text']==k:
                    if v is False:
                        self.Label5.configure(foreground="red")
                    elif v is True:
                        self.Label5.configure(foreground="green")

                if self.Label6['text']==k:
                    if v is False:
                        self.Label6.configure(foreground="red")
                    elif v is True:
                        self.Label6.configure(foreground="green")

            if i>=len(kk):
                mp3=False
        except:
            self.Label1.configure(foreground="black")
            self.Label2.configure(foreground="black")
            self.Label3.configure(foreground="black")
            self.Label4.configure(foreground="black")
            self.Label5.configure(foreground="black")
            self.Label6.configure(foreground="black")
            print("查询失败，服务器未能查到相关数据！")

end_bool=False
def end(web):
    try:
        global end_bool
        while end_bool:
            key_press()
            #kk.send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
            time.sleep(30)
    except:
        print("防止网页静止切换！出现了问题")
        


class Application_ui(Frame):
    #Õâ¸öÀà½öÊµÏÖ½çÃæÉú³É¹¦ÄÜ£¬¾ßÌåÊÂ¼þ´¦Àí´úÂëÔÚ×ÓÀàApplicationÖÐ¡£
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('旗舰版')
        self.master.geometry('520x520')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Label_ip.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label_ip = Label(self.top, text='ip:', style='Label_ip.TLabel')
        self.Label_ip.place(relx=0.559, rely=0.35, relwidth=0.084, relheight=0.051)

        self.Text_ipVar = StringVar(value='')
        self.Text_ip = Entry(self.top, text='', textvariable=self.Text_ipVar, font=('ËÎÌå',9))
        self.Text_ip.place(relx=0.641, rely=0.35, relwidth=0.298, relheight=0.051)


        self.style.configure('Command1.TButton',font=('ËÎÌå',9))
        self.Command1 = Button(self.top, text='打开浏览器', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.100, rely=0.05, relwidth=0.280, relheight=0.100)
        self.style.configure('Command2.TButton',font=('ËÎÌå',9))
        self.Command2 = Button(self.top, text='开启检测参数', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.100, rely=0.15, relwidth=0.280, relheight=0.100)
        self.style.configure('Command3.TButton',font=('ËÎÌå',9))
        self.Command3 = Button(self.top, text='清空检测内容', command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0.100, rely=0.25, relwidth=0.280, relheight=0.100)
        self.style.configure('Command4.TButton',font=('ËÎÌå',9))
        self.Command_ck = Button(self.top, text='开启模拟按键', command=self.Command_ck, style='Command_ck.TButton')
        self.Command_ck.place(relx=0.100, rely=0.35, relwidth=0.280, relheight=0.100)
        self.style.configure('Command4.TButton',font=('ËÎÌå',9))
        self.Command4 = Button(self.top, text='记录指令', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.581, rely=0.88, relwidth=0.199, relheight=0.105)

        self.style.configure('Label_text.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label_text = Label(self.top, text='Label1', style='Label_text.TLabel')
        self.Label_text.place(relx=0.520, rely=0.02, relwidth=0.462, relheight=0.184)


        self.style.configure('Command_post.TButton',font=('ËÎÌå',9))
        self.Command_post = Button(self.top, text='提交开始监控', command=self.Command_post, style='Command_post.TButton')
        self.Command_post.place(relx=0.789, rely=0.88, relwidth=0.199, relheight=0.105)

        self.style.configure('Label1.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label1 = Label(self.top, text='Label1', style='Label1.TLabel')
        self.Label1.place(relx=0.115, rely=0.500, relwidth=0.084, relheight=0.05)

        self.Text1Var = StringVar(value='')
        self.Text1 = Text(self.top,highlightcolor='red',font=('ËÎÌå',9))
        self.Text1.place(relx=0.200, rely=0.514, relwidth=0.739, relheight=0.25)

        #self.Text1.grid(row=0,column=0)


        self.style.configure('Label2.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label2 = Label(self.top, text='Label1', style='Label2.TLabel')
        self.Label2.place(relx=0.115, rely=0.540, relwidth=0.084, relheight=0.05)

        # self.Text2Var = StringVar(value='')
        # self.Text2 = Entry(self.top, text='', textvariable=self.Text2Var, font=('ËÎÌå',9))
        # self.Text2.place(relx=0.641, rely=0.514, relwidth=0.298, relheight=0.051)

        self.style.configure('Label3.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label3 = Label(self.top, text='Label1', style='Label3.TLabel')
        self.Label3.place(relx=0.115, rely=0.580, relwidth=0.084, relheight=0.05)

        # self.Text3Var = StringVar(value='')
        # self.Text3 = Entry(self.top, text='', textvariable=self.Text3Var, font=('ËÎÌå',9))
        # self.Text3.place(relx=0.197, rely=0.596, relwidth=0.298, relheight=0.051)

        self.style.configure('Label4.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label4 = Label(self.top, text='Label1', style='Label4.TLabel')
        self.Label4.place(relx=0.115, rely=0.620, relwidth=0.084, relheight=0.05)

        # self.Text4Var = StringVar(value='')
        # self.Text4 = Entry(self.top, text='', textvariable=self.Text4Var, font=('ËÎÌå',9))
        # self.Text4.place(relx=0.641, rely=0.596, relwidth=0.298, relheight=0.051)

        self.style.configure('Label5.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label5 = Label(self.top, text='Label1', style='Label5.TLabel')
        self.Label5.place(relx=0.115, rely=0.660, relwidth=0.084, relheight=0.05)
        #
        # self.Text5Var = StringVar(value='')
        # self.Text5 = Entry(self.top, text='', textvariable=self.Text5Var, font=('ËÎÌå',9))
        # self.Text5.place(relx=0.197, rely=0.677, relwidth=0.298, relheight=0.051)

        self.style.configure('Label6.TLabel',anchor='w', font=('ËÎÌå',9))
        self.Label6 = Label(self.top, text='Label1', style='Label6.TLabel')
        self.Label6.place(relx=0.115, rely=0.700, relwidth=0.084, relheight=0.05)

        # self.Text6Var = StringVar(value='')
        # self.Text6 = Entry(self.top, text='', textvariable=self.Text6Var, font=('ËÎÌå',9))
        # self.Text6.place(relx=0.641, rely=0.677, relwidth=0.298, relheight=0.051)


        self.style.configure('delete.TButton',font=('宋体',9))
        self.delete = Button(self.top, text='删除服务器数据', command=self.delete_Cmd, style='delete.TButton')
        self.delete.place(relx=0.032, rely=0.878, relwidth=0.150, relheight=0.084)

        # self.style.configure('bt.TButton',font=('宋体',9))
        # self.bt = Button(self.top, text='删除服务器数据', command=self.bt_Cmd, style='bt.TButton')
        # self.bt.place(relx=0.032, rely=0.780, relwidth=0.080, relheight=0.054)


        self.style.configure('Command1_l.TButton',font=('宋体',9))
        self.Command1_l = Button(self.top, text='Command1', command=self.Command1_l, style='Command1_l.TButton')
        self.Command1_l.place(relx=0.259, rely=0.816, relwidth=0.051, relheight=0.064)

        self.style.configure('Command2_l.TButton',font=('宋体',9))
        self.Command2_l = Button(self.top, text='Command1', command=self.Command2_l, style='Command2_l.TButton')
        self.Command2_l.place(relx=0.339, rely=0.816, relwidth=0.051, relheight=0.064)

        self.style.configure('Command3_l.TButton',font=('宋体',9))
        self.Command3_l = Button(self.top, text='Command1', command=self.Command3_l, style='Command3_l.TButton')
        self.Command3_l.place(relx=0.42, rely=0.816, relwidth=0.051, relheight=0.064)

        self.style.configure('Command4_l.TButton',font=('宋体',9))
        self.Command4_l = Button(self.top, text='Command1', command=self.Command4_l, style='Command4_l.TButton')
        self.Command4_l.place(relx=0.259, rely=0.898, relwidth=0.051, relheight=0.064)

        self.style.configure('Command5_l.TButton',font=('宋体',9))
        self.Command5_l = Button(self.top, text='Command1', command=self.Command5_l, style='Command5_l.TButton')
        self.Command5_l.place(relx=0.339, rely=0.898, relwidth=0.051, relheight=0.064)

        self.style.configure('Command6_l.TButton',font=('宋体',9))
        self.Command6_l = Button(self.top, text='Command1', command=self.Command6_l, style='Command6_l.TButton')
        self.Command6_l.place(relx=0.42, rely=0.898, relwidth=0.051, relheight=0.064)


class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    # def bt_Cmd(self, event=None):
    #     kk=self.Text1.get('0.0','end')
    #     text_list=kk.split('\n')
    #     print(kk)
    def Command1_l(self, event=None):
        try:
            kk = get("http://"+server_ip+"/api/set/{}/key={}".format(dt['name'],self.Command1_l['text']))
            if kk.text=='true':
                showinfo('提示', '修改成功，等待刷新即可')
        except:
            print("检查前面步骤是否出错！")

        pass
    def Command2_l(self, event=None):
        try:
            kk = get("http://"+server_ip+"/api/set/{}/key={}".format(dt['name'],self.Command2_l['text']))
            if kk.text=='true':
                showinfo('提示', '修改成功，等待刷新即可')
        except:
            print("检查前面步骤是否出错！")

    def Command3_l(self, event=None):
        try:
            kk = get("http://"+server_ip+"/api/set/{}/key={}".format(dt['name'], self.Command3_l['text']))
            if kk.text == 'true':
                showinfo('提示', '修改成功，等待刷新即可')
        except:
            print("检查前面步骤是否出错！")
    def Command4_l(self, event=None):
        try:
            kk = get("http://"+server_ip+"/api/set/{}/key={}".format(dt['name'], self.Command4_l['text']))
            if kk.text == 'true':
                showinfo('提示', '修改成功，等待刷新即可')
        except:
            print("检查前面步骤是否出错！")
    def Command5_l(self, event=None):
        try:
            kk = get("http://"+server_ip+"/api/set/{}/key={}".format(dt['name'], self.Command5_l['text']))
            if kk.text == 'true':
                showinfo('提示', '修改成功，等待刷新即可')
        except:
            print("检查前面步骤是否出错！")
    def Command6_l(self, event=None):
        try:
            kk = get("http://"+server_ip+"/api/set/{}/key={}".format(dt['name'], self.Command6_l['text']))
            if kk.text == 'true':
                showinfo('提示', '修改成功，等待刷新即可')
        except:
            print("检查前面步骤是否出错！")


    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        #web=chromedriver()
        #print(web.find_element_by_xpath("//*").get_attribute("outerHTML"))
        #print(web.page_source)
        #lists = soup.select("#mini-4$nodes2$-1")
        open_dir()
    def delete_Cmd(self,event=None):
        global judge
        try:
            judge = False
            kk = get(url="http://"+server_ip+"/api/delete/{}".format(dt['name']))
            kk = json.loads(kk.text)
            if kk['return']:
                showinfo('提示', '删除成功!')
            else:
                showinfo('提示', '删除失败!')
        except:
            print("检查前面步骤是否出错！联系管理员--delete_Cmd")
        pass
    def Command_post(self, event=None):
        #TODO, Please finish the function here!
        #web=chromedriver()
        #print(web.find_element_by_xpath("//*").get_attribute("outerHTML"))
        #print(web.page_source)
        #lists = soup.select("#mini-4$nodes2$-1")
        global server_ip
        global judge
        try:
            if 'data_Instruct' in dt['data']:
                try:
                    if self.Text_ip.get()!="":
                        server_ip=self.Text_ip.get()
                    dtt = json.dumps(dt)
                    kk =post(url="http://"+server_ip+"/api/add", data=dtt)
                    kk=json.loads(kk.text)
                    if kk['return']:
                        judge=True
                        thr=threading.Thread(target=get_Instruct,args=(self,))
                        thr.start()
                        showinfo('提示', "提交成功，已经开启监控窗口！")
                    else:
                        showinfo('提示', kk['text'])
                except:
                    showinfo('提示', '提交数据出现问题')
            else:
                showinfo('提示', '请先写入指令程序')
        except:
            print("提交包出现问题")



    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        #req=driver.requests
        global cook
        global data_list
        try:
            log=driver.get_log('performance')
        #print(req)
            T1={}
            #获取log中想要的数据
            lists=get_data(log)
            post_url=lists[0]['documentURL']
            dcit=get_data_decode(lists)
            print("取到"+str(len(dcit))+"个指令页面!")
            name=""
            for key,value in dcit.items():
                try:
                    name=value['userId']
                    break
                except:
                    print("查找userId失败！")
            cookeis = get_cookies(get_login_cookies(driver))
            T1['T1_name'] = name
            T1['cookies'] = cookeis
            T1['data'] = dcit
            T1['post_url']=post_url
            dt['name']=name
            dt['data']=T1
            self.Label_text['text'] = ("账号：{}\ncookies：{}\n指令窗口数量{}".format(name,str(cookeis!="") ,len(dcit)))
            len_i=len(dcit)
            index=0
            for i,value in dcit.items():
                if index==0:
                    self.Label1['text']=str(i)
                    self.Command1_l['text']=str(i)
                if index==1:
                    self.Label2['text']=str(i)
                    self.Command2_l['text'] = str(i)
                if index==2:
                    self.Label3['text']=str(i)
                    self.Command3_l['text'] = str(i)
                if index==3:
                    self.Label4['text']=str(i)
                    self.Command4_l['text'] = str(i)
                if index==4:
                    self.Label5['text']=str(i)
                    self.Command5_l['text'] = str(i)
                if index==5:
                    self.Label6['text']=str(i)
                    self.Command6_l['text'] = str(i)
                index+=1

            if 1<=len_i:
                self.Label1['state'] = NORMAL
                self.Text1['state']=NORMAL
                self.Command1_l['state'] = NORMAL
            else:
                self.Label1['state'] = DISABLED
                self.Text1['state']=DISABLED
                self.Command1_l['state'] = DISABLED

            if 2 <= len_i:
                self.Label2['state'] = NORMAL
                #self.Text2['state'] = NORMAL
                self.Command2_l['state'] = NORMAL
            else:
                self.Label2['state'] = DISABLED
                #self.Text2['state'] = DISABLED
                self.Command2_l['state'] = DISABLED

            if 3 <= len_i:
                self.Label3['state'] = NORMAL
                #self.Text3['state'] = NORMAL
                self.Command3_l['state'] = NORMAL
            else:
                self.Label3['state'] = DISABLED
                #self.Text3['state'] = DISABLED
                self.Command3_l['state'] = DISABLED

            if 4 <= len_i:
                self.Label4['state'] = NORMAL
                #self.Text4['state'] = NORMAL
                self.Command4_l['state'] = NORMAL
            else:
                self.Label4['state'] = DISABLED
                #self.Text4['state'] = DISABLED
                self.Command4_l['state'] = DISABLED

            if 5 <= len_i:
                self.Label5['state'] = NORMAL
                #self.Text5['state'] = NORMAL
                self.Command5_l['state'] = NORMAL
            else:
                self.Label5['state'] = DISABLED
                #self.Text5['state'] = DISABLED
                self.Command5_l['state'] = DISABLED

            if 6 <= len_i:
                self.Label6['state'] = NORMAL
                #self.Text6['state'] = NORMAL
                self.Command6_l['state'] = NORMAL
            else:
                self.Label6['state'] = DISABLED
                #self.Text6['state'] = DISABLED
                self.Command6_l['state'] = DISABLED
            print(cookeis)

            try:
                # 获取cookie并通过json模块将dict转化成str
                dictCookies = driver.get_cookies()
                jsonCookies = json.dumps(dictCookies)
                # 登录完成后，将cookie保存到本地文件
                with open('cookies.json', 'w') as f:
                    f.write(jsonCookies)
            except:
                print("读取写出cookies失败！")
        except:
            print("获取数据包失败，请检查浏览器是否正常打开！")

    def Command3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        #req=driver.requests
        try:
            driver.get_log('performance')
            showinfo('提示', '清除成功！')
            #self.update_idletasks()
        except:
            print("获取数据包失败，请检查浏览器是否正常打开！")

    def Command4_Cmd(self, event=None):
        #TODO, Please finish the function here!
        #req=driver.requests
        try:
            kk = self.Text1.get('0.0', 'end')
            text_list = kk.split('\n')
            in_dt={}
            if self.Label1['text']!='Label1':
                in_dt[self.Label1['text']]=text_list[0]
            if self.Label2['text'] != 'Label1':
                in_dt[self.Label2['text']]=text_list[1]
            if self.Label3['text'] != 'Label1':
                in_dt[self.Label3['text']]=text_list[2]
            if self.Label4['text'] != 'Label1':
                in_dt[self.Label4['text']]=text_list[3]
            if self.Label5['text'] != 'Label1':
                in_dt[self.Label5['text']]=text_list[4]
            if self.Label6['text'] != 'Label1':
                in_dt[self.Label6['text']]=text_list[5]
            if len(in_dt)<1:
                showinfo('提示', '未能取到任何指令')
            try:
                dt['data']['data_Instruct']=in_dt
                showinfo('提示', '修改成功')
            except:
                showinfo('提示', '请检查你的参数是否读取')
            # self.Label1['state'] = NORMAL
            # self.Text1['state'] = NORMAL

            #cookeis=get_login_cookies(driver)
            # print(cookeis)
            #dcit=get_data_decode(data_list)
        except:
            print("获取数据包失败，请检查浏览器是否正常打开！")
    def Command_ck(self, event=None):
        #TODO, Please finish the function here!
        #req=driver.requests
        global end_bool
        try:
            if end_bool is False:
                end_bool=True
                thr = threading.Thread(target=end, args=(driver,))
                thr.start()
                self.Command_ck['text']="正在运行"
            else:
                end_bool = False
                self.Command_ck['text'] = "开启模拟按键"

            #driver.delete_all_cookies()
            # with open('cookies.json', 'r', encoding='utf-8') as f:
            #     listCookies = json.loads(f.read())
            # for cookie in listCookies:
            #     dicts = {
            #         'domain': cookie['domain'],  # 此处xxx.com前，需要带点
            #         'httpOnly': cookie['httpOnly'],
            #         'name': cookie['name'],
            #         'path': cookie['path'],
            #         'secure': cookie['secure'],
            #         'value': cookie['value']
            #     }
            #     if 'expiry' in cookie:
            #         dicts['expiry'] = cookie['expiry']
            #     driver.add_cookie(dicts)
        except:
            print("获取数据包失败，请检查浏览器是否正常打开！")

def open_dir():
    global driver
    driver=chromedriver()
    time.sleep(1)
    driver.get("https://www.booking4.sellingplatformconnect.amadeus.com/app_sell2.0/apf/init/login?SITE=LOGINURL&LANGUAGE=CN&refreshOnError=true")
    print("打开网页")

    # time.sleep(3)
    # try:
    #     driver.delete_all_cookies()
    #     with open('cookies.json','r',encoding='utf-8') as f:
    #         listCookies=json.loads(f.read())
    #     for cookie in listCookies:
    #         dicts={
    #             'domain': cookie['domain'],  # 此处xxx.com前，需要带点
    #             'httpOnly':cookie['httpOnly'],
    #             'name': cookie['name'],
    #             'path': cookie['path'],
    #             'secure':cookie['secure'],
    #             'value': cookie['value']
    #         }
    #         if 'expiry' in cookie:
    #             dicts['expiry']=cookie['expiry']
    #         driver.add_cookie(dicts)
    # except:
    #     print("读取cookies失败")

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass

# data = """data=%7B%22jSessionId%22%3A%22hkqDiT3JtmKPO7J9NJ7GXTex_7sJJ96Wc6FyptYE!1633853230266%22%2C%22contextId%22%3A%22dc1822950a552d33ec475892a26cf9e755bdf838120750c2dddd8e904593eaaf%22%2C%22userId%22%3A%22YXIAO%22%2C%22organization%22%3A%22NMC-US%22%2C%22officeId%22%3A%22IAHG32415%22%2C%22gds%22%3A%22AMADEUS%22%2C%22isStatelessCloneRequired%22%3Afalse%2C%22tasks%22%3A%5B%7B%22type%22%3A%22CRY%22%2C%22command%22%3A%7B%22command%22%3A%22AD28octSVOPVG%2FASU%2FCW%2CY%22%2C%22prohibitedList%22%3A%22SITE_JCPCRYPTIC_PROHIBITED_COMMANDS_LIST_2%22%7D%7D%2C%7B%22type%22%3A%22PAR%22%2C%22parserType%22%3A%22screens.ScreenTypeParser%22%7D%2C%7B%22type%22%3A%22PAR%22%2C%22parserType%22%3A%22screens.ScreenTypeParser%22%7D%2C%7B%22type%22%3A%22ACT%22%2C%22actionType%22%3A%22speedmode.SpeedModeAction%22%2C%22args%22%3A%7B%22argsType%22%3A%22speedmode.SpeedModeActionArgs%22%2C%22obj%22%3A%7B%7D%7D%7D%2C%7B%22type%22%3A%22PAR%22%2C%22parserType%22%3A%22pnr.PnrParser%22%7D%5D%7D"""
# data1="""data=%7B%22jSessionId%22%3A%22Tc5Yv3mpAng92KRr-SvFM4kwYpMmTlJ-Wl_wE86o!1633863588389%22%2C%22contextId%22%3A%22dc1822950a555825ef35328fdc6efc9952a2f838120750c2dddd8e904593eaaf%22%2C%22userId%22%3A%22YXIAO%22%2C%22organization%22%3A%22NMC-US%22%2C%22officeId%22%3A%22IAHG32415%22%2C%22gds%22%3A%22AMADEUS%22%2C%22isStatelessCloneRequired%22%3Afalse%2C%22tasks%22%3A%5B%7B%22type%22%3A%22CRY%22%2C%22command%22%3A%7B%22command%22%3A%22AD28octSVOPVG%2FASU%2FCW%2CY%22%2C%22prohibitedList%22%3A%22SITE_JCPCRYPTIC_PROHIBITED_COMMANDS_LIST_2%22%7D%7D%2C%7B%22type%22%3A%22PAR%22%2C%22parserType%22%3A%22screens.ScreenTypeParser%22%7D%2C%7B%22type%22%3A%22PAR%22%2C%22parserType%22%3A%22screens.ScreenTypeParser%22%7D%2C%7B%22type%22%3A%22ACT%22%2C%22actionType%22%3A%22speedmode.SpeedModeAction%22%2C%22args%22%3A%7B%22argsType%22%3A%22speedmode.SpeedModeActionArgs%22%2C%22obj%22%3A%7B%7D%7D%7D%2C%7B%22type%22%3A%22PAR%22%2C%22parserType%22%3A%22pnr.PnrParser%22%7D%5D%7D"""
# while(1):
#     get_count(data)
#     get_count(data1)
#come_thread_put=threading.Thread(target=get_count,args=(data))
#come_thread=threading.Thread(target=get_count,args=(data1))
#come_thread_put.start()
#come_thread.start()