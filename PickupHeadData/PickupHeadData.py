#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NetBrocastUdp.HeadData import HeadData
import struct
import binascii
import ctypes


class PickupHeadData(HeadData):

    def __init__(self):
        self.__head_data = HeadData.broadcast_head
        self.do_pickup_data()

    def do_pickup_data(self):
        headstr = struct.Struct('BBBBIIBBHI')
        self.prebuffer = headstr.pack(*self.__head_data)

    def do_unpick_data(self, data):
        ndata = data[20:-2]
        if len(ndata) > 20:
            print("get carema data: %s" % ndata)
        return ndata




