import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
import time

class emp_people_create(unittest.TestCase):
    ''' 创建编辑人员接口 '''

    def setUp(self):
        table_name = "ua_employee"
        data = {'EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
                'EMP_STATUS': '1', 'CELL_PHONE': '123456'}
        sdata = {'EMP_CNAME': '测试账号α'}

        db = DB()
        db.insert(table_name=table_name, table_data=data)

        self.s1 = db.select(table_value='id', table_name=table_name, table_data=sdata)
        print("id:"+str(self.s1))
        db.close()

        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/emp/saveEmployeeInfo.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)

    def test_createparam_correct(self):
        ''' 正确的参数_新增_all'''
        payload = {"empName":"ZHANGHAO2","empCname":"测试账号β","cellphone":"123456","email":"123@qq.com","empNo":"009","opType":"0"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_editparam_correct(self):
        ''' 正确的参数_修改姓名、账号、电话、邮箱_all'''
        payload = {"id":self.s1,"empName":"ZHANGHAO2","empCname":"测试账号β","cellphone":"123456","email":"123@qq.com","empNo":"009","opType":"1"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_createparam_null(self):
        '''错误的参数_空值(opType=0 新增)'''
        payload = {"id":"","empName":"","empCname":"","cellphone":"","email":"1","empNo":"","opType":"0"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '缺少必要的参数，请重新确认!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_editparam_null(self):
        '''错误的参数_空值(opType=1 编辑)'''
        payload = {"id":"","empName":"","empCname":"","cellphone":"","email":"1","empNo":"","opType":"1"}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '缺少必要的参数，请重新确认!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def tearDown(self):

        self.table_name = "ua_employee"
        self.data = {'EMP_CNAME': '测试账号α'}
        self.data2 = {'EMP_CNAME': '测试账号β'}

        db = DB()
        db.clear(table_name=self.table_name,table_data=self.data)
        db.clear(table_name=self.table_name, table_data=self.data2)

        db.close()

        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()