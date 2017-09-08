import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
from db import test_data

class emp_login(unittest.TestCase):
    ''' 人员手机号查重接口 '''

    def setUp(self):


        test_data.ua_emp_insert(count=2)
        self.emp = urlbase.list()[0]
        self.empid1 = test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.empid1, roleid=1)
        test_data.ua_role_insert(1)



        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/role/getRoleInfoList"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_params_correct(self):
        ''' 正确的参数_all'''
        payload = {"roleName":"测试角色α","pageSize":"10","starts":"1"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
 #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], "测试角色α")

        time.sleep(1)


    def test_correct_rolename(self):
        ''' 正确的参数_单独名称参数'''

        payload = {"roleName":"测试角色α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
#        self.assertEqual(self.result['message'],'缺少必要的参数，请重新确认!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], "测试角色α")
        time.sleep(1)

    def test_part_rolename(self):
        ''' 正确的参数_不完全匹配的名称参数'''

        payload = {"roleName": "α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], "测试角色α")

        time.sleep(1)

    def test_params_correct_allnull(self):
        ''' 正确的参数_allnull'''
        payload = {"roleName": None,"pageSize":None,"starts":None}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        #       self.assertEqual(self.result['message'], '操作成功!')
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['roleName'], "测试角色α")
        time.sleep(1)

    def test_params_pagesize2(self):
        ''' 测试的参数_一页2条数据'''
        payload = {"pageSize":2}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(len(self.result['resultObject']),2)
        time.sleep(1)


    def test_incorrect_rolename(self):
        ''' 错误的参数_错误的名称参数'''

        payload = {"roleName": "β"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)

        time.sleep(1)


    def test_incorrect_starts(self):
        ''' 错误的参数_不存在的分页参数'''

        payload = {"starts": "99999999"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)

        time.sleep(1)



    def tearDown(self):
        self.empid2 = test_data.ua_emp_search(value='id', type='α')
        test_data.ua_roleemp_delete(EMP_ID=self.empid1)
        test_data.ua_emp_delete(type='β',id=self.empid1)
        test_data.ua_emp_delete(type='α',id=self.empid2)
        test_data.ua_role_delete('α')


        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()