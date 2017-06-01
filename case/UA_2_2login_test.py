import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data


class emp_login(unittest.TestCase):
    ''' 后台登录接口 '''

    def setUp(self):
        self.base_url = urlbase.sit_emp()+"/login"



    def test_login_success(self):
        ''' 正确的参数 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'ceshi','password':'123456','verifyCode':'0000'}
        r = requests.post('http://192.168.31.188:9280/login',data=payload,headers=head)
        self.result = r.json()

        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['success'], True)


    def test_login_pwd_wrong(self):
        ''' 错误的密码 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'ceshi','password':'654321','verifyCode':'0000'}
        r = requests.post('http://192.168.31.188:9280/login',data=payload,headers=head)
        self.result = r.json()

        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)


    def test_login_loginname_wrong(self):
        ''' 错误的账号 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'aaaaa','password':'123456','verifyCode':'0000'}
        r = requests.post('http://192.168.31.188:9280/login',data=payload,headers=head)
        self.result = r.json()

        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)

    def test_login_code_wrong(self):
        ''' 错误的验证码 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'ceshi','password':'123456','verifyCode':'1111'}
        r = requests.post('http://192.168.31.188:9280/login',data=payload,headers=head)
        self.result = r.json()

        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)

    def test_login_null(self):
        ''' 全部都为空值 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'','password':'','verifyCode':''}
        r = requests.post('http://192.168.31.188:9280/login',data=payload,headers=head)
        self.result = r.json()

        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)


    def test_login_null2(self):
        ''' 除验证码外都为空值 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'','password':'','verifyCode':'0000'}
        r = requests.post('http://192.168.31.188:9280/login',data=payload,headers=head)
        self.result = r.json()

        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)

    def tearDown(self):
        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()