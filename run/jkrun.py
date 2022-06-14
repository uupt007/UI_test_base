import os
import sys
#声明包查找的路径
from run.BSTestRunner import BSTestRunner
import unittest
import time
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(sys.path)
#指定测试用例和测试报告的路径
test_dir = '../testcase'
report_dir = '../reports'

#给测试报告命名
now = time.strftime("%Y-%m-%d-%H_%M_%S")
report_name = report_dir + '/' + now + 'test_report.html'

#匹配测试多条用例
testcase = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

#运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="我的XX功能测试报告", description="我的XX功能测试报告")
    runner.run(testcase)