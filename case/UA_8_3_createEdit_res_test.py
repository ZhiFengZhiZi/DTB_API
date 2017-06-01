import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB


class emp_createEdit_res(unittest.TestCase):
    ''' 创建编辑资源接口 '''

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
        self.base_url = urlbase.sit_emp() + "/res/addResInfo.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_params_create_correct(self):
        ''' 正确的参数_新增'''
        payload = {"resName":"测试管理β","parent":self.s1,"type":0,"resValue":"/123/456","icon":"","orderNum":"","remark":"",
                   "resUrlList":"","opType":0}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'],None)

        time.sleep(1)

    def test_params_edit_correct(self):
        ''' 正确的参数_编辑'''
        payload = {"resId":self.s1,"resName":"测试管理β","parent":"","type":0,"resValue":"/123/456","icon":"","orderNum":"","remark":"",
                   "resUrlList":"","opType":1}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'],None)
        table_name = "ua_resource"
        data = {'id': self.s1}
        db = DB()
        self.edit_name = db.select(table_value='RES_NAME', table_name=table_name, table_data=data)
        db.close()
        self.assertEqual(self.edit_name, "测试管理β")

        time.sleep(1)


    def tearDown(self):


        self.table_name = "ua_resource"
        self.data = {'RES_NAME': '测试管理α'}
        self.data2 = {'RES_NAME': '测试管理β'}
        db = DB()
        db.clear(table_name=self.table_name,table_data=self.data)
        db.clear(table_name=self.table_name, table_data=self.data2)
        db.close()

        print(self.result)

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()