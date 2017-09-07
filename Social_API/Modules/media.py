# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/22
# @File Name    : media.py
# @Introduction : media apis test cases

from json import dumps
from requests import get
from time import time


def media_usermedia(cf):
    """
    # GET /apis/media/v0/userMedia, get user media(pagination)
    :return: 
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'media/v0/userMedia?userId=', cf['userid'], '&', cf['skip'], '&', cf['limit']]
    url = ''.join(sub)
    ts = time()
    res = get(url, headers=header, timeout=5)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1) + '\n')
        return res.status_code
    else:
        time_cost = (te - ts)
        # print(dumps(res.json(), indent=1)+'\n')
        return time_cost
