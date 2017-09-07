# -*- coding: utf-8 -*-
# @Create Time  : 2017/05/24
# @File Name    : environment.py
# @Introduction : Validation request parameters


import configparser


def target_server():
    """
    1. 選擇“驗證的環境”，未選擇（預設）是“TEST”環境
    2. 讀取共同參數
    :return:
    """
    sel_server = input('\n' + "Please select a server number (1:Test, 2:Dev, 3:Prod): ")
    print('\n')
    server_dict = {"1": "TEST_COMMON", "2": "DEV_COMMON", "3": "PROD_COMMON"}
    if sel_server != '':
        target = server_dict.get(sel_server)
    else:
        target = "TEST_COMMON"

    # debug = input("Active 'Debug' mode (0/1): ")
    # debug_dict = {"0": "0", "1": "1"}
    # if debug != '':
    #     debug = int(debug_dict.get(debug))
    # else:
    #     debug = 0

    cf = configparser.ConfigParser()  # Init config file parser
    cf.read("mconfig.ini")  # read environment config for target server & api module
    common_lst = cf.items("COMMON")  # read 'COMMON' section
    api_lst = cf.items(target)
    env_dict = dict(common_lst + api_lst)

    return env_dict  # return env_dict, debug


def apis_type(api_type):
    """
    讀取“api”分類參數
    :return:
    """
    cf = configparser.ConfigParser()  # Init config file parser
    cf.read("mconfig.ini")  # read environment config for target server & api module
    api_parameters_lst = cf.items(api_type)  # read 'api type' section
    api_parameters_dict = dict(api_parameters_lst)

    return api_parameters_dict  # return api parameters

