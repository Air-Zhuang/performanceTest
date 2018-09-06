# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/5 19:08'

import os
import time
import csv

class Controller(object):
    def __init__(self,count):
        self.counter = count
        self.alldata = [("timestamp", "power")]
    def testprocess(self):
        result=os.popen("adb shell dumpsys battery")
        for line in result:
            if "level" in line:
                power=line.split(":")[1]
        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,power))
    def run(self):
        os.popen("adb shell dumpsys battery set status 1") #将手机设为非充电状态
        while self.counter>0:
            self.testprocess()
            self.counter=self.counter-1
            time.sleep(3)
    def getCurrentTime(self):
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime
    def SaveDataToCSV(self):
        csvfile=file('power.csv','wb')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()
if __name__ == '__main__':
    controller=Controller(5)
    controller.run()
    controller.SaveDataToCSV()