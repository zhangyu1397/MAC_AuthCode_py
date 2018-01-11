#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PickupHeadData.PickupHeadData import PickupHeadData
import socket
import select



class BroadcastUdp:

    _toBroadcastDat = None

    def __init__(self, port):
        self.__parck = PickupHeadData()
        self.__port = port
        self.__setup_server()
        self.__broadcast_data()

    def __setup_server(self):
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        self._udp.bind(('', self.__port))

    def __broadcast_data(self):
        self._udp.sendto(self.__parck.prebuffer, ('255.255.255.255', self.__port))

    def get_broadcast_data(self):
        input = [self._udp]
        time_out = 0
        readable, writable, exceptional = select.select(input, [], [], time_out)
        for a in readable:
            if a == self._udp:
                data, addr = self._udp.recvfrom(1024)
                return self.__parck.do_unpick_data(data)
        return ""




