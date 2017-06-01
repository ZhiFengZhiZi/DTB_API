import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB


class emp_getResInfo_info(unittest.TestCase):
    ''' 查询资源信息接口 '''

    def setUp(self):

        table_name = "ua_resource"
        data = {'RES_NAME':'测试管理α','SYS_ID': 1, 'RES_TYPE': 0,'RES_LEVEL': '1'}

        db = DB()
        db.insert(table_name=table_name, table_data=data)
        sdata = {'RES_NAME': '测试管理α'}
        self.s1 = db.select(table_value='id', table_name=table_name, table_data=sdata)
        print("id:"+str(self.s1))
        db.close()

        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/res/getResInfo.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_params_correct(self):
        ''' 正确的参数_id'''
        payload = {"resId":self.s1}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
 #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject']['resName'], "测试管理α")

        time.sleep(1)

    def test_params_incorrect(self):
        ''' 错误的参数_不存在的id'''
        payload = {"resId": 99898}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)

    def test_params_null(self):
        ''' 错误的参数_空的id'''
        payload = {"resId": ""}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)


    def tearDown(self):


        self.table_name = "ua_resource"
        self.data = {'RES_NAME': '测试管理α'}
        db = DB()
        db.clear(table_name=self.table_name,table_data=self.data)
        db.close()

        print(self.result)

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()