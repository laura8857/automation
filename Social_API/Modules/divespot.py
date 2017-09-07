# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/19
# @File Name    : divespot.py
# @Introduction : divespot apis test cases


from requests import get
from json import dumps
from time import time
import environment


def divespot(cf):
    """
    # GET /apis/divespot/v0, get divespots
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'appBundle/v0/bundle']
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


def divespot_divesites(cf):
    """
    # GET /apis/divespot/v0/divesites, get divesites
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'appBundle/v0/bundle']
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
