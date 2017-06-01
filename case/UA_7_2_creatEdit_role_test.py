import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB


class emp_createEdit_role_info(unittest.TestCase):
    ''' 新增编辑角色详情接口 '''

    def setUp(self):

        table_name = "ua_role"
        self.data = {'ROLE_CODE':'ROLE01','ROLE_NAME': '测试角色α', 'PINYIN': 'AERFA','STATUS': '1'}

        db = DB()
        db.insert(table_name=table_name, table_data=self.data)
        sdata = {'ROLE_NAME': '测试角色α'}
        self.s1 = db.select(table_value='id', table_name=table_name, table_data=sdata)
        print("id:"+str(self.s1))
        db.close()

        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/role/getRoleInfoList.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_createparams_correct(self):
        ''' 正确的参数_all（新增）'''
        payload = {"roleName":"测试角色β","remark":"我是描述","opType":"0"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
 #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], '测试角色β')

        time.sleep(1)

    def test_createparams_opTypeNull_correct(self):
        ''' 正确的参数_all（opType不传，默认新增）'''
        payload = {"roleName":"测试角色β", "remark": "我是描述"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], '测试角色β')

        time.sleep(1)

    def test_createparams_id_incorrect(self):
        ''' 错误的参数_id（新增传入测试数据的id）'''
        payload = {"id":self.s1,"roleName":"测试角色β", "remark": "我是描述"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], '测试角色α')

        time.sleep(1)

    def test_createparams_allnull_incorrect(self):
        ''' 错误的参数_allNull'''
        payload = {"roleName":"", "remark": ""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], '测试角色α')

        time.sleep(1)

    def test_editparams_correct(self):
        ''' 正确的参数_all（编辑）'''
        payload = {"id":self.s1,"roleName":"测试角色β", "remark": "我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], '测试角色α')


    def test_editparams_remarkNull_correct(self):
        ''' 正确的参数_remarkNull（编辑）'''
        payload = {"id":self.s1,"roleName":"测试角色β", "remark": "","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], '测试角色α')


    def test_editparams_id_incorrect(self):
        ''' 错误的参数_不存在的Id（编辑）'''
        payload = {"id":9998,"roleName":"测试角色β", "remark": "我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], '测试角色α')

    def test_editparams_idNull_incorrect(self):
        ''' 错误的参数_不存在的Id（编辑）'''
        payload = {"id":"","roleName":"测试角色β", "remark": "我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)

    def test_editparams_roleNameNull_incorrect(self):
        ''' 错误的参数_name为空值'''
        payload = {"id":self.s1,"roleName":"", "remark": "我是描述","opType":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)


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