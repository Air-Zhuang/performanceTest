# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/5 19:21'

'''
        内存
获取内存
    adb shell top
    adb shell top -d 1 (一秒刷新一次)
    adb shell top -d 1 > meminfo (将内容输入到meminfo文件)
    cat meminfo (查看刚才保存的文件)
    cat meminfo | grep packge (指定应用)
    VSS-Virtual Set Size 虚拟耗用内存
    RSS-Resident Set Size 实际使用物理内存
    (将取出的内存做曲线图，如果发现内存在长时间使用之后趋于一个稳定状态，可以认为我们app没有内存泄露情况)
'''