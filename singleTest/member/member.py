# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/5 19:46'

import csv
import os
import time

'''
执行脚本前先执行
adb shell top -d 1 > meminfo
将内存使用情况记录到dos命令正在使用的目录的meminfo文件下
'''

class Controller(object):
    def __init__(self):
        self.alldata = [("id", "vss", "rss")]
    def analyzedata(self):
        content=self.readfile()
        i=0
        for line in content:
            if "com.android.browser" in line:
                print line
                line="#".join(line.split())
                vss=line.split("#")[5].strip("K")
                rss=line.split("#")[6].strip("K")
                self.alldata.append((i,vss,rss))
                i+=1
    def SaveDataToCSV(self):
        csvfile=file('meminfo.csv','wb')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()
    def readfile(self):
        mfile=file("C:\\Users\\Administrator\\meminfo","r")
        content=mfile.readlines()
        mfile.close()
        return content
if __name__ == "__main__":
    controller = Controller()
    controller.analyzedata()
    controller.SaveDataToCSV()