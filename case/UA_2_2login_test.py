import unittest
import requests
import os, sys, time
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db.mysql_db import DB
from db import test_data

class emp_login(unittest.TestCase):
    ''' 后台登录接口 '''

    def setUp(self):

        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        ##获取当前时间
        test_data.ua_emp_insert(2)
        self.empid=test_data.ua_emp_search(value="id",type='β')
        self.empid2 = test_data.ua_emp_search(value="id",type='α')
        test_data.ua_roleemp_insert(empid=self.empid,roleid=1)
        self.base_url = urlbase.sit_emp() + "/login"
        self.base_url_login = urlbase.sit_emp() + "/login"



    def test_login_success(self):
        ''' 正确的参数 默认不修改密码'''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'ZHANGHAO2','password':'234567','verifyCode':'0000'}
        r = requests.post(self.base_url,data=payload,headers=head)
        self.result = r.json()

        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['username'], 'ZHANGHAO2')
        self.assertEqual(self.result['changePwd'],False)




    def test_chagePWD_login_success(self):
        ''' 正确的参数,默认应该修改密码 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'ZHANGHAO1','password':'123456','verifyCode':'0000'}
        r = requests.post(self.base_url,data=payload,headers=head)
        self.result = r.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['username'], 'ZHANGHAO1')
        self.assertEqual(self.result['changePwd'], True)
        self.assertTrue(self.result['resultObject'], not None)

    def test_login_pwd_wrong(self):
        ''' 错误的密码 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'ZHANGHAO2','password':'654321','verifyCode':'0000'}
        r = requests.post(self.base_url,data=payload,headers=head)
        self.result = r.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)


    def test_login_loginname_wrong(self):
        ''' 错误的账号 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'aaaaa','password':'123456','verifyCode':'0000'}
        r = requests.post(self.base_url,data=payload,headers=head)
        self.result = r.json()


        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)

    def test_login_code_wrong(self):
        ''' 错误的验证码 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'ZHANGHAO2','password':'234567','verifyCode':'1111'}
        r = requests.post(self.base_url,data=payload,headers=head)
        self.result = r.json()


        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)

    def test_login_null(self):
        ''' 全部都为空值 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'','password':'','verifyCode':''}
        r = requests.post(self.base_url,data=payload,headers=head)
        self.result = r.json()


        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)


    def test_login_null2(self):
        ''' 除验证码外都为空值 '''
        head = {'Content-Type':'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username':'','password':'','verifyCode':'0000'}
        r = requests.post(self.base_url,data=payload,headers=head)
        self.result = r.json()


        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['success'], False)

    def tearDown(self):

        self.table_name = "ua_employee"
        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_roleemp_delete(EMP_ID=self.empid2)
        self.data = {'EMP_NAME': 'ZHANGHAO1'}
        self.data2 = {'EMP_NAME': 'ZHANGHAO2'}
        db = DB()
        db.clear(table_name=self.table_name, table_data=self.data)
        db.clear(table_name=self.table_name,table_data=self.data2)

        db.close()



        print(self.result)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()