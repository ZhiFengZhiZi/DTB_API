import sys
import time
import unittest
sys.path.append('./case')
sys.path.append('./db_fixture')

import HTMLTestRunner


# 指定测试用例为当前文件夹下的 interface 目录


class report():

    def __init__(self):
        self.test_dir = './case'
        self.discover = unittest.defaultTestLoader.discover(self.test_dir, pattern='*_test.py',top_level_dir=None)


    def run(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        self.filename = './report/' + self.now + '_result.html'
        self.fp = open(self.filename, 'wb')


        self.runner = HTMLTestRunner.HTMLTestRunner(stream=self.fp,
                                title='Guest Manage System Interface Test Report',
                                description='Implementation Example with: ')

        self.runner.run(self.discover)
        self.fp.close()

if __name__ == "__main__":
#    test_data.init_data() # 初始化接口测试数据


    report().run()
