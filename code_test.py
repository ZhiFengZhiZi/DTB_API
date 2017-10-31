import unittest
import requests
import os, sys
import json
from common import urlbase
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data
from db import test_data
import os
import sys
class eims_login(object):
    ''' 后台登录接口 '''



    def test_catch_code_success(self):
        #print(os.path.abspath(os.path))

        print(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据
    eims_login().test_catch_code_success()
