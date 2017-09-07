# @Create Time  : 2017/05/23
# @File Name    : slidepanel.py
# @Introduction : slidepanel apis test cases

from json import dumps
from requests import get
from time import time


def slidepanel_allslide(cf):
    """
    # GET /apis/slidePanel/v0/allSlide
    :return: 
    """
    header = {'accept-language': cf['accept-language']}
    sub = [cf['api_host'], 'slidePanel/v0/allSlide']
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
