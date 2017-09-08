import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
from db import test_data

class emp_phone_duplicate(unittest.TestCase):
    ''' 人员邮箱查重接口 '''

    def setUp(self):

        test_data.ua_emp_insert(count=2)
        self.emp = urlbase.list()[0]
        self.empid1 = test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.empid1, roleid=1)

        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/emp/checkEmpName"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_params_correct(self):
        ''' 正确的参数_不存在的邮箱'''
        payload = {"empId":self.empid1,"empName":"ZHANGHAO3"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_param_now_correct(self):
        ''' 正确的参数_当前的邮箱'''
        payload = {"empId":self.empid1,"empName":"ZHANGHAO2"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_phone_null(self):
        ''' 错误的参数_邮箱为空'''

        payload = {"empId":self.empid1,"empName":""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_get_userinfo_wrong_empphone(self):
        ''' 错误的参数_存在的邮箱'''
        payload = {"empId":self.empid1,"empName":"ZHANGHAO1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_get_userinfo_wrong_id(self):
        ''' 错误的参数_不存在的id'''
        payload = {"empId": 99998, "empName": "ZHANGHAO2"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def tearDown(self):
        self.empid2 = test_data.ua_emp_search(value='id', type='α')
        test_data.ua_roleemp_delete(EMP_ID=self.empid1)
        test_data.ua_emp_delete(type='β',id=self.empid1)
        test_data.ua_emp_delete(type='α',id=self.empid2)
        print(self.result)


if __name__ == '__main__':

    unittest.main()