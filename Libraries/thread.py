# -*- coding: utf-8 -*-
# @Time   : 2017/04/28 18:00
# @File   : time_usage.py
# Purpose : thread amount & summary


import pprint
from threading import Thread
from queue import Queue


def run(num, func):
    global q
    q = Queue(num)

    # Thread pool
    th = []

    for i in range(num):
        t = Thread(target=func, name="t.%d" % i)
        th.append(t)
    # start thread
    for i in th:
        i.start()

    # wait for all thread
    for i in th:
        i.join()
    return summary(num)


def summary(num):
    global q
    # result pool
    res_pool = []
    # time pool
    time_pool = []
    # name
    name = ""
    for i in range(num):
        res = q.get()
        time_pool.append(res['time'])
        res_pool.append(res['result'])
        name = res['name']

    fail_count = 0
    for i in res_pool:
        if not i:
            fail_count += 1

    result = {'test_case': name,
              'fail_rate': '{:.2%}'.format(fail_count / num),
              'max_time': '{:.2f} ms'.format(max(time_pool) * 1000),
              'min_time': '{:.2f} ms'.format(min(time_pool) * 1000),
              'avg_time': '{:.2f} ms'.format((sum(time_pool) / len(time_pool)) * 1000)
              }

    pprint.pprint(result, depth=2, compact=True)
    print('\n')
    return result
