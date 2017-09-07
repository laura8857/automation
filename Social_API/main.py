# -*- coding: utf-8 -*-
# @Create Time    : 2017/4/28 18:00
# @File Name    : main.py
# @Introduction : API main

import funclist
import environment as env


group = funclist.group()
discover = funclist.discover()
entity = funclist.entity()
album = funclist.album()
trending = funclist.trending()
buddy = funclist.buddy()
divespot = funclist.divespot()
user = funclist.user()
notification = funclist.notification()
follow = funclist.follow()
divelog = funclist.divelog()
appbundle = funclist.appbundle()
divecert = funclist.divecert()
media = funclist.media()
slidepanel = funclist.slidepanel()
firmware = funclist.firmware()


if __name__ == "__main__":
    try:
        cf = env.target_server()

        for name, func in user:
            cf_apis_type = env.apis_type('TEST_' + 'user')
            cf.update(cf_apis_type)
            test_times = 2
            test_loops = 0
            time_exec = 0
            failure_count = 0
            time_raw = []
            print("Function = ", name)

            while test_times != 0:
                test_loops += 1
                func_res = func(cf)
                if func_res <= 5:
                    time_raw.append(func_res)
                    time_summary = sum(time_raw)
                    test_times -= 1
                    print("    ● Test times : %d ," % test_loops, "Elapsed time : %f" % func_res)
                else:
                    test_times -= 1
                    failure_count += 1
                    print("    ○ Test times : %d ," % test_loops, "Result : \033[1;31;27m failure")
                    print('\033[0m')

            print("-" * 60)
            print("Total test times : %d , " % test_loops,
                  'Failure rate : {:.2%}'.format(failure_count / test_loops))
            print("Total time : %f ," % sum(time_raw), "Average time : %f" % (sum(time_raw)/len(time_raw)))
            print("Max time : %f ," % max(time_raw), "Min time : %f ," % min(time_raw),
                  "Delta : %f" % (max(time_raw)-min(time_raw)))
            print("-" * 60 + "\n")

    except Exception as e:
        print(e)
