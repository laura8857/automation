# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/22
# @File Name    : user.py
# @Introduction : user apis test cases

from json import dumps
from requests import get
from time import time


def activeaccount(cf):
    """
    # GET /apis/user/v0/activeAccount, 2.4 透過email url來確認帳號,回傳一個html頁面 (Madlen's userId)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v0/activeAccount?ownerId=', cf['ownerid'], '&code=1111']
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


def suggestdiver(cf):
    """
    # GET /apis/user/v0/suggestDiver, 潛水員建議清單 query suggest divers list
    :return: 
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v0/suggestDiver']
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


# def switchtoken(cf):
#     """
#     # POST /apis/user/v0/switchToken, 2.4 token switch
#     :return:
#     """
#     header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
#     sub = [cf['api_host'], 'user/v0/switchToken']
#     url = ''.join(sub)
#     ts = time()
#     res = get(url, headers=header, timeout=5)
#     te = time()
#     if res.status_code != 200:
#         print(dumps(res.json(), indent=1)+'\n')
#         return res.status_code
#     else:
#         time_cost = (te-ts)
#         # print(dumps(res.json(), indent=1)+'\n')
#         return time_cost


def profile(cf):
    """
    # GET /apis/user/v0/profile, get user profile by deepbluId (Madlen's deepbluId)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v0/profile?deepbluId=', cf['deepbluid']]
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


def search(cf):
    """
    # GET /apis/user/v0/search, search user
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v0/search?', cf['skip'], '&', cf['limit'], '&searchString=dive&excludeBuddy=0']
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


def profile_userid(cf):
    """
    # GET /apis/user/v0/profile/{userId}, 查詢基本資料 {Madlen userId}
    :return: 
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v0/profile/', cf['userid']]
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


def termofcondition(cf):
    """
    # GET /apis/user/v0/termOfCondition, get if user need to show term of condition page
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v0/termOfCondition']
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


def v0_user_atdata(cf):
    """
    # GET /apis/user/v0/user/atData, 查詢@清單資料 {Madlen token}
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v0/user/atData']
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


def v1_user_atdata(cf):
    """
    # GET /apis/user/v1/user/atData 查詢@清單資料(group & buddy & Org.)  {Madlen token}
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'user/v1/user/atData']
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
