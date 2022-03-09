import os
import multiprocessing
thread=[]
def cmds(i):
    command = "python " + os.getcwd() + "/" + "Server_run.py " + str(8011 + i)
    os.system(command)

if __name__=="__main__":
    count = input("输入要开启的端口数量：")
    for i in range(int(count)):
        thread=multiprocessing.Process(target=cmds,args=(i,))
        thread.start()
        print(str(8011+i))
