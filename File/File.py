#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
class File:
    __fd = None
    def __init__(self):

        with os.open('MAC-AuthCode.txt', 'a+') as self.__fd:
            print('open MAC-AuthCode success\n')

    def write_mac(self, wirtestring):
        self.__fd.write(wirtestring)
