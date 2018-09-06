# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/3 22:10'


import os
import time
import csv

class App(object):
    def __init__(self):
        self.content=""
        self.startTime=0
    def LaunchApp(self):#启动
        cmd='adb shell am start -W -n com.android.browser/.BrowserActivity'
        self.content=os.popen(cmd)
    def StopApp(self):#停止App
        #冷启动结束
        # cmd='adb shell am force-stop com.android.browser'
        #热启动结束
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)
    def GetLaunchedTime(self):#获取启动时间
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime=line.split(":")[1]
                break
        return self.startTime
class Controller(object):
    def __init__(self,count):
        self.app=App()
        self.counter=count
        self.alldata=[("timestamp","elapsedtime")]
    def testprocess(self):#单次测试过程
        self.app.LaunchApp()
        time.sleep(0.5)
        elapsedtime=self.app.GetLaunchedTime()
        self.app.StopApp()
        time.sleep(0.5)
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime,elapsedtime))
    def run(self):#多次执行
        while self.counter>0:
            self.testprocess()
            self.counter=self.counter-1
    def getCurrentTime(self):
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime
    def SaveDataToCSV(self):
        csvfile=file('startTime.csv','wb')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()
if __name__ == '__main__':
    controller=Controller(6)
    controller.run()
    controller.SaveDataToCSV()