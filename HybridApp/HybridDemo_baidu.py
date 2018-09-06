# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/7 0:09'

from appium import webdriver
import time
import os

# os.system("taskkill -F -PID node.exe")
def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6'
    desired_caps['deviceName'] = '8ae28a45'
    desired_caps['appPackage'] = 'com.baidu.searchbox'
    desired_caps['appActivity'] = '.MainActivity'
    desired_caps['udid'] = '8ae28a45'           #苹果id
    desired_caps['noReset'] = 'True'            #如果不是True，每次启动app都会清除数据，是True，不需要再次安装
    desired_caps['unicodeKeyboard'] = 'True'    #unicodeKeyboard的编码方式来发送字符串
    desired_caps['resetKeyboard'] = 'True'      #将键盘隐藏起来
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
if __name__ == '__main__':
    driver=get_driver()
    time.sleep(5)
    driver.find_element_by_id('com.baidu.searchbox:id/baidu_searchbox').click()
    time.sleep(1)
    driver.find_element_by_id('com.baidu.searchbox:id/SearchTextInput').send_keys('clannad')
    time.sleep(1)
    driver.find_element_by_id('com.baidu.searchbox:id/float_search_or_cancel').click()
    time.sleep(1)
    driver.find_element_by_id('com.baidu.searchbox:id/baidu_searchbox').click()


    # driver.find_element_by_id('com.android.browser:id/url').send_keys('clannad')
    # time.sleep(1)
    # driver.find_element_by_id('com.example.zhangjian.minibrowser2:id/searchbutton').click()
    # time.sleep(1)
    # print driver.contexts
    # time.sleep(1)
    # driver.switch_to.context('WEBVIEW_0')
    # time.sleep(1)
    # print driver.current_context
    # time.sleep(1)
    # driver.find_element_by_id('android.widget.EditText').click()
    # time.sleep(1)
    # driver.find_element_by_id('android.widget.EditText').send_keys('clannad')
    # time.sleep(1)
    # driver.find_element_by_id('android.widget.Button').click()
    # time.sleep(1)
    # time.sleep(3)
    # driver.quit()
    # os.system("taskkill -F -PID node.exe")