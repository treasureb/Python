#! /usr/bin/python3

import sys
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
server.bind(('localhost',9090))

server.listen(5)
while True:
    conn,addr = server.accept()
    print("addr:%s " % str(addr))
    msg = 'welcome python web!' + "\r\n"
    conn.send(msg.encode('utf-8'))
    conn.close()
