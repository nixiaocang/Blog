# -*- coding: utf-8 -*-
import sys
import struct
import base64
import StringIO
from os.path import isabs


def getxorvalue(org, key):
    mylist = []
    orghex = str2hex(org)
    keyhex = str2hex(key)
    minlen = min(len(orghex), len(keyhex))
    for i in range(minlen):
        a = int(orghex[i][0], 16) * 16 + int(orghex[i][1], 16)
        b = int(keyhex[i][0], 16) * 16 + int(keyhex[i][1], 16)
        B = struct.pack('B', a ^ b)
        mylist.append(B)
    result = ''.join(mylist) + org[minlen:]
    return result


def str2hex(value):
    hexs = []
    for val in value:
        rst = hex(ord(val))[2:]
        if len(rst) == 2:
            hexs.append(rst)
        else:
            hexs.append('0' + rst)
    return hexs


class DataCrypter:
    def __init__(self, KEY1='WoBig5Liu0HaiZhi', KEY2='PingNiuBi007', NUM1=138, NUM2=15):
        self.KEY1 = KEY1
        self.KEY2 = KEY2
        self.NUM1 = NUM1
        self.NUM2 = NUM2

    def _wrap_data(self, data):
        return base64.b64encode(data)

    def _unwrap_data(self, data):
        return base64.b64decode(data)

    def encrypt_data(self, in_data, ssid=''):
        # 待加密文件必须是压缩文件，典型如tar.gz
        in_data = self._wrap_data(in_data)
        if ssid:
            self.KEY1 = ssid[:8] + ssid[-8:]
            self.KEY2 = ssid[:6] + ssid[-6:]
        if len(in_data) >= self.NUM1:
            size = self.NUM1 + self.NUM2
            head = getxorvalue(in_data[:self.NUM1], self.KEY1)
            tail = getxorvalue(in_data[self.NUM1:size], self.KEY2)
            out_data = head
            out_data += tail
            out_data += in_data[size:]
            out_data += struct.pack('i', self.NUM1)
        else:
            ANOTHER_KEY = '007_' + self.KEY2 + '_HaiZHI'
            while len(ANOTHER_KEY) < len(in_data):
                ANOTHER_KEY += ANOTHER_KEY
            all_data = getxorvalue(in_data, ANOTHER_KEY)
            out_data = all_data
            out_data += struct.pack('i', self.NUM1)
        out_data = self._wrap_data(out_data)
        return out_data

    def decrypt_data(self, in_data, ssid=''):
        in_data = self._unwrap_data(in_data)
        if ssid:
            self.KEY1 = ssid[:8] + ssid[-8:]
            self.KEY2 = ssid[:6] + ssid[-6:]
        module = struct.unpack('i', in_data[-4:])[0]
        if len(in_data) >= module:
            size = module + self.NUM2
            out_data = getxorvalue(in_data[:module], self.KEY1)
            out_data += getxorvalue(in_data[module:size], self.KEY2)
            out_data += in_data[size:-4]
        else:
            ANOTHER_KEY = '007_' + self.KEY2 + '_HaiZHI'
            while len(ANOTHER_KEY) < len(in_data):
                ANOTHER_KEY += ANOTHER_KEY
            out_data = getxorvalue(in_data[:-4], ANOTHER_KEY)
        out_data = self._unwrap_data(out_data)
        return out_data


if __name__ == "__main__":
    # s = 'Ul1HNxo8XEYlJT8WDCAFKgwlCQYDL3QNigAAAA=='
    s = sys.argv[1]
    print s
    res = DataCrypter().decrypt_data(s, 'yiersansiwuliuqi')
    print res
