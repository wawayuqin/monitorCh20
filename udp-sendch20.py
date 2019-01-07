#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
from getch20 import get_ch20
import time
#向云服务器发送采集的甲醛数据
ip_port = ('',8888)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data='20' #get_ch20()
    sk.sendall(data)
    time.sleep(5)


sk.close()

