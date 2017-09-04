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
    ''' 添加编辑组织架构接口 '''

    def setUp(self):

        test_data.ua_role_insert(1)
        test_data.ua_emp_insert(1)
        self.emp=test_data.ua_emp_search(value='id',type='β')
        print(self.emp)
        test_data.ua_roleemp_insert(empid=self.emp,roleid=1)
        self.s1=test_data.ua_role_search('id','α')



        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/org/saveOrg"
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

    def test_params_correct(self):
        ''' 正常传各类参数(新增)'''
        payload = {"id":999,'parentId':3,'orgName':"系统研发测试组织",'orgRemark':'描述','opType':'0'}#id 3 是系统研发中心
        r2 = self.s.get(self.base_url,params = payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], True)
        #self.assertEqual(self.result['resultObject']['id'],3)
        time.sleep(1)

    def test_no_parentID(self):
        '''不传parentid '''
        payload = {"id":999,'orgName':"系统研发测试组织",'orgRemark':'描述','opType':'0'}#id 3 是系统研发中心
        r2 = self.s.get(self.base_url,params = payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        #self.assertEqual(self.result['resultObject']['id'],3)
        time.sleep(1)

    def test_no_opType(self):
        ''' 不传opType'''
        payload = {"id":999,'parentId':3,'orgName':"系统研发测试组织",'orgRemark':'描述'}#id 3 是系统研发中心
        r2 = self.s.get(self.base_url,params = payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        #self.assertEqual(self.result['resultObject']['id'],3)
        time.sleep(1)


    def test_duplicate_id(self):
        ''' 重复的id'''
        payload = {"id":3,'parentId':3,'orgName':"系统研发测试组织",'orgRemark':'描述'}#id 3 是系统研发中心
        r2 = self.s.get(self.base_url,params = payload)
        self.result = r2.json()
        self.assertEqual(self.result['result'], False)
        #self.assertEqual(self.result['resultObject']['id'],3)
        time.sleep(1)




    def tearDown(self):

        test_data.ua_roleemp_delete(EMP_ID=self.emp)
        test_data.ua_emp_delete(type='β')
        test_data.ua_role_delete('α')
        test_data.ua_org_delete(999)
        print(self.result)

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()