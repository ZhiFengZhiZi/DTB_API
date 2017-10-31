import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db.mysql_db import DB
import time
from db import  test_data
class get_getEmpResource(unittest.TestCase):
    ''' 欢迎页获取用户权限接口 '''

    def setUp(self):
        self.emp = urlbase.UA_url()
        self.base_url = self.emp + "/emp/updatePwd"
        self.base_url_login = self.emp + "/login"

        test_data.ua_emp_insert(count=1)


        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()

        r1 = self.s.post(self.base_url_login, data=payload, headers=head).json()
        print(r1)
        self.token = r1["resultObject"]
        print(self.token)



    def test_token_success(self):
        ''' 正确的token和原密码'''


        payload = {"token":self.token,'newPassword':'123456','oldPassword':'234567'}
        r2 = self.s.post(self.base_url, data=payload)
        print(r2.text)

        self.result = r2.json()
        self.assertEqual(self.result['result'], True)

        pwd=test_data.ua_emp_search(value="PASSWORD",type='β')
        self.assertEqual(pwd, 'e10adc3949ba59abbe56e057f20f883e')


    def test_old_wrong(self):
        ''' 正确的token和原密码'''


        payload = {"token":self.token,'newPassword':'123456','oldPassword':'789456'}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)

        pwd=test_data.ua_emp_search(value="PASSWORD",type='β')
        self.assertEqual(pwd, '508df4cb2f4d8f80519256258cfb975f')


    def test_token_wrong(self):
        ''' 错误的token'''

        payload = {"token":123456,'oldPassword':'123456','newPassword':'654321'}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        pwd = test_data.ua_emp_search(value="PASSWORD", type='β')
        self.assertEqual(pwd, '508df4cb2f4d8f80519256258cfb975f')

    def test_pwd_wrong(self):
        ''' 错误的的密码'''

        payload = {"token":self.token,'oldPassword':'000000','newPassword':'654321'}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        pwd = test_data.ua_emp_search(value="PASSWORD", type='β')
        self.assertEqual(pwd, '508df4cb2f4d8f80519256258cfb975f')

    def test_token_null(self):
        ''' 空的token'''

        payload = {"token":'', 'oldPassword': '123456', 'newPassword': '654321'}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        pwd = test_data.ua_emp_search(value="PASSWORD", type='β')
        self.assertEqual(pwd, '508df4cb2f4d8f80519256258cfb975f')

    def test_pwd_null(self):
        ''' 空的密码'''

        payload = {"token":self.token, 'oldPassword': '', 'newPassword': '654321'}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        pwd = test_data.ua_emp_search(value="PASSWORD", type='β')
        self.assertEqual(pwd, '508df4cb2f4d8f80519256258cfb975f')



    def tearDown(self):
        self.empid = test_data.ua_emp_search(value="id", type='β')
        test_data.ua_emp_delete(type='β',id=self.empid)
        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()