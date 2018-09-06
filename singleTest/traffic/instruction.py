# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/3 23:41'

'''
        流量
获取进程ID指令
    adb shell ps | grep packagename
获取进程ID流量
    adb shell cat /proc/pid/net/dev
        (看wlan0，对应的received和transmit)
        (执行两次指令，中间夹带操作，结果做差)
'''