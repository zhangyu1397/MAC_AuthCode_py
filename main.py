#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NetBrocastUdp.NetBroadcastUdp import BroadcastUdp
from File.File import File
import queue
import threading

class MainController:

    def __init__(self):
        self._sys_init()
        self._run()
        self.dataque = queue.Queue

    def _sys_init(self):
        self.broadcast = BroadcastUdp
        self.file = File

    def _run(self):
        threading.Thread(target=self._pth_run)
        while True:
            data = self.dataque.get()
            self.file.write_mac(data)

    def _pth_run(self):
        while True:
            data = self.broadcast.get_broadcast_data()
            self.dataque.put(data)

        #打开文件
        #建立服务器
        #建立广播程序
        #发送广播
        #接收广播
        #JSON分析
        #MAC换算
        #存储到文件