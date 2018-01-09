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
        main_thd = threading.Thread(target=self._pth_run)
        main_thd.start()
        while True:
            data = self.dataque.get()
            self.file.write_mac(data)

    def _pth_run(self):
        while True:
            data = self.broadcast.get_broadcast_data()
            if len(data) > 30:
                self.dataque.put(data)


main = MainController()
