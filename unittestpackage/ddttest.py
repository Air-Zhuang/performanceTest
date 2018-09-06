# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/5 23:00'
import unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print '======setUp======'
    @data("aaa","bbb","ccc")
    def test_single_param(self,value):
        print '======test_single_param======'
        print value
        # print self.__class__.__name__

    # @data((1,2),(3,4),(5,6))
    # @unpack
    # def test_multi_param(self,value1,value2):
    #     print '======test_multi_param======'
    #     print value1+value2

    def tearDown(self):
        print '======tearDown======'


if __name__ == '__main__':
    unittest.main()
