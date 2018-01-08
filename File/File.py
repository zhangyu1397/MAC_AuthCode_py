#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from File.MD5 import Md5
import os
import json


class File:
    __fd = None
    MAX_READLINES = 1024
    __mac_ser = 0
    def __init__(self):
        with open("./MAC-AuthCode.txt", 'a+') as self.__fd:
            print("sucess open\n")

    def write_mac(self, wirtestring):
        with open("./MAC-AuthCode.txt", 'a+') as self.__fd:
            data = json.loads(wirtestring)
            mdata = data['NetWork.NetCommon']
            mac = mdata['MAC']
            ret, ser = self.__check_mac(mac)
            if ret == 1:
                md5 = Md5(mac)
                self.__fd.seek(0, 2)  # 0，光标移动到头；1光标移动当前位置；2光标移动末尾
                self.__fd.write(self.__data_trans(ser, mac, md5.md5_data))

    def __data_trans(self, ret, mac, data):
        ret += 1
        pic_data = "%3d MAC: %s    AuthCode: %s\n" % (ret, mac, data)
        return pic_data

    def __check_mac(self, mac):
        self.__fd.seek(0, 0)
        while True:
            read_line = self.__fd.readline(1024)
            ser, gmac = self.__get_mac(read_line)
            if read_line == "":
                return 1, ser
            print("mac:%s gmac:%s\n" % (mac, gmac))
            if gmac == mac:
                return 0, ser

    def __get_mac(self, data):
        tmp = 0
        #pdata = str(data, encoding="utf-8")
        print("data type:", type(data))


        mac = data[9:26]
        ser = data[0:3]

        if len(ser) == 3:
            print("ser",int(ser))
            print("ll", type(ser[0]), len(ser[-1]))
            tmp = int(ser)
            if tmp > self.__mac_ser:
                self.__mac_ser = tmp
                print("mac_ser:", self.__mac_ser)
            return self.__mac_ser, mac
        print("mac_ser:", self.__mac_ser)
        return self.__mac_ser, mac




