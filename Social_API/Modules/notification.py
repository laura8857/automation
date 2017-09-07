# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/23
# @File Name    : notification.py
# @Introduction : notification apis test cases

from json import dumps, loads
from requests import get, post
from time import time, strftime


# def notification_notificationlogs(cf):
#     """
#     # GET /apis/notification/v0/notificationLogs, query notificationLogs (TOKEN : JESSE)
#     :return:
#     """
#     header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
#     sub = [cf['api_host'], 'notification/v0/notificationLogs?', cf['skip'], '&', cf['limit']]
#     url = ''.join(sub)
#     ts = time()
#     res = get(url, headers=header, timeout=5)
#     te = time()
#     if res.status_code != 200:
#         print(dumps(res.json(), indent=1) + '\n')
#         return res.status_code
#     else:
#         time_cost = (te - ts)
#         # print(dumps(res.json(), indent=1)+'\n')
#         return time_cost


def notification_systemnotif(cf):
    """
    # POST  /apis/notification/v0/systemNotif, send Notif From A to B
    :return:
    """
    header = {'authorization': cf['auth_deepblu'], 'accept-language': cf['accept-language']}
    body = cf['body_notif']
    body = loads(body)
    body["msg"] = strftime("%d/%m/%Y,%I:%M:%S, " + "TEST Message")
    sub = [cf['api_host'], 'notification/v0/systemNotif']
    url = ''.join(sub)
    ts = time()
    res = post(url, headers=header, json=body, timeout=5)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1) + '\n')
        return res.status_code
    else:
        time_cost = (te - ts)
        # print(dumps(res.json(), indent=1)+'\n')
        return time_cost


# def notification_unreadcount(cf):
#     """
#     # GET /apis/notification/v0/unReadCount, get notificationLogs unread count (TOKEN : JESSE)
#     :return:
#     """
#     header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language']}
#     sub = [cf['api_host'], 'notification/v0/unReadCount']
#     url = ''.join(sub)
#     ts = time()
#     res = get(url, headers=header, timeout=5)
#     te = time()
#     if res.status_code != 200:
#         print(dumps(res.json(), indent=1) + '\n')
#         return res.status_code
#     else:
#         time_cost = (te - ts)
#         # print(dumps(res.json(), indent=1)+'\n')
#         return time_cost
