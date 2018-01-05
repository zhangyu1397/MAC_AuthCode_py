#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
class FIle:
    __fd = None
    def __init__(self):

        with open('MAC-AuthCode.txt', 'a+') as self.__fd:
            print('open MAC-AuthCode success\n')

    def write_mac(self, wirtestring):
        self.__fd.write(wirtestring)
