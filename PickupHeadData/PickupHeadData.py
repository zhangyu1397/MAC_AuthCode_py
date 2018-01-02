#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

class PickupHeadData:
    __HeadStruct = None
    HeadString = None
    def __init__(self, HeadStrcut):
        self.__HeadStruct = HeadStrcut

    def DoPickupData(self):
        self.HeadString = struct.pack()