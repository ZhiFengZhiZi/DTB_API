import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
from db import test_data

class emp_people_search(unittest.TestCase):
    ''' 人员查询接口 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        test_data.ua_emp_insert(count=1)

        self.empid=test_data.ua_emp_search(value="id",type='β')

        test_data.ua_roleemp_insert(empid=self.empid,roleid=1)


        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/emp/getEmpInfoList"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_get_userinfo(self):
        ''' 正确的参数_all'''

        payload = {"empName": "ZHANGHAO2","empCname": "测试账号β","cellphone":"123456","pageSize":"10","starts":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], True)

    def test_get_userinfo_empcname(self):
        ''' 正确的参数_单独查询人员名称'''

        payload = {"empCname":"测试账号β"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], True)


    def test_get_userinfo_empname(self):
        ''' 正确的参数_单独查询人员账号'''

        payload = {"empName": "ZHANGHAO2"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], True)


    def test_get_userinfo_empphone(self):
        ''' 正确的参数_单独查询手机号'''

        payload = {"cellPhone": "123456"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], True)



    def test_get_userinfo_wrong_empcname(self):
        ''' 不存在的参数_单独查询人员名称'''

        payload = {"empCname": "测试账号Z"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], False)



    def test_get_userinfo_wrong_empname(self):
        ''' 错误的参数_单独查询人员账号'''

        payload = {"empName": "ZHANGHAO123"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()


        self.assertEqual(self.result['result'], False)


    def test_get_userinfo_wrong_empphone(self):
        ''' 错误的参数_单独查询手机号'''

        payload = {"cellPhone": "0000"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], False)






    def test_get_userinfo_wrong_starts(self):
        ''' 错误的的参数_不存在的分页'''

        payload = {"empName": "ZHANGHAO2","empCname": "测试账号β","cellphone":"123456","pageSize":"10","starts":"3"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], False)



    def test_get_userinfo_wrong_data(self):
        ''' 错误的的参数_账号、账号名、手机号'''

        payload = {"empName": "ZHANGHAOXX","empCname": "测试账号XX","cellphone":"123456XXX","pageSize":"10","starts":"0"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], False)



    def test_get_userinfo_space_data(self):
        ''' 错误的的参数_空的_账号、账号名、手机号'''

        payload = {"empName": "","empCName": "","cellphone":"","pageSize":"10","starts":"0"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], False)



    def tearDown(self):
        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_emp_delete(type='β',id=self.empid)

        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()