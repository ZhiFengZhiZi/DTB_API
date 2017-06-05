import unittest
import requests
import os, sys
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db.mysql_db import DB
import time

class get_getEmpResource(unittest.TestCase):
    ''' 欢迎页获取用户权限接口 '''

    def setUp(self):
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        ##获取当前时间
        db = DB()

        self.base_url = urlbase.sit_emp()+"/auth/getEmpResource.htm"
        self.base_url_login = urlbase.sit_emp() + "/login"
        self.table_name = "ua_employee"
        self.table_name2 = "ua_role_emp"
        self.data = {'EMP_CNAME': '测试账号α','EMP_NAME':'ZHANGHAO1','PASSWORD':'e10adc3949ba59abbe56e057f20f883e',
                     'EMP_STATUS':'1','CELL_PHONE':'123456','UPDATE_TIME':nowtime}
        db.insert(table_name=self.table_name, table_data=self.data)

        sdata = {'EMP_CNAME': '测试账号α'}
        self.empid = db.select(table_value='id', table_name=self.table_name, table_data=sdata)

        self.data2 = {'EMP_ID': self.empid, 'ROLE_ID': 1, 'STATUS':'1','UPDATE_TIME': nowtime}
        db.insert(table_name=self.table_name2,table_data=self.data2)

        db.close()
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO1', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()


        r1 = self.s.post(self.base_url_login, data=payload, headers=head).json()
        self.token = r1["resultObject"]
        print(self.token)



    def test_token_success(self):
        ''' 正确的token'''

        payload = {"token":self.token}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject']['systemId'], 1)


    def test_token_wrong(self):
        ''' 错误的token'''

        payload = {"token":123456}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()

        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'],None)




    def tearDown(self):



        self.data = {'EMP_NAME': 'ZHANGHAO1'}
        self.data2 = {'EMP_ID': self.empid}
        db = DB()
        db.clear(table_name=self.table_name2, table_data=self.data2)
        db.clear(table_name=self.table_name,table_data=self.data)

        db.close()


        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()