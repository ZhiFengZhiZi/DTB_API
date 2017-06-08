import unittest
import requests
import os, sys
from common import urlbase
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db.mysql_db import DB


class emp_checkRoleName(unittest.TestCase):
    ''' 校验角色名称接口 '''

    def setUp(self):

        table_name = "ua_role"
        table_name2 = "ua_employee"
        table_name3 = "ua_role_emp"
        data = {'ROLE_CODE':'ROLE01','ROLE_NAME': '测试角色α', 'PINYIN': 'AERFA','STATUS': '1'}
        data2 = {'EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                 'EMP_STATUS': '1', 'CELL_PHONE': '123456'}

        db = DB()
        db.insert(table_name=table_name, table_data=data)
        db.insert(table_name=table_name2, table_data=data2)
        self.sdata = {'ROLE_NAME': '测试角色α'}
        self.sdata2 = {'EMP_CNAME': '测试账号α'}
        self.roleid = db.select(table_value='id', table_name=table_name, table_data=self.sdata)
        self.empid = db.select(table_value='id', table_name=table_name2, table_data=self.sdata2)
        data3 = {'EMP_ID':self.empid,'ROLE_ID':self.roleid,'STATUS':1,'UPDATE_TIME':'2017-05-26 13:27:50'}
        db.insert(table_name=table_name3, table_data=data3)

        db.close()
        print(self.roleid)
        self.base_url_login = urlbase.sit_emp() + "/login"
        self.base_url = urlbase.sit_emp() + "/role/getRoleEmpList.htm?roleId=1"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)


    def test_ExistingCheck_id(self):
        '''存在check关系的角色id'''
        payload = {"roleId":121}
#        r2 = self.s.get(self.base_url, params=payload)
        r2 = self.s.get(self.base_url)

#        self.result = r2.json()
        self.text = r2.text()
#        self.code = r2.status_code()
#        self.assertEqual(self.result['result'], True)
#        s= self.result['resultObject']
#        j=0
#        for i in s:
#            j = j+1

 #           if i["name"] == self.sdata2["EMP_CNAME"]:
  #              self.checked = s[j]["checked"]
  #          else:
  #              self.checked = "不存在的人"
  #      self.assertEqual(self.checked,True)


    def tearDown(self):

        self.table_name = "ua_role"
        self.table_name2 = "ua_employee"
        self.table_name3 = "ua_role_emp"
        self.table_name4 = "ua_org_emp"
        self.data = {'ROLE_NAME': '测试角色α'}
        self.data2 = {'EMP_CNAME': '测试账号α'}
        self.data3 = {'EMP_ID':self.empid}
        self.data4 = {'EMP_ID': self.empid}
        db = DB()
        db.clear(table_name=self.table_name3, table_data=self.data3)
        db.clear(table_name=self.table_name4, table_data=self.data4)
        db.clear(table_name=self.table_name,table_data=self.data)
        db.clear(table_name=self.table_name2, table_data=self.data2)

        db.close()



        print(self.text)



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据

    unittest.main()