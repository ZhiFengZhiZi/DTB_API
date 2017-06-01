import sys
sys.path.append('../db_fixture')
from db.mysql_db import DB
from common import urlbase
import requests
# create data



# Inster table datas
def init_data():

    table_name = "ua_employee"
    data = {'EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
                 'EMP_STATUS': '1', 'CELL_PHONE': '123456'}
    data2 = {'EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
                  'EMP_STATUS': '0', 'CELL_PHONE': '123456'}
    sdata = {'EMP_CNAME': '测试账号α'}
    sdata2 = {'EMP_CNAME': '测试账号β'}

    db = DB()
    db.insert(table_name=table_name, table_data=data)
    db.insert(table_name=table_name, table_data=data2)

    s1 = db.select(table_value='id', table_name=table_name, table_data=sdata)
    s2 = db.select(table_value='id', table_name=table_name, table_data=sdata2)

    print(s1)
    print(s2)
    db.close()

    base_url_login = urlbase.sit_emp() + "/ajaxLogin"
    base_url = urlbase.sit_emp() + "/emp/getEmpInfoList.htm"
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    ##以x-www-form-urlencoded
    payload = {'username': 'ceshi', 'password': '123456', 'verifyCode': '0000'}
    s = requests.Session()
    r1 = s.post(base_url_login, data=payload, headers=head)

    base_url = urlbase.sit_emp() + "/emp/updateEmpStatus.htm"
    payload = {"ID": s1, "empStatus": 1}
    r2 = s.post(base_url, data=payload)
    result = r2.text
    print(result)

if __name__ == '__main__':
    init_data()
