import unittest
import requests
import os, sys
import json
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db import test_data

class eims_login(object):
    ''' 后台登录接口 '''



    def test_catch_code_success(self):
        ''' 正确的参数 '''



        test_data.ua_emp_insert(count=1)

        self.empid=test_data.ua_emp_search(value="id",type='β')


        print(self.empid)

        test_data.ua_roleemp_insert(empid=self.empid,roleid=1)

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据
    eims_login().test_catch_code_success()
