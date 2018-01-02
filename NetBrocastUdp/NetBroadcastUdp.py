#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,traceback
import sys
class BroadcastUdp:
    _toBroadcastDat = None
    def __init__self(self, data):
        self._toBroadcastDat = data

    def __SetupClient(self):
        Udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        Udp.setsockopt(socket.SOL_SOCKET, socket.INADDR_BROADCAST, 1)
        Udp.sendto(self._toBroadcastDat, ('127.0.0.1', 9999))


