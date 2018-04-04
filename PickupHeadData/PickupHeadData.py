#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NetBrocastUdp.HeadData import HeadData
import struct
import json
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
        ndata = data[20:]
        ndata = ndata.rstrip(b'\0x00')
        ndata = ndata.rstrip()
        if len(ndata) > 30:
            tdata = json.loads(ndata)
            mdata = tdata['NetWork.NetCommon']
            mac = mdata['MAC']
            print("get carema MAC: %s\n" % mac);
            #mac = '00:12:17:21:da:ed'

            return mac
        return ""




