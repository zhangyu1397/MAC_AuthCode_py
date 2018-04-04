#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NetBrocastUdp.NetBroadcastUdp import BroadcastUdp
from File.File import File
from FILEMAC.FileMac import FileMac
import queue
import threading


class MainController:
    dataque = None

    def __init__(self):
        self.broadcast = BroadcastUdp(34569)
        self.file = File()
        self.fileMac = FileMac()
        self.dataque = queue.Queue()
        self._run()

    def _run(self):
        self.__run_flag = 1
        run_time_thd = threading.Timer(20, self._run_time)
        getCarema_thd = threading.Thread(target=self._getCarema_run)
        getFileMac_thd = threading.Thread(target=self.__getFile_Mac)
        run_time_thd.start()
        getCarema_thd.start()
        getFileMac_thd.start()

        while self.__run_flag:
            if not self.dataque.empty():
                data = self.dataque.get()
                if len(data) > 0:
                    print("data %s\n" % data)
                self.file.write_mac(data)

    def _getCarema_run(self):
        while self.__run_flag:
            data = self.broadcast.get_broadcast_data()
            #print("data %s\n" % data)
            if len(data) > 10:
                self.dataque.put(data)

    def __getFile_Mac(self):
        while self.__run_flag:
            mac = self.fileMac.getmac()
            if len(mac) >10:
                self.dataque.put(mac)

    def _run_time(self):
        self.__run_flag = 0


main = MainController()
