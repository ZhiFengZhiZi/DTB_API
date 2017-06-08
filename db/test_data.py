import sys,time
sys.path.append('../db_fixture')
from db.mysql_db import DB
from common import urlbase



# Inster table datas
def ua_emp_insert(count):
    table = 'ua_employee'
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    try:


        if  count==1:
            table_name = table
            emp = {'EMP_NO':'99991','EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                'EMP_STATUS': '1', 'CELL_PHONE': '9898123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.close()

        elif  count==2:

            table_name = table
            emp = {'EMP_NO':'99991','EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2', 'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
               'EMP_STATUS': '1', 'CELL_PHONE': '9898123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}



            emp2 = {'EMP_NO':'99992','EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1', 'PASSWORD': 'e10adc3949ba59abbe56e057f20f883e',
           'EMP_STATUS': '1', 'CELL_PHONE': '1010123456','UPDATE_TIME':nowtime,'EMAIL':'JIEKOUCESHI2@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.insert(table_name=table_name, table_data=emp2)
            db.close()

        elif count == 9:
            table_name = table
            emp = {'EMP_NO': '99991', 'EMP_CNAME': '测试账号β', 'EMP_NAME': 'ZHANGHAO2',
                   'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                   'EMP_STATUS': '0', 'CELL_PHONE': '9898123456', 'UPDATE_TIME': nowtime,'EMAIL':'JIEKOUCESHI@ZHIFENG.COM'}

            emp2 = {'EMP_NO': '99992', 'EMP_CNAME': '测试账号α', 'EMP_NAME': 'ZHANGHAO1',
                    'PASSWORD': '508df4cb2f4d8f80519256258cfb975f',
                    'EMP_STATUS': '1', 'CELL_PHONE': '1010123456', 'UPDATE_TIME': nowtime,'EMAIL':'JIEKOUCESHI2@ZHIFENG.COM'}

            db = DB()
            db.insert(table_name=table_name, table_data=emp)
            db.insert(table_name=table_name, table_data=emp2)
            db.close()
    except Exception as err:
        return  err
    finally:
        return "good"

def ua_emp_search(value,type):
    semp = {'EMP_CNAME': '测试账号α'}
    semp2 = {'EMP_CNAME': '测试账号β'}
    table_name = "ua_employee"


    if   type=='α':
        db = DB()

        s = db.select(table_value=value, table_name=table_name, table_data=semp)
        db.close()
    elif type == 'β':
        db = DB()

        s = db.select(table_value=value, table_name=table_name, table_data=semp2)
        db.close()
    return s

def ua_emp_delete(type):
    table_name = "ua_employee"
    data = {'EMP_CNAME': '测试账号α'}
    data2 = {'EMP_CNAME': '测试账号β'}

    if type == 'α':
        db = DB()
        db.clear(table_name=table_name,table_data=data)
        db.close()

    elif type == 'β':
        db = DB()
        db.clear(table_name=table_name, table_data=data2)
        db.close()

def ua_role_insert(count):
    table_name = "ua_role"
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if count==1 :
        role = {'ROLE_CODE': 'ROLE01', 'ROLE_NAME': '测试角色α', 'PINYIN': 'AERFA', 'STATUS': '1','UPDATE_TIME':nowtime}
        db = DB()
        db.insert(table_name=table_name, table_data=role)
        db.close()


    elif count==2 :
        role = {'ROLE_CODE': 'ROLE01', 'ROLE_NAME': '测试角色α', 'PINYIN': 'AERFA',
                'STATUS': '1','UPDATE_TIME':nowtime}
        role2 = {'ROLE_CODE': 'ROLE02', 'ROLE_NAME': '测试角色β', 'PINYIN': 'BETA',
                 'STATUS': '1','UPDATE_TIME':nowtime}
        db = DB()
        db.insert(table_name=table_name, table_data=role)
        db.insert(table_name=table_name, table_data=role2)
        db.close()

def ua_role_search(value, type):
    semp = {'ROLE_NAME': '测试角色α'}
    semp2 = {'ROLE_NAME': '测试角色β'}
    table_name = "ua_role"

    if type == 'α':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp)
            db.close()
    if type == 'β':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp2)
            db.close()

    return s

def ua_role_delete(type):
    data = {'ROLE_NAME': '测试角色α'}
    data2 = {'ROLE_NAME': '测试角色β'}
    table_name = "ua_role"

    if type == 'α':
        db = DB()
        db.clear(table_name=table_name,table_data=data)
        db.close()

    elif type == 'β':
        db = DB()
        db.clear(table_name=table_name, table_data=data2)
        db.close()

def ua_res_insert(count):
    table_name = "ua_resource"

    if count == 1:
            role = {'RES_NAME':'测试管理α','SYS_ID': 1, 'RES_TYPE': 0,'RES_LEVEL': '1'}
            db = DB()
            db.insert(table_name=table_name, table_data=role)
            db.close()

    if count == 2:
            role = {'RES_NAME':'测试管理α','SYS_ID': 1, 'RES_TYPE': 0,'RES_LEVEL': '1'}
            role2 = {'RES_NAME':'测试管理β','SYS_ID': 1, 'RES_TYPE': 0,'RES_LEVEL': '1'}
            db = DB()
            db.insert(table_name=table_name, table_data=role)
            db.insert(table_name=table_name, table_data=role2)
            db.close()

def ua_res_search(value, type):
        semp = {'RES_NAME': '测试管理α'}
        semp2 = {'RES_NAME': '测试管理β'}
        table_name = "ua_resource"

        if type == 'α':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp)
            db.close()
        if type == 'β':
            db = DB()

            s = db.select(table_value=value, table_name=table_name, table_data=semp2)
            db.close()

        return s

def ua_res_delete(type):
    data = {'RES_NAME': '测试管理α'}

    data2 = {'RES_NAME': '测试管理β'}
    table_name = "ua_resource"

    if type == 'α':
        db = DB()
        db.clear(table_name=table_name,table_data=data)
        db.close()

    elif type == 'β':
        db = DB()
        db.clear(table_name=table_name, table_data=data2)
        db.close()

def ua_roleemp_insert(empid,roleid):
    table_name = "ua_role_emp"
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    data = {'EMP_ID':empid,'ROLE_ID':roleid,'STATUS':1,'UPDATE_TIME':nowtime}
    db = DB()
    db.insert(table_name=table_name, table_data=data)
    db.close()

def ua_roleemp_delete(EMP_ID):
    data = {'EMP_ID':EMP_ID}

    table_name = "ua_role_emp"

    db = DB()
    db.clear(table_name=table_name, table_data=data)
    db.close()


if __name__ == '__main__':

    ua_role_insert(count=2)
    s=ua_role_search(value='ROLE_NAME', type='β')
    print(s)