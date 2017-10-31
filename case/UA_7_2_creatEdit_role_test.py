import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
from db import test_data



class emp_createEdit_role_info(unittest.TestCase):
    ''' 新增编辑角色详情接口 '''

    def setUp(self):
        self.emp = urlbase.UA_url()
        test_data.ua_role_insert(count=1)
        test_data.ua_emp_insert(count=1)

        self.empid = test_data.ua_emp_search(value='id', type='β')
        self.roleid=test_data.ua_role_search(value='id',type='α')

        test_data.ua_roleemp_insert(empid=self.empid,roleid='1')

        self.base_url_login = self.emp + "/login"

        self.base_url = self.emp + "/role/addRoleInfo"

        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()

        r1 = self.s.post(self.base_url_login, data=payload, headers=head)
        print(r1.text)


    def test_createparams_correct(self):
        ''' 正确的参数_all（新增）'''
        payload = {"empId":self.empid,"roleName":"测试角色β","remark":"我是描述","opType":"0"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        s=test_data.ua_role_search(value='ROLE_NAME',type='β')
        self.assertEqual(s,'测试角色β')
        time.sleep(1)

    def test_createparams_opTypeNull_correct(self):
        ''' 正确的参数_all（opType不传，默认新增）'''
        payload = {"empId":self.empid,"roleName":"测试角色β","remark":"我是描述"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        s=test_data.ua_role_search(value='ROLE_NAME',type='β')
        self.assertEqual(s,'测试角色β')
        time.sleep(1)


    def test_createparams_allnull_incorrect(self):
        ''' 错误的参数_allNull'''
        payload = {"id":"","empId":"","roleName":"","remark":""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        time.sleep(1)


    def test_editparams_correct(self):
        ''' 正确的参数_all（编辑）'''
        payload = {"id":self.roleid,"empId":self.empid,"roleName":"测试角色β","remark":"我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        s=test_data.ua_role_search(value='ROLE_NAME',type='β')
        self.assertEqual(s,'测试角色β')
        time.sleep(1)


    def test_editparams_remarkNull_correct(self):
        ''' 正确的参数_remarkNull（编辑）'''
        payload = {"id":self.roleid,"empId":self.empid,"roleName":"测试角色β","remark":"","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        s=test_data.ua_role_search(value='ROLE_NAME',type='β')
        self.assertEqual(s,'测试角色β')
        time.sleep(1)


    def test_editparams_id_incorrect(self):
        ''' 错误的参数_不存在的Id（编辑）'''
        payload = {"id":9998,"empId":self.empid,"roleName":"测试角色β", "remark": "我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)


    def test_editparams_idNull_incorrect(self):
        ''' 错误的参数_空的Id（编辑）'''
        payload = {"id":"","empId":self.empid,"roleName":"测试角色β", "remark": "我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)


    def test_editparams_roleNameNull_incorrect(self):
        ''' 错误的参数_name为空值'''
        payload = {"id":self.roleid,"empId":self.empid,"roleName":"", "remark": "我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)

    def test_editparams_roleNameSame_incorrect(self):
        ''' 错误的参数_name值为原值'''
        payload = {"empId":self.empid,"roleName":"测试角色α", "remark": "我是描述","opType":"0"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)



    def tearDown(self):
        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_role_delete(type='α')
        test_data.ua_role_delete(type='β')

        test_data.ua_emp_delete(type='β',id=self.empid)


        print(self.result)


if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()