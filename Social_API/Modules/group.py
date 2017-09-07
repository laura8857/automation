# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/22
# @File Name    : group.py
# @Introduction : group apis test cases

from json import dumps
from requests import get
from time import time


def group_all(cf):
    """
    # GET /apis/group/v0/all, 查詢全部群組
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/all?', cf['skip'], '&', cf['limit'], '&', 'orderCriteria=popularity']
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


def group_search(cf):
    """
    # GET /apis/group/v0/search, 依群組名稱關鍵字搜尋
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/search?', cf['skip'], '&', cf['limit'], '&orderCriteria=popularity']
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


def group_mygroup(cf):
    """
    # GET /apis/group/v0/myGroup, 查詢我的群組 (Madlen Token)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/search?', cf['skip'], '&', cf['limit'], '&orderCriteria=popularity']
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


def group_mygroupscount(cf):
    """
    # GET /apis/group/v0/myGroupsCount, 查詢我自已已建立的群組數量 (Madlen Token)
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/myGroupsCount']
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


def group_suggest(cf):
    """
    # GET /apis/group/v0/suggest, 推荐群組 {Madlen token}
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/suggest']
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


def group_groupid_buddyandfollower(cf):
    """
    # GET /apis/group/v0/{groupId}/buddyAndFollower, 取得朋友以及追蹤者在這個群組裡的狀態 {Madlen token}
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/', cf['groupid'], '/buddyAndFollower']
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


def group_groupid_buddystatus(cf):
    """
    # GET /apis/group/v0/{groupId}/buddyStatus, 取得朋友在這個群組裡的狀態
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/', cf['groupid'], '/buddyStatus?', cf['skip'], '&', cf['limit']]
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


def group_groupid_inviteusers(cf):
    """
    # GET /apis/group/v0/{groupId}/inviteUsers, 取得邀請加入的成員列表
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/', cf['groupid'], '/inviteUsers?', cf['skip'], '&', cf['limit']]
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


def group_groupid_member(cf):
    """
    # GET /apis/group/v0/{groupId}/member, 查詢指定群組的成員列表
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/', cf['groupid'], '/member?', cf['skip'], '&', cf['limit']]
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


def group_groupid_profile(cf):
    """
    # GET /apis/group/v0/{groupId}/profile, 查詢群組Profile
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/', cf['groupid'], '/member?', cf['skip'], '&', cf['limit']]
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


def group_groupid_requestjoin(cf):
    """
    # GET /apis/group/v0/{groupId}/requestJoin, 取得邀請加入的成員列表
    :return: 
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/', cf['groupid'], '/requestJoin?', cf['skip'], '&', cf['limit']]
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



def group_userid_group(cf):
    """
    # GET /apis/group/v0/{userId}/group, 查詢指定使用者的群組
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'group/v0/', cf['userid'], '/group?orderCriteria=identity', '&', cf['skip'], '&', cf['limit']]
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
