#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NetBrocastUdp.NetBroadcastUdp import BroadcastUdp
from File.File import File
import queue
import threading


class MainController:
    dataque = None

    def __init__(self):
        self._sys_init()
        self.dataque = queue.Queue()
        self._run()

    def _sys_init(self):
        self.broadcast = BroadcastUdp(34569)
        self.file = File()

    def _run(self):
        main_thd = threading.Thread(target=self._pth_run)
        main_thd.start()
        while True:
            data = self.dataque.get()
            print(data,__name__)
            self.file.write_mac(data)

    def _pth_run(self):
        while True:
            data = self.broadcast.get_broadcast_data()
            if len(data) >20:
                self.dataque.put(data)

main = MainController()
        #打开文件
        #建立服务器
        #建立广播程序
        #发送广播
        #接收广播
        #JSON分析
        #MAC换算
        #存储到文件