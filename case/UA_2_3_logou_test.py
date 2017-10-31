import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data


class emp_login(unittest.TestCase):
    ''' 后台登出接口 '''

    def setUp(self):
        self.emp = urlbase.UA_url()
        self.base_url = self.emp +"/logout"
        self.base_url_login = self.emp + "/login"





    def test_login_pwd_wrong(self):
        ''' 登录以后执行 '''
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login,  headers=head)


        r = self.s.get(self.base_url,)
        self.result = r.json()

        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)


    def tearDown(self):
        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()