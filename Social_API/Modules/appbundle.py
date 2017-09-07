# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/19
# @File Name    : appbundle.py
# @Introduction : appbundle apis test cases


from json import dumps
from requests import get
from time import time


def appbundle_bundle(cf):
    """
    # GET /apis/appBundle/v0/bundle, 取得 appBundle
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


def appbundle_country(cf):
    """
    # GET /apis/appBundle/v0/country, 以用戶IP反查國家地區資訊
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
