# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/23
# @File Name    : trending.py
# @Introduction : trending apis test cases

from json import dumps
from requests import get
from time import time


def trending_slider(cf):
    """
    # GET /apis/trending/v0/slider, Social_Web 取得 Trending Sliders
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'trending/v0/slider']
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


def trending_slider_mobile(cf):
    """
    # GET /apis/trending/v0/slider/mobile, mobile 取得 Trending Sliders
    :return: 
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'trending/v0/slider/mobile']
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
