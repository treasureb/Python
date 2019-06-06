#! /usr/bin/python3

import socket
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',9090))

msg = client.recv(1024)

print("server respond:%s" %str(msg))
client.close()
