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
