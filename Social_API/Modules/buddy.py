# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/22
# @File Name    : buddy.py
# @Introduction : buddy apis test cases

from json import dumps
from requests import get
from time import time


def buddy_userid_buddy_list(cf):
    """
    # GET /apis/buddy/v0/{userId}/buddy/list, 查詢我的Buddy清單 (Madlen's userId)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'buddy/v0/', cf['userid'], '/buddy/list?', cf['skip'], '&', cf['limit']]
    # buddy / v0 / 56dd612563ed3f065480ed9c / buddy / list?skip = 0 & limit = 10
    url = ''.join(sub)
    ts = time()
    res = get(url, headers=header, timeout=5)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1)+'\n')
        return res.status_code
    else:
        time_cost = (te-ts)
        # print(dumps(res.json(), indent=1)+'\n')
        return time_cost


def buddy_userid_request_list(cf):
    """
    # GET /apis/buddy/v0/{userId}/request/list, 查詢我邀請中的buddy列表 (Madlen's userId)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'buddy/v0/', cf['userid'], '/request/list?', cf['skip'], '&', cf['limit']]
    url = ''.join(sub)
    ts = time()
    res = get(url, headers=header, timeout=5)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1)+'\n')
        return res.status_code
    else:
        time_cost = (te-ts)
        # print(dumps(res.json(), indent=1)+'\n')
        return time_cost
