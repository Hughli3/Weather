
import os
import time
#import io
#import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer)
import configparser
#import mysql.connector
import pymysql
from ftplib import FTP 

#from os.path import join, getsize   
os.chdir('/Users/hughli/Documents/学习/共享/OneDrive/python/气象')
timeout = 300                                               
cf = configparser.ConfigParser()
cf.read("setting.ini")

def information(): 
    db_host = cf.get("db", "db_host")
    db_user = cf.get("db", "db_user")
    db_pass = cf.get("db", "db_pass")
    db_path = cf.get("db","db_path")
    hostadd= db_host                     
    username=db_user
    password=db_pass                      
    path=db_path                 
    ftpconnect(hostadd,username,password,path)          
    return hostadd, username, password, path
 
def ftpconnect(hostadd,username,password,path):
    db_port = cf.getint("db", "db_port")
    ftp = FTP()
    ftp.encoding = 'UTF-8'
    print ('开始连接到 %s' %(hostadd))
    ftp.connect(hostadd, db_port)  
    print ('成功连接到 %s' %(hostadd))  
    print ('开始登录到 %s' %(hostadd))                               
    ftp.login(username, password)  
    print ('成功登录到 %s' %(hostadd))                                  
    ftp.cwd(path)  
    print(ftp.getwelcome())
#    ftp.dir()
    lista = ftp.nlst()                                       
    name_size_list = []                                     
    ftp.dir("", name_size_list.append)                     
    i=0
    filesizembtt = 0                                        
    for name in lista: 
            name_size_list=name_size_list[1:]
            filesize = name_size_list[0].split()[4:5]
            filename = (name_size_list[0].split()[-1])
            filesizemb = int(filesize[0])
            filesizembtt += filesizemb                      
            print("文件名称:>>>     " + filename + "      文件大小:>>>     " 
                  + str("%.4f" %(filesizemb/(1024*1024))) + "MB")
            i+=1
    print("")
    print("")
    print("###########################################################")
    print("总文件数量:>>>>>>>>>>       " + str(i))
    print("总文件大小:>>>>>>>>>>       " + \
          str("%.4f" %(filesizembtt/(1024*1024))) + "MB")
    print("###########################################################")
    sqldb_hostaddr = cf.get("mysqldb", "sqldb_hostaddr") 
    sqldb_user = cf.get("mysqldb", "sqldb_user") 
    sqldb_pwd = cf.get("mysqldb", "sqldb_pwd") 
    sqldb_db = cf.get("mysqldb", "sqldb_db") 
    db = pymysql.connect(host=sqldb_hostaddr,user=sqldb_user,password=\
    sqldb_pwd,db=sqldb_db,charset="utf8mb4")
    table_name = cf.get("table","tb_name")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    createTab = """CREATE TABLE """ + table_name + """(
        id INT NOT NULL AUTO_INCREMENT UNIQUE KEY,
        NAME VARCHAR(100) NOT NULL,
        FILENAME VARCHAR(100) NOT NULL PRIMARY KEY,
        SIZE BIGINT(255) NOT NULL,
        CREATE_DATE VARCHAR(20) NOT NULL,
        UPLOAD_DATE VARCHAR(20) NOT NULL,
        FILE_LOCATION VARCHAR(100) NOT NULL
    )"""
    cursor.execute(createTab)
    cl_dlpath = cf.get("client", "cl_dlpath") 
    start = 0
    lists = get_movies(ftp,lista,start)
    print(lists)
    for i in lists:
        a = i["name"]
        t = a.split(".")[0]
        b = i["size"]
        b=int(b[0])
        c = i["date"]
        c = str(c[0] +"-"+c[1] +"-"+ c[2])
        d = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        e = cl_dlpath
        ldb = "INSERT INTO " + table_name +"(NAME,FILENAME,SIZE,CREATE_DATE,UPLOAD_DATE,\
        FILE_LOCATION) VALUES('%s','%s','%s','%s','%s','%s')" %(t,a,b,c,d,e)
        cursor.execute(ldb)
        db.commit()
        print(i["name"]+" is success")
    db.close()
    download(ftp,lista)                            
    return ftp,lista
   
def download(ftp,lista):   
    cl_dlpath = cf.get("client", "cl_dlpath")   
    print(cl_dlpath)                              
    i=0
    totaln = len(lista)
    size_listn = []
    ftp.dir("", size_listn.append)
    loc = cl_dlpath                 
    print("")
    print("<<<<<<<<<开始下载!>>>>>>>>>")                    
    for name in lista:
        if i != totaln:
            print("------------------------------------------------")
            print("总进度<<<<<" + "%.2f%%" % (i/totaln * 100)+">>>>>") 
            print("------------------------------------------------")                            
            print("当前文件名称>>>>>>>>>>>>>" + name)
            size_listn=size_listn[1:]                       
            filesizen = size_listn[0].split()[4:5]
            filesizembn = int(filesizen[0])
            print("当前文件大小>>>>>" + \
                  str("%.4f" %(filesizembn/(1024*1024))) + "MB")
            i+=1
            DL = loc 
            LocalFile = DL+name                             
            bufsize = 1024
            print("")
            print(LocalFile)
            file = open(LocalFile, 'wb')                 
            ftp.retrbinary('RETR %s' %os.path.basename(LocalFile),\
                           file.write,bufsize)
            ftp.set_debuglevel(0)
        elif i == totaln:
            print("------------------------------------------------")
            print("总进度<<<<<" + "%.2f%%" % (i/totaln * 100)+">>>>>") 
            print("------------------------------------------------") 
            print("          <<<<<<<<<<下载完成>>>>>>>>>>          ")
            ftp.close()                                                
    
def get_movies(ftp,lista,start):
    sql_list = []
    size_listm=[]
    ftp.dir("", size_listm.append)
    for name in lista:
        size_listm=size_listm[1:]                       
        filesizem = size_listm[0].split()[4:5]
        movie = {}
        movie["name"] = name
        movie["size"] = filesizem
        movie["date"] = size_listm[0].split()[5:8]
        sql_list.append(movie)
    return sql_list

if __name__ == "__main__":
    information()

