# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/19
# @File Name    : discover.py
# @Introduction : discover apis test cases

from json import dumps
from requests import get
from time import time


def discover_post_divelogfeed(cf):
    """
    # GET /apis/discover/v0/post/diveLogFeed, 查詢DiveLog的文章
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/diveLogFeed?' + cf['skip'] + '&' + cf['limit']]
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


def discover_post_livefeed(cf):
    """
    # GET /apis/discover/v0/post/liveFeed, 查詢全站貼文
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/liveFeed?', cf['skip'], '&', cf['limit']]
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


def discover_post_search(cf):
    """
    # GET /apis/discover/v0/post/search 搜尋文章
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/search?', cf['posttype'], '&', cf['skip'], '&', cf['limit']]
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


def discover_post_trendingfeed(cf):
    """
    # GET /apis/discover/v0/post/trendingFeed, 查詢TrendingFeed
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/trendingFeed?', cf['skip'], '&', cf['limit']]
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


def discover_post_groupfeed(cf):
    """
    # GET /apis/discover/v0/post/groupFeed, 查詢指定群組內的貼文
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/groupFeed?groupId=14&', cf['limit'], '&', cf['skip'],
           '&orderCriteria=popularity']
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


def discover_post_followerfeed(cf):
    """
    # GET /apis/discover/v0/post/followerFeed, 查詢我關注及好友的公開貼文 (TOKEN : jesse@deepblu.com)
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/followerFeed?' + cf['skip'] + '&' + cf['limit']]
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


def discover_post_userfeed(cf):
    """
    # GET /apis/discover/v0/post/userFeed, 查詢指定使用者的貼文
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/userFeed?userId=', cf['userid'], '&', cf['skip'], '&', cf['limit']]
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


def discover_post_comment_commentid(cf):
    """
    # GET /apis/discover/v0/post/comment/{commentId}, 查詢指定的評論
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/comment/1258']
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


def discover_post_divelog_divelogid(cf):
    """
    # GET /apis/discover/v0/post/diveLog/{diveLogId}, 用DiveLogId來查貼文
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/diveLog/', cf['divelogid']]
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


def discover_post_entityfeed(cf):
    """
    # GET /apis/discover/v0/post/entityFeed, 查詢Entity貼文
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/entityFeed?', 'entityId=', cf['entityid'], '&', cf['skip'], '&',
           cf['limit']]
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


def discover_post_search_tag(cf):
    """
    # GET /apis/discover/v0/post/search/tag, 搜尋Tag文章
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/search/tag?queryString=shark&orderCriteria=latest&', cf['skip'], '&',
           cf['limit']]
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


def discover_post_searchasdivebuddies(cf):
    """
    # GET /apis/discover/v0/post/searchAsDiveBuddies 搜尋文章 as diveBuddies
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/search/tag?queryString=shark&orderCriteria=latest&', cf['skip'], '&',
           cf['limit']]
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


def discover_post_trashcan(cf):
    """
    # GET /apis/discover/v0/post/trashcan, 搜尋使用者刪除的 post (Madlen Token)
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/trashcan?', cf['skip'], '&', cf['limit']]
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


def discover_post_postid(cf):
    """
    # GET /apis/discover/v0/post/{postId}, 查詢指定的貼文
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/', cf['postid']]
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


def discover_post_postid_comment(cf):
    """
    # GET /apis/discover/v0/post/{postId}/comment, 查詢指定文章的評論列表
    :return:
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'discover/v0/post/', cf['postid'], '/comment?', cf['skip'], '&', cf['limit']]
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
