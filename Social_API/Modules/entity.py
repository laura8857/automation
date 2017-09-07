# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/22
# @File Name    : entity.py
# @Introduction : entity apis test cases


from json import dumps
from requests import get
from time import time


def entity_entitylist(cf):
    """
    # GET /apis/entity/v0/entityList, query entity list
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'entity/v0/entityList?', cf['skip'], '&', cf['limit']]
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


def entity_language(cf):
    """
    # GET /apis/entity/v0/language, 查詢所有支援的語言資訊
    :return:
    """
    sub = [cf['api_host'], 'entity/v0/language']
    url = ''.join(sub)
    ts = time()
    res = get(url, timeout=5)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1) + '\n')
        return res.status_code
    else:
        time_cost = (te - ts)
        # print(dumps(res.json(), indent=1)+'\n')
        return time_cost


def entity_paymentmethod(cf):
    """
    # GET /apis/entity/v0/payment-method, 查詢所有支援的支付方式
    :return:
    """
    sub = [cf['api_host'], 'entity/v0/payment-method']
    url = ''.join(sub)
    ts = time()
    res = get(url, timeout=5)
    te = time()
    if res.status_code != 200:
        print(dumps(res.json(), indent=1) + '\n')
        return res.status_code
    else:
        time_cost = (te - ts)
        # print(dumps(res.json(), indent=1)+'\n')
        return time_cost


def entity_entityid(cf):
    """
    # GET /apis/entity/v0/{entityId}, query entity profile
    :return:
    """
    header = {"accept-language": cf['accept-language'], "entityId": cf['entityid']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid']]
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


def entity_entityid_staff_buddystatus(cf):
    """
    # GET /apis/entity/v0/{entityId}/Staff/buddyStatus, get buddy status in entity
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/Staff/buddyStatus?', cf['skip'], '&',
           cf['limit']]
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


def entity_entityid_staff_invite(cf):
    """
    # GET /apis/entity/v0/{entityId}/Staff/invite, get entity invite staffs
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/Staff/invite']
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


def entity_entityid_divecenter(cf):
    """
    # GET /apis/entity/v0/{entityId}/diveCenter, get dive center list
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/diveCenter?', cf['skip'], '&',
           cf['limit']]
    #  entity / v0 / 5cb458b0394111e78cb33fdffc203f85 / diveCenter?skip = 0 & limit = 10
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


def entity_entityid_divecenter_divecentid(cf):
    """
    # GET /apis/entity/v0/{entityId}/diveCenter/{diveCenterId}, get dive center Info
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/diveCenter/', cf['divecenterid']]
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


def entity_entityid_diverCertification_user_all(cf):
    """
    # GET /apis/entity/v0/{entityId}/diverCertification/user/all, get diver certification
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'],
           '/diverCertification/user/all?certificationRole=Regular&skip=0&limit=10']
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


def entity_entityid_information(cf):
    """
    # GET /apis/entity/v0/{entityId}/information, query entity information
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'skip': cf['skip'],
              'limit': cf['limit']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/information']
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


# def entity_entityid_service_serviceid(cf):  #(seemo:BUG 暫時用不到)
#     """
#     # GET /apis/entity/v0/{entityId}/service/{serviceId}, 取得 entity service
#     :return:
#     """
#     header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
#               'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'serviceId': cf['serviceid'],
#               'entityId': cf['entityid']}
#     sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/service/', cf['serviceid']]
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


def entity_entityid_services(cf):
    """
    # GET /apis/entity/v0/{entityId}/services, 取得某一 entity 所有的 services
    :return:
    """
    header = {'authorization': cf['auth_owner'], 'accept-language': cf['accept-language'],
              'x-platform': cf['x-platform'], 'x-appversion': cf['x-appversion'], 'entityId': cf['entityid']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/services']
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


def entity_entityid_staffs(cf):
    """
    # GET /apis/entity/v0/{entityId}/staffs, get all entity staffs
    :return:
    """
    header = {"accept-language": cf['accept-language']}
    sub = [cf['api_host'], 'entity/v0/', cf['entityid'], '/staffs?', cf['skip'], '&', cf['limit']]
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
