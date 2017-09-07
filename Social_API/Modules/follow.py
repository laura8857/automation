# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/22
# @File Name    : follow.py
# @Introduction : follow apis test cases


from json import dumps
from requests import get
from time import time


def follow_getfollowstatus(cf):
    """
    # GET /apis/follow/v0/getFollowStatus, get user status (Madlen's token & userId)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'follow/v0/getFollowStatus?userId=', cf['userid']]
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


def follow_getfollowers(cf):
    """
    # GET /apis/follow/v0/getFollowers, get Follower users (Madlen's token & userId)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'follow/v0/getFollowers?userId=', cf['userid'], '&', cf['skip'], '&', cf['limit']]
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


def follow_getfollowings(cf):
    """
    # GET /apis/follow/v0/getFollowings, get Following users (Madlen's token & userId)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'follow/v0/getFollowers?userId=', cf['userid'], '&', cf['skip'], '&', cf['limit']]
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
