# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/19
# @File Name    : album.py
# @Introduction : album apis test cases


from json import dumps
from requests import get
from time import time


def albumid(cf):
    """
    # GET /apis/album/v0/{albumId}, get album info
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion']}
    sub = [cf['api_host'], 'album/v0/', cf['albumid']]
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


def medialist(cf):
    """
    # GET /apis/album/v0/{albumId}/mediaList, get media list in album
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion']}
    sub = [cf['api_host'], 'album/v0/', cf['albumid'], '/mediaList?', cf['skip'], '&', cf['limit']]
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


def album_entityid_albumlist(cf):
    """
# GET /apis/album/v0/{entityId}/albumList, get entity album
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion']}
    sub = [cf['api_host'], 'album/v0/', cf['entityid'], '/albumList?', cf['skip'], '&', cf['limit']]
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
