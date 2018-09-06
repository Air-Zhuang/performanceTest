# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/3 23:17'

import os
import time
import csv

class Controller(object):
    def __init__(self,count):
        self.counter=count
        self.alldata=[("timestamp","cpustatus")]
    def testprocess(self):
        result=os.popen("adb shell dumpsys cpuinfo | grep com.android.browser")
        for line in result.readlines():
            cpuvalue=line.split("%")[0]
        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,cpuvalue))
    def run(self):
        while self.counter>0:
            self.testprocess()
            self.counter-=1
            time.sleep(3)
    def getCurrentTime(self):
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime
    def SaveDataToCSV(self):
        csvfile=file('cpustatus.csv','wb')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()
if __name__ == '__main__':
    controller=Controller(6)
    controller.run()
    controller.SaveDataToCSV()