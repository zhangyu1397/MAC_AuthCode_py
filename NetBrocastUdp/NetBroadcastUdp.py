#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PickupHeadData.PickupHeadData import PickupHeadData
import socket
import sys


class BroadcastUdp:

    _toBroadcastDat = None

    def __init__(self, port):
        self.__parck = PickupHeadData()
        self.__port = port
        self.__setup_client()
        self.__broadcast_data()

    def __setup_client(self):
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        self._udp.bind(('127.0.0.1', self.__port))

    def __broadcast_data(self):
        print("broadcast\n")
        self._udp.sendto(self.__parck.prebuffer, ('255.255.255.255', self.__port))

    def get_broadcast_data(self):
        data, addr = self._udp.recvfrom(1024)
        print("data:",data)
        return self.__parck.do_unpick_data(data)





