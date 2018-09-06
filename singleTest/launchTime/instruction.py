# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/3 21:01'

'''
        启动时间
启动App命令-冷启动
    adb shell am start -W -n package/activity   (例：adb shell am start -W -n com.android.browser/.BrowserActivity)
停止App命令
    adb shell am force-stop package
启动App命令-热启动
    启动和热启动一样
停止App命令
    adb shell input keyevent 3   (其实是模拟点击一个back键)

自动化实现思路
    1、获取命令执行事件，作为启动事件参考值（推荐，更准确）
    2、在命令前后加上时间戳，以差值作为参考值
'''
'''
做csv数据分析时一般剔除第一行内容
一般做一个均值，再做一个曲线图
业界同类产品做对比
迭代版本之间对比
'''