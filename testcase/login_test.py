import unittest

from business.login import login_test
from data.testdata import get_csv_data


class TestLogin(unittest.TestCase):
    # 测试开始前执行
    def setUp(self):
        print('开始测试')

    # 测试结束后执行
    def tearDown(self):
        print('结束测试')

    # 登录的用例
    def test_login(self):
        # 获取文件路径
        csv_file = '../data/login_data.csv'
        # 读取文件内容
        data = get_csv_data(csv_file)
        for i in range(len(data)):
            print('\n这是第'+str(i+1)+'次测试')
            data1 = data[i].split(',')
            try:
                if data1[2].strip()=='true':
                    self.assertTrue(login_test(data1[0],data1[1]))
                else:
                    self.assertFalse(login_test(data1[0],data1[1]))
            except:
                print('本次测试未通过')
            else:
                print('本次测试通过')