# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/19
# @File Name    : firmware.py
# @Introduction : firmware apis test cases

from json import dumps
from requests import get
from time import time


def checkversion(cf):
    """
    # GET /apis/firmware/v0/checkVersion, check firmware version
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'firmware/v0/checkVersion?', cf['mno']]
    url = ''.join(sub)
    ts = time()
    res = get(url, headers=header, timeout=3)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1)+'\n')
        return res.status_code
    else:
        time_cost = (te-ts)
        print(dumps(res.json(), indent=1)+'\n')
        return time_cost
