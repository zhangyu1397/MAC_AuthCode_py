#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NetBrocastUdp.NetBroadcastUdp import BroadcastUdp
from File.File import File
import queue
import threading


class MainController:
    dataque = None

    def __init__(self):
        self.broadcast = BroadcastUdp(34569)
        self.file = File()
        self.dataque = queue.Queue()
        self._run()

    def _run(self):
        self.__run_flag = 1
        run_time_thd = threading.Timer(10, self._run_time)
        main_thd = threading.Thread(target=self._pth_run)
        run_time_thd.start()
        main_thd.start()
        while self.__run_flag:
            if not self.dataque.empty():
                data = self.dataque.get()
                self.file.write_mac(data)

    def _pth_run(self):
        while self.__run_flag:
            data = self.broadcast.get_broadcast_data()
            if len(data) > 30:
                self.dataque.put(data)

    def _run_time(self):
        self.__run_flag = 0


main = MainController()
