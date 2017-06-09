import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data


class emp_login(unittest.TestCase):
    ''' 验证码接口 '''

    def setUp(self):
        self.base_url = urlbase.sit_emp()+"/verifyCode"



    def test_login_success(self):
        ''' 验证码接口'''

        ##以x-www-form-urlencoded
        r = requests.get(self.base_url)
        self.result = r.status_code
        self.assertEqual(self.result,200)



    def tearDown(self):
        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()