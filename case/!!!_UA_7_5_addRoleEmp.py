import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
from db import test_data

class emp_checkRoleName(unittest.TestCase):
    ''' 校验角色名称接口 '''

    def setUp(self):

        table_name = "ua_role"
        table_name2 = "ua_employee"
        data = {'ROLE_CODE':'ROLE01','ROLE_NAME': '测试角色γ', 'PINYIN': 'AERFA','STATUS': '1'}
        data2 = {'EMP_CNAME': '测试账号γ', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
                 'EMP_STATUS': '1', 'CELL_PHONE': '1234567890'}
        data3 = {'EMP_CNAME': '测试账号γ2', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
                 'EMP_STATUS': '1', 'CELL_PHONE': '123456789'}


        test_data.ua_emp_insert(1)
        self.emp = test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.emp,roleid=1)
        print(self.emp)

        db = DB()
        db.insert(table_name=table_name, table_data=data)
        db.insert(table_name=table_name2, table_data=data2)
        db.insert(table_name=table_name2, table_data=data3)
        self.sdata = {'ROLE_NAME': '测试角色γ'}
        self.sdata2 = {'EMP_CNAME': '测试账号γ'}
        self.sdata3 = {'EMP_CNAME': '测试账号γ2'}
        self.s1 = db.select(table_value='id', table_name=table_name, table_data=self.sdata)
        self.empid = db.select(table_value='id', table_name=table_name2, table_data=self.sdata2)
        self.empid2 = db.select(table_value='id', table_name=table_name2, table_data=self.sdata3)

        print("id:"+str(self.s1))
        db.close()

        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/role/addRoleEmp"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        self.s.post(self.base_url_login, data=payload, headers=head)


    def test_correct_oneEmp(self):
        ''' 正确的参数_all(单个emp id)'''
        payload = {"roleId":self.s1,"empIds":self.empid}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'],None)
        time.sleep(1)

    def test_correct_Emps(self):
        ''' 正确的参数_all(多个emp id)'''
        payload = {"roleId": self.s1, "empIds": str(self.empid)+','+str(self.empid2)}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_incorrect_oneEmp(self):
        ''' 错误的参数_all(单个emp id)'''
        payload = {"roleId": self.s1, "empIds": 99989}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_incorrect_Emps(self):
        ''' 错误的参数_all(多个emp id)'''
        payload = {"roleId": self.s1, "empIds": '99989,99988,99987'}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def tearDown(self):


        test_data.ua_roleemp_delete(EMP_ID=self.emp)
        test_data.ua_emp_delete(type='β')

        self.table_name = "ua_role"
        self.table_name2 = "ua_employee"
        self.table_name3 = "ua_role_emp"
        self.ddata = {'ROLE_NAME': '测试角色γ'}
        self.ddata2 = {'EMP_NAME': '测试账号γ'}
        self.ddata3 = {'EMP_NAME': '测试账号γ2'}
        self.ddata4 = {'ROLE_ID': self.s1}
        db = DB()

        db.clear(table_name=self.table_name3, table_data=self.ddata4)
        db.clear(table_name=self.table_name,table_data=self.ddata)
        db.clear(table_name=self.table_name2, table_data=self.ddata2)
        db.clear(table_name=self.table_name2, table_data=self.ddata3)
        db.close()

        print(self.result)


if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()