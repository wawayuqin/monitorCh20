#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import socket
import pymysql
def connect_wxremit_db():
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='',
                           database='jiance',
                           charset='latin1')
def insert_nongdu(nongdu):
        con = connect_wxremit_db()
        cur = con.cursor()
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            sql_str = ("INSERT INTO test(nongdu,timestamp)"+" VALUES('%s','%s')" % (nongdu,dt))
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            #logging.exception('Insert operation error')
            raise
        finally:
            cur.close()
            con.close()
    assert len(rows) == 1, 'Fatal error: country_code does not exists!'
    return rows[0][0]
#nd=query_country_name('1')
#print(nd)
ip_port = ('',8888)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:

    conn,address =  sk.accept()
    Flag = True
    while Flag:
        data = conn.recv(1024)
        if len(data)>1:
             insert_nongdu(data)
             print data
    conn.close()

