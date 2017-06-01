import unittest
import requests
import os, sys
import json
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db.mysql_db import DB

class eims_login(object):
    ''' 后台登录接口 '''



    def test_catch_code_success(self):
        ''' 正确的参数 '''


        self.base_url_login = urlbase.sit_emp() + "/ajaxLogin"
        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        ##以x-www-form-urlencoded
        payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
        self.s = requests.Session()
        r1 = self.s.post(self.base_url_login, data=payload, headers=head)

        self.base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
        payload = {"empCname":"测试账号α"}
        r2 = self.s.get(self.base_url, params=payload)
        self.result = r2.json()
        print("我是结果+" + str(self.result))



if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据
    eims_login().test_catch_code_success()
