import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db import test_data


class emp_createEdit_res(unittest.TestCase):
    ''' 创建编辑资源接口 '''

    def setUp(self):
        self.emp = urlbase.list()[0]
        test_data.ua_res_insert(1)
        test_data.ua_emp_insert(1)
        self.empid=test_data.ua_emp_search(value='id',type='β')
        test_data.ua_roleemp_insert(empid=self.empid,roleid=1)
        self.s1=test_data.ua_res_search('id','α')


        self.base_url_login = self.emp + "/login"
        self.base_url = self.emp + "/res/addResInfo"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ZHANGHAO2', 'password': '234567', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)
        print(r1.json())

    def test_params_create_correct(self):
        ''' 正确的参数_新增'''
        payload = {'resSysId':'1',"resName":"测试管理β","parentId":"","resValue":"/123/456","description":"","resourceUrls":"","opType":0}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'],None)
        self.resid2 = test_data.ua_res_search('id', type='β')
        test_data.ua_resurls_delete(self.resid2)
        self.resid1 = test_data.ua_res_search('id', type='α')
        test_data.ua_resurls_delete(self.resid1)
        test_data.ua_resauth_delete(res_id=self.resid1)
        time.sleep(1)

    def test_params_edit_correct(self):
        ''' 正确的参数_编辑'''
        payload = {'id':self.s1,'resSysId':'1',"resName":"测试管理β","parentId":"","resValue":"/123/456","description":"",
                   "resourceUrls":"","opType":1}
        r2 = self.s.post(self.base_url, data=payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'],None)
        self.edit_name =test_data.ua_res_search(self.s1,type='id')
        self.assertEqual(self.edit_name, "测试管理β")
        self.resid2 = test_data.ua_res_search(value='id', type='β')
        test_data.ua_resurls_delete(res_id=self.resid2)
        test_data.ua_resauth_delete(res_id=self.resid2)
        time.sleep(1)


    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.empid)
        test_data.ua_emp_delete(type='β',id=self.empid)


        test_data.ua_res_delete('α')
        test_data.ua_res_delete('β')
        print(self.result)

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()