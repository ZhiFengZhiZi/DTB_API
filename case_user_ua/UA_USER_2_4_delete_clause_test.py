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
class delete_Clause(unittest.TestCase):
    ''' 删除条款 '''

    def setUp(self):


        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.UaUser()+"/clause/delClause"
        self.base_url_createTicket = urlbase.sit_emp() + '/ticket/createTicket'
        self.base_url_verify = urlbase.sit_UaUser()+'/verifyAuthenticationTicket'

        test_data.ua_emp_insert(count=1)

        self.s1 = test_data.ua_emp_search(value='id', type='β')
        test_data.ua_roleemp_insert(empid=self.s1, roleid=1)

        head = {'Content-Type': 'application/x-www-form-urlencoded'}

        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        self.s.post(self.base_url_login, data=payload, headers=head)

        r1 = self.s.get(self.base_url_createTicket)

        toke = r1.json()['resultObject']
        print(toke)

        payload2 ={'ticket':toke}
        self.s2 = requests.Session()
        self.s2.get(self.base_url_verify,params=payload2)
        test_data.dtb_clause_inser(count=1)
        self.cid = test_data.dtb_clause_search(value='id',type='α')
        print(self.cid)



    def test_id_success(self):
        ''' 正常的id'''


        payload = {"id":self.cid[0][0] }
        r2 = self.s2.post(self.base_url,data=payload)
        self.result = r2.json()
        self.data22 = str(test_data.dtb_clause_search(value='*', type='α'))
        print(self.data22)
        self.assertEqual(self.result['result'], True)


        self.assertEqual(self.data22,'()')



    def test_name_success(self):
        '''不存在的id参数'''

        payload = {"id":'998989' }
        r2 = self.s2.post(self.base_url,data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)


    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.s1)
        test_data.ua_emp_delete(type='β', id=self.s1)
        test_data.dtb_clause_delete(type='α')

        print(self.result)







if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()