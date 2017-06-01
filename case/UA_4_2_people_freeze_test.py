import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
import time

class emp_people_freeze(unittest.TestCase):
    ''' 冻结恢复删除登录接口 '''

    def setUp(self):
        table_name = "ua_employee"
        data = {'EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
                'EMP_STATUS': '1', 'CELL_PHONE': '123456'}
        data2 = {'EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
                 'EMP_STATUS': '0', 'CELL_PHONE': '123456'}
        sdata = {'EMP_CNAME': '测试账号α'}
        sdata2 = {'EMP_CNAME': '测试账号β'}

        db = DB()
        db.insert(table_name=table_name, table_data=data)
        db.insert(table_name=table_name, table_data=data2)

        self.s1 = db.select(table_value='id', table_name=table_name, table_data=sdata)
        self.s2 = db.select(table_value='id', table_name=table_name, table_data=sdata2)

        db.close()

        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)

    def test_people_common(self):
        ''' 正确的参数_正常状态'''
        self.base_url = urlbase.sit_emp() + "/emp/updateEmpStatus.htm"
        payload = {"id":self.s1,"empStatus": 1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_people_dele(self):
        ''' 正确的参数_删除状态'''
        self.base_url = urlbase.sit_emp() + "/emp/updateEmpStatus.htm"
        payload = {"id":self.s1,"empStatus":2}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'],'操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_people_freeze(self):
        ''' 正确的参数_冻结状态'''
        self.base_url = urlbase.sit_emp() + "/emp/updateEmpStatus.htm"
        payload = {"id":self.s2,"empStatus": 1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['success'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_status_wrong_noid(self):
        ''' 错误的参数_不存在的id'''
        self.base_url = urlbase.sit_emp() + "/emp/updateEmpStatus.htm"
        payload = {"id":99999999,"empStatus": 1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '操作失败!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 1)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_status_wrong_nostatus(self):
        ''' 错误的参数_不存在的status'''
        self.base_url = urlbase.sit_emp() + "/emp/updateEmpStatus.htm"
        payload = {"id":self.s1,"empStatus":5}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '操作失败!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 1)
        self.assertEqual(self.result['success'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_status_wrong_null(self):
        ''' 错误的参数_空的数据'''
        self.base_url = urlbase.sit_emp() + "/emp/updateEmpStatus.htm"
        payload = {"id":'',"empStatus":''}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['message'], '操作失败!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 1)
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