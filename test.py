#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue
import os
'''
q = queue.Queue(0)
q.put(10)
q.put('a')
q.put('b')
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
print("error\n")
print("%3d"%(3))
data = "123 MAC: 00:12:16:82:0a:7b    AuthCode: 98cc52ee711d20953575d67a280abc28"
print(data[0:2])
print(data[9:26])

ret = 5
mac = "00:12:16:82:0a:7b"
data = "98cc52ee711d20953575d67a280abc28"

redata = "%3d MAC: %s    AuthCode: %s"%(ret, mac, data)
print(redata)
broadcast_head = [0xff, 0, 0, 0, 0, 0, 0, 0, 0x5fa, 0]
print(*broadcast_head)
fd = None
'''

'''
fd = open("./MAC-AuthCode.txt", 'a+')
print("aaaa")
fd.write("aaaa\n")
fd.seek(2)
for line in fd.readlines():
    print(line.strip())
'''
'''
class TestOpen:
    __fd = None
    def __init__(self):
        with open("./MAC-AuthCode.txt", 'r') as self.__fd:
            print("sucess open\n")

    def writetest(self):
        self.__fd.write("ssssss")



main = TestOpen()
main.writetest()
'''
'''
import hashlib

ss = "00:12:16:82:0a:7b+\\<_\\>\\)\\<ipCameraFanvil"
print(type(ss))
md5 = hashlib.md5()
md5.update(ss.encode("utf-8"))
print(md5.hexdigest())

'''
aa = b"  1 MAC: 00:12: 16:82: 0a: 7c AuthCode: 98cc52ee711d20953575d67a280abc28"
#a = aa.find("MAC", 0, len(aa))
print(aa[:3])
print(int(aa[:3]))
print("xx")
print(type(aa[1]))
print("\10")
print("xxx")

