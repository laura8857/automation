# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/22
# @File Name    : divelog.py
# @Introduction : divelog apis test cases

from json import dumps, loads
from requests import get, post
from time import time


def divelog_getlogstatus(cf):
    """
    # GET /apis/divelog/v0/getLogStatus, get logs status/hide (Madlen's token & divelogId)
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'divelog/v0/getLogStatus?logIds=', cf['logids']]
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


def divelog_getrawlogs(cf):
    """
    # GET /apis/divelog/v0/getRawLogs, query raw dive logs (Pagination) (Madlen's token & userId)
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'divelog/v0/getRawLogs?type=0&', cf['filterby'], '&', cf['skip'], '&', cf['limit']]
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


def divelog_subsurface(cf):
    """
    # post /apis/divelog/v0/subsurface, upload subsurface xml file
    :return:
    """
    header = {'authorization': cf['auth_jesse'], 'accept-language': cf['accept-language']}
    body = cf['body_3rd_26']
    """ body_3rd_13 / body_3rd_26 / body_3rd_52 """
    print(body)
    body = loads(body)
    sub = [cf['api_host'], 'divelog/v0/subsurface']
    url = ''.join(sub)
    ts = time()
    res = post(url, headers=header, json=body, timeout=5)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1)+'\n')
        return res.status_code
    else:
        time_cost = (te-ts)
        # print(dumps(res.json(), indent=1)+'\n')
        return time_cost


def divelog_id(cf):
    """
    # GET //apis/divelog/v0/{id}, get raw divelog (Madlen's token & divelogId)
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'divelog/v0/', cf['id']]
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
