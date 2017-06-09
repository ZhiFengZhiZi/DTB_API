import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
from db import test_data

class emp_getResList_info(unittest.TestCase):
    ''' 查询资源列表接口 '''

    def setUp(self):


        test_data.ua_res_insert(1)
        test_data.ua_emp_insert(1)
        self.emp=test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.emp,roleid=1)



        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/role/getResList"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_params_correct(self):
        ''' 正确的参数'''
        r2 = self.s.get(self.base_url,)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'][0]['children'][-1]['label'], "测试管理α")

        time.sleep(1)

    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.emp)
        test_data.ua_emp_delete(type='β')
        test_data.ua_res_delete('α')

        print(self.result)


if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()