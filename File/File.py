#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from File.MD5 import Md5
import json


class File:
    __fd = None
    __mac_ser = 0

    def __init__(self):
        with open("./MAC-AuthCode.txt", 'a+') as self.__fd:
            print("sucess open\n")

    def write_mac(self, mac):
        with open("./MAC-AuthCode.txt", 'a+') as self.__fd:
            '''
            data = json.loads(wirtestring)
            mdata = data['NetWork.NetCommon']
            #mac = mdata['MAC']
            mac = '00:12:17:21:da:ed'
            '''
            if len(mac) < 10:
                return -1
            ret, ser = self.__check_mac(mac)
            if ret == 1:
                md5 = Md5(mac)
                self.__fd.seek(0, 2)  # 0，光标移动到头；1光标移动当前位置；2光标移动末尾
                self.__fd.write(self.__data_trans(ser, mac, md5.md5_data))
                return 1

    def __data_trans(self, ret, mac, data):
        ret += 1
        pic_data = "%3d MAC: %s    AuthCode: %s\n" % (ret, mac, data)
        return pic_data

    def __check_mac(self, mac):
        self.__fd.seek(0, 0)
        max_ser = 0
        while True:
            read_line = self.__fd.readline(1024)
            if read_line == "":
                return 1, max_ser
            if len(read_line) < 20:
                continue
            ser, gmac = self.__get_mac(read_line)
            if ser > max_ser:
                max_ser = ser
            if gmac == mac:
                return 0, ser

    def __get_mac(self, data):
        mac = data[9:26]
        ser = data[0:3]
        if len(ser) == 3:
            tmp = int(ser)
            return tmp, mac
        return 0, mac




