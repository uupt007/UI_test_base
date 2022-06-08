import os
import sys
import unittest
import warnings

from business.xuanke_bus import jk_xuanke
from data.testdata import get_csv_data
sys.path.append('..')

class TestXUANKE(unittest.TestCase):
    csv_file = os.path.abspath(os.path.dirname(os.getcwd())) +"/data/xuanke.csv"
    def setUp(self):
        print("开始测试~")
        # 这句话的作用是用来忽略 ResourceWaring 异常警告的
        warnings.simplefilter("ignore", ResourceWarning)
    def  tearDown(self):
        print("结束测试~")
    def test_xuanke_111(self):
        print("第一条选课用例测试~")
        print(self.csv_file)
        # 获取csv文件中的第一行数据
        data = get_csv_data(self.csv_file,1)
        # 预期失败用例（获取第一列和第二列数据）交给 登录
        self.assertTrue(jk_xuanke(data[0],data[1],data[2]))
    def test_xuanke_222(self):
        # 读取CSV的第二行数据
        print("第二条选课用例测试~")
        data = get_csv_data(self.csv_file,2)
        # 预期失败用例
        self.assertTrue(jk_xuanke(data[0],data[1], data[2]))
    def test_xuanke_333(self):
        print("第三条选课用例测试~")  # 获取csv文件中的第三行数据
        data = get_csv_data(self.csv_file, 3)
        # 预期失败用例
        self.assertFalse(jk_xuanke(data[0], data[1], data[2]))
if __name__ == '__main__':
    unittest.main()





