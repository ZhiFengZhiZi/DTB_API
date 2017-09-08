import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB
from db import test_data

class emp_getResInfo_info(unittest.TestCase):
    '''删除组织架构接口 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        test_data.ua_role_insert(1)
        test_data.ua_emp_insert(1)
        self.empid=test_data.ua_emp_search(value='id',type='β')
        print(self.empid)
        test_data.ua_roleemp_insert(empid=self.empid,roleid=1)
        self.s1=test_data.ua_role_search('id','α')


        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/org/delOrg"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)
        print(r1.text)

    def test_params_incorrect(self):
        ''' 不传参数'''
        r2 = self.s.get(self.base_url)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)

        time.sleep(1)






    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_emp_delete(type='β',id=self.empid)
        test_data.ua_role_delete('α')
        test_data.ua_org_delete(999)
        print(self.result)

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()