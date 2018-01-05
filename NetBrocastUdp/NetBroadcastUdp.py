#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import sys

class BroadcastUdp:
    _toBroadcastDat = None

    def __init__(self, data, port):
        self._toBroadcastDat = data
        self.__setup_client()
        self._port = port

    def __setup_client(self):
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udp.setsockopt(socket.AF_INET, socket.SO_BROADCAST, 1)
        self._udp.bind('127.0.0.1', self._port)

    def __broadcast_data(self):
        self._udp.sendto(self._toBroadcastDat, ('255.255.255.255', 34569))

    def get_broadcast_data(self):
        data = self._udp.recvfrom(1024)
        return data




