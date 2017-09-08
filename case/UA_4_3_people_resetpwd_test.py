import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
import time
from db import test_data

class emp_people_resetpwd(unittest.TestCase):
    ''' 重置密码接口 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/emp/resetPwd"

        test_data.ua_emp_insert(count=1)

        self.empid1 = test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.empid1, roleid=1)

        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)

    def test_param_correct(self):
        ''' 正确的参数_id'''

        payload = {"id":self.empid1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)

        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_param_null(self):
        '''错误的参数_空值'''

        payload = {"id":""}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_param_wrong(self):
        '''错误的参数_不存在的id'''
        payload = {"id":"99999999"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)



    def tearDown(self):
        test_data.ua_roleemp_delete(EMP_ID=self.empid1)
        test_data.ua_emp_delete(type='β',id=self.empid1)
        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()