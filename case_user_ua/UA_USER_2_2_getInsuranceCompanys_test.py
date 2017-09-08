import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db.mysql_db import DB
import time
from db import test_data
class get_InsuranceCompanys(unittest.TestCase):
    ''' 获取保险公司列表 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        self.uauser = urlbase.list()[1]

        self.base_url_login = self.emp + "/login"
        self.base_url = self.uauser+"/clause/getClauseList"
        self.base_url_createTicket = self.emp + '/ticket/createTicket'
        self.base_url_verify = self.uauser+'/verifyAuthenticationTicket'

        self.s = requests.Session()

        test_data.ua_emp_insert(count=1)
        self.empid = test_data.ua_emp_search(value='id', type='β')





    def test_success(self):
        ''' 正常调用'''

        test_data.ua_emp_insert(count=1)


        test_data.ua_roleemp_insert(empid=self.empid, roleid=1)

        head = {'Content-Type': 'application/x-www-form-urlencoded'}

        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}

        self.s.post(self.base_url_login, data=payload, headers=head)

        r1 = self.s.get(self.base_url_createTicket)

        toke = r1.json()['resultObject']
        print(toke)

        payload2 ={'ticket':toke}
        self.s2 = requests.Session()
        self.s2.get(self.base_url_verify,params=payload2)



        r2 = self.s2.post(self.base_url)
        self.result = r2.json()

        self.assertEqual(self.result['result'], True)
        self.assertIsNotNone(self.result['resultObject'])



    def test_insuccess(self):
        '''错误调用（直接调用）'''


        r2 = self.s.get(self.base_url)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        self.s1 = 'aaa'




    def tearDown(self):
        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_emp_delete(type='β', id=self.empid)









if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()