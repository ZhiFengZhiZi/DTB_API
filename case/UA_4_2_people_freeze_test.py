import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
import time
from db import test_data

class emp_people_freeze(unittest.TestCase):
    ''' 冻结恢复删除登录接口 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        self.base_url = self.emp + "/emp/updateEmpStatus"
        test_data.ua_emp_insert(count=9)
        self.empid1 = test_data.ua_emp_search(value='id', type='α')
        self.empid2 = test_data.ua_emp_search(value='id', type='β')
        test_data.ua_roleemp_insert(empid=self.empid1, roleid=1)
        test_data.ua_roleemp_insert(empid=self.empid2, roleid=1)

        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/emp/updateEmpStatus"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload =  {'username': 'ZHANGHAO1', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)

    def test_people_common(self):
        ''' 正确的参数_正常状态'''

        payload = {"id":self.empid1,"empStatus": 1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_people_dele(self):
        ''' 正确的参数_删除状态'''

        payload = {"id":self.empid1,"empStatus":2}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_people_freeze(self):
        ''' 正确的参数_冻结状态'''

        payload = {"id":self.empid2,"empStatus": 1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)

        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)


    def test_status_wrong_noid(self):
        ''' 错误的参数_不存在的id'''

        payload = {"id":99999999,"empStatus": 1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)

        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_status_wrong_nostatus(self):
        ''' 错误的参数_不存在的status'''

        payload = {"id":self.empid1,"empStatus":5}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)

        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)

    def test_status_wrong_null(self):
        ''' 错误的参数_空的数据'''

        payload = {"id":'',"empStatus":''}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)

        self.assertEqual(self.result['resultObject'], None)
        time.sleep(1)




    def tearDown(self):
        test_data.ua_roleemp_delete(EMP_ID=self.empid1)
        test_data.ua_roleemp_delete(EMP_ID=self.empid2)
        test_data.ua_emp_delete(type='β',id=self.empid1)
        test_data.ua_emp_delete(type='α',id=self.empid2)
        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()