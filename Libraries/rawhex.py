# -*- coding: utf-8 -*-
# @Create Time  : 2017/04/28
# @File Name    : rawhex.py
# @Introduction : RawHex Transfer


from base64 import b64decode
import json

def raw2divedt(rawdata):
    temp = b64decode(rawdata)[6:12]

    year = ord(temp[0:1]) + ord(temp[1:2]) * 256
    month = ord(temp[3:4])
    day = ord(temp[2:3])
    min = ord(temp[4:5])
    hour = ord(temp[5:6])

    divedt = ("{0}-{1:02d}-{2:02d}T{3:02d}:{4:02d}:00-1000".format(year, month, day, hour, min))
    print('dive DT : ', divedt)
    return divedt


def raw2airpressure(rawdata):
    # temp = b64decode(rawdata)[6:12]
    dvsetting = b64decode(rawdata)[4:6]

    # dvsetting = temp[4:6]
    airpressure = (ord(dvsetting[1:2]) & 15) * 256 + ord(dvsetting[0:1])
    print('air pressure = ', airpressure)
    return airpressure


def raw2all(rawdata):

    temp = b64decode(rawdata)
    temp1 = temp[6:12]
    temp2 = temp[36:40]

    year = ord(temp1[0:1]) + ord(temp1[1:2]) * 256
    month = ord(temp1[3:4])
    day = ord(temp1[2:3])
    min = ord(temp1[4:5])
    hour = ord(temp1[5:6])

    count = ord(temp2[0:1]) + ord(temp2[1:2]) * 256 + ord(temp2[2:3]) * 65536 + ord(temp2[3:4]) * 16777216
    endp = 40 + count * 4
    temp3 = temp[40:endp]

    # print("{0}-{1:02d}-{2:02d}T{3:02d}:{4:02d}:00-1000".format(year, month, day, hour, min))

    alldumpslst = []
    for x in range(count):
        sTemperature = ord(temp3[4 * x:4 * x + 1]) + ord(temp3[4 * x + 1:4 * x + 2]) * 256
        sPressure = ord(temp3[4 * x + 2:4 * x + 3]) + ord(temp3[4 * x + 3:4 * x + 4]) * 256
        z = ('{"id":"' + str(x) + '","temperature":' + str(sTemperature) + ',"pressure":' + str(sPressure) + ',"time":null}')
        alldumpslst.append(z)
    print('dive profile :', alldumpslst)
    return alldumpslst


if __name__ == "__main__":
    diveRawHex = input("Please Input 'DiveRawHEX' Data : ")
    raw2divedt(diveRawHex)
    raw2airpressure(diveRawHex)
    raw2all(diveRawHex)
