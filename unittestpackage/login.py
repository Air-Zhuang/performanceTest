# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/5 21:14'

from appium import webdriver
import time
import os

def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6'
    desired_caps['deviceName'] = '8ae28a45'
    desired_caps['appPackage'] = 'com.mook.mook'
    desired_caps['appActivity'] = '.LoginActivity'
    desired_caps['udid'] = '8ae28a45'           #苹果id
    desired_caps['noReset'] = 'True'            #如果不是True，每次启动app都会清除数据，是True，不需要再次安装
    desired_caps['unicodeKeyboard'] = 'True'    #unicodeKeyboard的编码方式来发送字符串
    desired_caps['resetKeyboard'] = 'True'      #将键盘隐藏起来
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
if __name__ == '__main__':
    driver=get_driver()
    time.sleep(5)
    driver.find_element_by_id('com.mook.mook:id/email').send_keys('aaaa')
    time.sleep(1)
    driver.find_element_by_id('com.mook.mook:id/password').send_keys('123456')
    time.sleep(1)
    driver.find_element_by_id('com.mook.mook:id/email_sign_in_button').click()

    time.sleep(3)
    driver.quit()
    os.system("taskkill -F -PID node.exe")