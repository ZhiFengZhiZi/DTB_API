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
        test_data.ua_emp_insert(count=1)
        test_data.ua_role_insert(count=1)
        self.empid = test_data.ua_emp_search(value='id',type='β')
        self.role = test_data.ua_role_search(value='id',type='α')
        test_data.ua_roleemp_insert(empid=self.empid, roleid=1)
        test_data.ua_role_insert(1)


        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/role/checkRoleName"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_duplicate_name(self):
        ''' 重复的角色名'''
        payload = {"roleId":self.role,"roleName":"测试角色α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
 #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)
        time.sleep(1)

    def test_Mismatching_name(self):
        '''不存在的角色名 '''
        payload = {"roleId": self.role, "roleName": "测试角色β"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_part_matching_name(self):
        '''部分匹配的角色名 '''
        payload = {"roleId": self.role, "roleName": "测试"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_null_name(self):
        '''空的角色名 '''
        payload = {"roleId": self.role, "roleName": ""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_null_all(self):
        '''全部为空的数据 '''
        payload = {"roleId":"", "roleName": ""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_Nonexistent_id(self):
        '''不存在的id '''
        payload = {"roleId":9989, "roleName":"测试角色α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_only_name(self):
        '''单独传存在的角色名 '''
        payload = { "roleName":"测试角色α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_emp_delete(type='β',id=self.empid)
        test_data.ua_role_delete('α')


        print(self.result)


if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()