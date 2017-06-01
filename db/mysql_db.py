# encoding=utf-8
import pymysql.cursors
import os
import configparser as cparser


# ======== Reading db_config.ini setting ===========



# ======== MySql base operating ===================
class DB:

    def __init__(self):

        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + "/db_config.ini"

        cf = cparser.ConfigParser()

        cf.read(file_path)
        host = cf.get("mysqlconf_dev", "host")
        port = cf.get("mysqlconf_dev", "port")
        db = cf.get("mysqlconf_dev", "db_name")
        user = cf.get("mysqlconf_dev", "user")
        password = cf.get("mysqlconf_dev", "password")
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',)
 #                                             cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %s: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name, table_data):
        # real_sql = "truncate table " + table_name + ";"
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        clear_sql = "DELETE from %s where %s = %s; "
        with self.connection.cursor() as cursor:
#            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(clear_sql%(str(table_name),str(key),str(value)))
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    def select(self,table_value,table_name, table_data):

        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        sel_sql = "select %s from %s where %s = %s"
        with self.connection.cursor() as cursor:
            #            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(sel_sql % (str(table_value),str(table_name),str(key),str(value)))
            s=cursor.fetchall()

        return s[0][0]


if __name__ == '__main__':

    db = DB()
    table_name = "yb_category_primary"
    data = {'category_name':'一级类目1'}
#    table_name2 = "sign_guest"
#    data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'event_id':1}
#    db.insert(table_name, data)
    db.clear(table_name,data)

    db.close()
