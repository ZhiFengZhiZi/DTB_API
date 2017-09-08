import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
import time
from db import test_data


class emp_people_create(unittest.TestCase):
    ''' 创建编辑人员接口 '''

    def setUp(self):
        test_data.ua_emp_insert(count=1)
        self.emp = urlbase.list()[0]

        self.empid1 = test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.empid1, roleid=1)

        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/emp/saveEmployeeInfo"

        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)

    def test_createparam_correct(self):
        ''' 正确的参数_新增_all'''
        payload = {"empName":"ZHANGHAO1","empCname":"测试账号α","cellphone":"123456","email":"123@qq.com","empNo":"00900","opType":"0"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_editparam_correct(self):
        ''' 正确的参数_修改姓名、账号、电话、邮箱_all'''
        payload = {"id":self.empid1,"empName":"ZHANGHAO1","empCname":"测试账号α","cellphone":"123456","email":"123@qq.com","empNo":"00900","opType":"1"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_createparam_null(self):
        '''错误的参数_空值(opType=0 新增)'''
        payload = {"id":"","empName":"","empCname":"","cellphone":"","email":"1","empNo":"","opType":"0"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_editparam_null(self):
        '''错误的参数_空值(opType=1 编辑)'''
        payload = {"id":"","empName":"","empCname":"","cellphone":"","email":"1","empNo":"","opType":"1"}
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