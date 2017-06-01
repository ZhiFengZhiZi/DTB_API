import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB


class emp_checkRoleName(unittest.TestCase):
    ''' 校验角色名称接口 '''

    def setUp(self):

        table_name = "ua_role"
        self.data = {'ROLE_CODE':'ROLE01','ROLE_NAME': '测试角色α', 'PINYIN': 'AERFA','STATUS': '1'}

        db = DB()
        db.insert(table_name=table_name, table_data=self.data)
        self.sdata = {'ROLE_NAME': '测试角色α'}
        self.s1 = db.select(table_value='id', table_name=table_name, table_data=self.sdata)
        print("id:"+str(self.s1))
        db.close()

        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/role/checkRoleName.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_duplicate_name(self):
        ''' 重复的角色名'''
        payload = {"roleId":self.s1,"roleName":"测试角色α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
 #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'],None)
        time.sleep(1)

    def test_Mismatching_name(self):
        '''不匹配的角色名 '''
        payload = {"roleId": self.s1, "roleName": "测试角色β"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_part_matching_name(self):
        '''部分匹配的角色名 '''
        payload = {"roleId": self.s1, "roleName": "测试"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_null_name(self):
        '''空的角色名 '''
        payload = {"roleId": self.s1, "roleName": ""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_null_all(self):
        '''全部为空的数据 '''
        payload = {"roleId":"", "roleName": ""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
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

        self.table_name = "ua_role"
        self.data = {'ROLE_NAME': '测试角色α'}
        self.data2 = {'ROLE_NAME': '测试角色β'}
        db = DB()
        db.clear(table_name=self.table_name,table_data=self.data)
        db.clear(table_name=self.table_name, table_data=self.data2)
        db.close()

        print(self.result)


if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()