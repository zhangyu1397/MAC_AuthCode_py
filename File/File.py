#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from File.MD5 import Md5
import os
import json


class File:
    __fd = None

    def __init__(self):
            print('open MAC-AuthCode success\n')

    def write_mac(self, wirtestring):
        data = json.loads(wirtestring)
        print(data)
        mdata = data['NetWork.NetCommon']
        mac = mdata['mac']
        ret, ser = self.__check_mac(mac)
        if ret:
            md5 = Md5(mac)
            self.__data_trans(md5, ret)
            self.__fd.write(self.__data_trans(ret, mac, data))

    def __data_trans(self, ret, mac, data):
        #xxx MAC: 00:12:16:82:0a:7b    AuthCode: 98cc52ee711d20953575d67a280abc28
        ret += 1
        pic_data = "%3d MAC: %s    AuthCode: %s"%(ret, mac, data)
        return pic_data

    def __check_mac(self, mac):
        with os.open('MAC-AuthCode.txt', 'a+') as self.__fd:
            for eachline in self.__fd:
                ser,gmac = self.__get_mac(eachline)
                if gmac == mac:
                    return 0, ser
            return 1, ser

    def __get_mac(self, data):
        ser = data[0:2]
        mac = data[9:26]
        return int(ser), mac



