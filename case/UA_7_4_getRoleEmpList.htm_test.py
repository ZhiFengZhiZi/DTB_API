import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_checkRoleName(unittest.TestCase):
    ''' 校验角色名称接口 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        test_data.ua_emp_insert(count=2)
        test_data.ua_role_insert(count=1)
        self.empid = test_data.ua_emp_search(value='id',type='β')
        self.emp1 = test_data.ua_emp_search(value='id', type='α')
        self.role = test_data.ua_role_search(value='id',type='α')
        test_data.ua_roleemp_insert(empid=self.empid, roleid=1)
        test_data.ua_roleemp_insert(empid=self.emp1, roleid=self.role)
        test_data.ua_role_insert(1)


        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/role/getRoleEmpList"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)
        print(r1.json())


    def test_ExistingCheck_id(self):
        '''存在check关系的角色id'''
        payload = {"roleId":self.role}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'],True)
        self.assertEqual(self.result['roleName'],'测试角色α')


    def test_Nonexistent_id(self):
        '''不存在的角色id'''
        payload = {"roleId":9987845}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'],False)
 #       self.assertEqual(self.result['roleName'],'测试角色α')

    def test_null_id(self):
        '''不存在的角色id'''
        payload = {"roleId":""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'],False)


    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_roleemp_delete(EMP_ID=self.emp1)
        test_data.ua_emp_delete(type='β',id=self.empid)
        test_data.ua_emp_delete(type='α',id=self.emp1)
        test_data.ua_role_delete('α')


        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()