# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/3 23:58'

import time
import os
import csv
import string

class Controller(object):
    def __init__(self,count):
        self.counter=count
        self.alldata = [("timestamp", "traffic")]
    def testprocess(self):
        result=os.popen("adb shell ps | grep com.android.browser")
        pid=result.readlines()[0].split(" ")[5]
        traffic=os.popen("adb shell cat /proc/"+pid+"/net/dev")
        for line in traffic:
            if "wlan0" in line:
                line="#".join(line.split()) #将所有空行换成#
                receive=line.split("#")[1]
                transmit=line.split("#")[9]
        alltraffic=string.atoi(receive)+string.atoi(transmit)   #这两行将字节转换成KB
        alltraffic=alltraffic/1024
        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,alltraffic))
    def run(self):
        while self.counter>0:
            self.testprocess()
            self.counter-=1
            time.sleep(3)
    def getCurrentTime(self):
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime
    def SaveDataToCSV(self):
        csvfile=file('traffic.csv','wb')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()
if __name__ == '__main__':
    controller=Controller(5)
    controller.run()
    controller.SaveDataToCSV()