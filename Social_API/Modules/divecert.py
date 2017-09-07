# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/18
# @File Name    : divecert.py
# @Introduction : divecert apis test cases

from json import dumps
from requests import get
from time import time


def divecert_certmetaall(cf):
    """
    # GET /apis/diveCert/v0/certMetaAll, 查詢所有 diveCert metadata
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


def divecert_instructor(cf):
    """
    # GET /apis/diveCert/v0/instructor, 查詢朋友裡的instructor
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'diveCert/v0/instructor?', cf['skip'], '&', cf['limit']]
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