import warnings
import configparser 
import os
#import sys
#os.getpwd()  
cf = configparser.ConfigParser()  
cf.readfp(open('/home/hughli/scripts/python/Weather-mastersetting.ini'))  
warnings.filterwarnings("ignore")

def main():    
    o = input("想更改配置文件的哪部分内容：1.数据库db 2.客户端client 3.MySql数据库mysqldb 4.数据库表sqltablename 5.退出程序：")
    if o == "1":
        p = input("想更改配置文件db的哪部分内容：1.地址 2.端口 3.用户名 4.密码 5.路径：")
        if p == "1":
            dbs = cf.get("db","db_host")
            print(dbs)
            q=input("要更改吗:1是 2不")
            dbhost(q,dbs)
        elif p == "2":
            dbs = cf.get("db","db_port")
            print(dbs)
            q=input("要更改吗:1是 2不")
            dbport(q,dbs)
        elif p == "3":
            dbs = cf.get("db","db_user")
            print(dbs)
            q=input("要更改吗:1是 2不")
            dbuser(q,dbs)
        elif p == "4":
            dbs = cf.get("db","db_pass")
            print(dbs)
            q=input("要更改吗:1是 2不")
            dbpass(q,dbs)
        elif p == "5":
            dbs = cf.get("db","db_path")
            print(dbs)
            q=input("要更改吗:1是 2不")
            dbpath(q,dbs)
        else:
            print("返回主菜单")
            main()
    elif o == "2":
        p = input("想更改配置文件client的哪部分内容：1.下载地址：")
        if p == "1":
            cls = cf.get("client","cl_dlpath")
            print(cls)
            q=input("要更改吗:1是 2不")
            clpath(q,cls)  
        else:
            print("返回主菜单")
            main()
    elif o == "3":
        p = input("想更改配置文件mysqldb的哪部分内容：1.地址 2.用户名 3.密码 4数据库名：")
        if p == "1":
            sqs = cf.get("mysqldb","sqldb_hostaddr")
            print(sqs)
            q=input("要更改吗:1是 2不")
            sqshost(q,sqs) 
        elif p == "2":
            sqs = cf.get("mysqldb","sqldb_user")
            print(sqs)
            q=input("要更改吗:1是 2不")
            sqsuser(q,sqs) 
        elif p == "3":
            sqs = cf.get("mysqldb","sqldb_pwd")
            print(sqs)
            q=input("要更改吗:1是 2不")
            sqspwd(q,sqs) 
        elif p == "4":
            sqs = cf.get("mysqldb","sqldb_db")
            print(sqs)
            q=input("要更改吗:1是 2不")
            sqsdb(q,sqs) 
        else:
            print("返回主菜单")
            main()
    elif o == "4":
        p = input("想更改配置文件表的哪部分内容：1.表名：")
        if p == "1":
            tbs = cf.get("table","tb_name")
            print(tbs)
            q=input("要更改吗:1是 2不")
            tbstbn(q,tbs)  
        else:
            print("返回主菜单")
            main()        
    elif o == "5":
        exit()
    else:
        print("请输入正确选项:")
        main()

def dbhost(q,dbs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("db", "db_host", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新地址为:" + r)
        main()
    elif q == "2":
        print("地址仍旧为:" + dbs)
        main()
       
def dbport(q,dbs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("db", "db_port", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新端口为:" + r)
        main()
    elif q == "2":
        print("端口仍旧为:" + dbs)
        main()        

def dbuser(q,dbs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("db", "db_user", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新用户名为:" + r)
        main()
    elif q == "2":
        print("用户名仍旧为:" + dbs)
        main()        
        
def dbpass(q,dbs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("db", "db_pass", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新密码为:" + r)
        main()
    elif q == "2":
        print("密码仍旧为:" + dbs)
        main()        
        
def dbpath(q,dbs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("db", "db_path", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新路径为:" + r)
        main()
    elif q == "2":
        print("路径仍旧为:" + dbs)
        main()        

def clpath(q,cls):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("cl", "cl_dlpath", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新下载路径为:" + r)
        main()
    elif q == "2":
        print("下载路径仍旧为:" + cls)
        main()                 
        
       
def sqshost(q,sqs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("mysqldb", "sqldb_hostaddr", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新地址为:" + r)
        main()
    elif q == "2":
        print("地址仍旧为:" + sqs)
        main()        

def sqsuser(q,sqs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("mysqldb", "sqldb_user", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新用户名为:" + r)
        main()
    elif q == "2":
        print("用户名仍旧为:" + sqs)
        main()  

def sqspwd(q,sqs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("mysqldb", "sqldb_pwd", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新密码为:" + r)
        main()
    elif q == "2":
        print("密码仍旧为:" + sqs)
        main()  

def sqsdb(q,sqs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("mysqldb", "sqldb_db", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新数据库名为:" + r)
        main()
    elif q == "2":
        print("数据库名仍旧为:" + sqs)
        main()          
        
def tbstbn(q,sqs):
    if q == "1":
        r = input("输入想要更改的内容:") 
        cf.set("table", "tb_name", r)
        cf.write(open('/home/hughli/scripts/python/Weather-mastersetting.ini', "w"))
        print("新表名为:" + r)
        main()
    elif q == "2":
        print("表名仍旧为:" + sqs)
        main()          
        
               
if __name__ == "__main__":
    main()
