import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db.mysql_db import DB
import time
from db import test_data
class get_userinfo(unittest.TestCase):
    ''' 欢迎页获取用户信息接口 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        self.base_url = self.emp+"/emp/getEmpInfo"
        self.base_url_login = self.emp + "/login"


        test_data.ua_emp_insert(count=1)
        self.empid=test_data.ua_emp_search(value="id",type='β')

        test_data.ua_roleemp_insert(empid=self.empid,roleid=1)


        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()


        r1 = self.s.post(self.base_url_login, data=payload, headers=head).json()
        self.token = r1["resultObject"]
        print(r1)

    def test_token_success(self):
        ''' 正确的token'''

        payload = {"token":self.token}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject']['empName'], "ZHANGHAO2")

    def test_token_wrong(self):
        ''' 错误的token'''

        payload = {"token":123456}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)




    def tearDown(self):
        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_emp_delete(type='β',id=self.empid)


        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()