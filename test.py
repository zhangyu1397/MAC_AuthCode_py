#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue

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