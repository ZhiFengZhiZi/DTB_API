import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB


class emp_people_search(unittest.TestCase):
    ''' 人员查询接口 '''

    def setUp(self):

        self.table_name = "ua_employee"
        self.data = {'EMP_CNAME': '测试账号α','EMP_NAME':'ZHANGHAO1','PASSWORD':'e10adc3949ba59abbe56e057f20f883e','EMP_STATUS':'1','CELL_PHONE':'123456'}
        db=DB()
        db.insert(table_name=self.table_name,table_data=self.data)
        db.close()


        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_get_userinfo(self):
        ''' 正确的参数_all'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empName": "ZHANGHAO1","empCName": "测试账号α","cellphone":"123456","pageSize":"10","starts":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['starts'], 1)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 1)

    def test_get_userinfo_empcname(self):
        ''' 正确的参数_单独查询人员名称'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empCname":"测试账号α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['starts'], 1)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 1)

    def test_get_userinfo_empname(self):
        ''' 正确的参数_单独查询人员账号'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empName": "ZHANGHAO1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['starts'], 1)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 1)

    def test_get_userinfo_empphone(self):
        ''' 正确的参数_单独查询手机号'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"cellPhone": "123456"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['starts'], 1)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 1)


    def test_get_userinfo_wrong_empcname(self):
        ''' 错误的参数_单独查询人员名称'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empCName": "测试账号Z"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['starts'], 0)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 0)


    def test_get_userinfo_wrong_empname(self):
        ''' 错误的参数_单独查询人员账号'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empName": "ZHANGHAO123"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['starts'], 0)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 0)

    def test_get_userinfo_wrong_empphone(self):
        ''' 错误的参数_单独查询手机号'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"cellPhone": "0000"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['starts'], 0)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 0)





    def test_get_userinfo_wrong_starts(self):
        ''' 错误的的参数_不存在的分页'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empName": "ZHANGHAO1","empCName": "测试账号a","cellphone":"123456","pageSize":"10","starts":"3"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['starts'], 0)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 0)


    def test_get_userinfo_wrong_data(self):
        ''' 错误的的参数_账号、账号名、手机号'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empName": "ZHANGHAOXX","empCName": "测试账号XX","cellphone":"123456XXX","pageSize":"10","starts":"0"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['starts'], 0)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 0)


    def test_get_userinfo_space_data(self):
        ''' 错误的的参数_空的_账号、账号名、手机号'''
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empName": "","empCName": "","cellphone":"","pageSize":"10","starts":"0"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['starts'], 0)
        self.assertEqual(self.result['pageSize'], 10)
        self.assertEqual(self.result['totalCount'], 1)


    def tearDown(self):

        self.table_name = "ua_employee"
        self.data = {'EMP_CNAME': '测试账号α'}
        db = DB()
        db.clear(table_name=self.table_name,table_data=self.data)
        db.close()

        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()