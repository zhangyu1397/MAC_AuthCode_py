#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib


class Md5:
    __add_str = "+\\<_\\>\\)\\<ipCameraFanvil"

    def __init__(self, str):
        str = str.lower()
        str = str + self.__add_str
        self.md5_data = hashlib.md5(str)

