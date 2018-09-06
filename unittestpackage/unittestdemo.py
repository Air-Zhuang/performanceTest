# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/5 21:14'
import unittest
from appium import webdriver
import time
import os
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print "=======setUp========"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6'
        desired_caps['deviceName'] = '8ae28a45'
        desired_caps['appPackage'] = 'com.mook.mook'
        desired_caps['appActivity'] = '.LoginActivity'
        desired_caps['udid'] = '8ae28a45'  # 苹果id
        desired_caps['noReset'] = 'True'  # 如果不是True，每次启动app都会清除数据，是True，不需要再次安装
        desired_caps['unicodeKeyboard'] = 'True'  # unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = 'True'  # 将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @data(('aaaa', '123456'), ('q@qq.com', '123456'))
    @unpack
    def test_something(self,name,password):
        print "=======test_something========"
        time.sleep(3)
        self.driver.find_element_by_id('com.mook.mook:id/email').send_keys(name)
        time.sleep(1)
        self.driver.find_element_by_id('com.mook.mook:id/password').send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id('com.mook.mook:id/email_sign_in_button').click()
        time.sleep(3)
    def tearDown(self):
        print "=======tearDown========"
        self.driver.quit()
        # os.system("taskkill -F -PID node.exe")


if __name__ == '__main__':
    # mysuit=unittest.TestSuite()
    # mysuit.addTest(MyTestCase.test_something())

    #以类的形式(这样可以实现多个unittest python文件之间的不同case的组合)
    cases=unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    mysuit=unittest.TestSuite([cases])
    # mysuit.addTest(MyTestCase.test_something()) #在使用ddt时这条就不要用了

    myrunner=unittest.TextTestRunner(verbosity=2) #verbosity=2感觉像是多了路径
    myrunner.run(mysuit)
