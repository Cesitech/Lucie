#!/usr/bin/env python
# coding: utf-8

import socket

hote = "localhost"
port = 6009

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

socket.send(b"getCoord();")
print("______")
msg = socket.recv(9999999)
print(msg)
print("Close")
socket.close()
