# -*- coding: utf-8 -*-
# @Time    : 2017/2/13 下午2:50
# @Author  : Yuhsuan
# @File    : deepblu_api.py
# @Software: PyCharm Community Edition

# link : http://test.tritondive.co:3000/explorer/
# Token : YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy

import requests
from datetime import datetime

# GET /users
def get_users(email):
    url = 'http://test.tritondive.co:3000/1/api/users?filter=%7B%22where%22%3A%7B%22email%22%3A%22'+ email+'%22%7D%7D&access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy'
    result = requests.get(url)
    return result.json()

# POST /NotificationLogs/sendGroupSNS
# content: 顯示的內容
# url: deepblu link or else
# title: I don't know
# type: GCM or APNS or all
# userid: e.g. 587db9693119400d12826869
def send_push_msg(content, url, title, type, user_id):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = now + ' ' + content
    #url = 'http://test.tritondive.co:3000/1/api/NotificationLogs/sendGroupSNS?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy&announce=test%2014%3A33&url=deepblu%3A%2F%2Fdeepblu.link%2Fgroup%3FgroupId%3D541&title=hello%20world&APNSorGCM=GCM&ownerId=587db9693119400d12826869&mode=go'
    url = 'http://test.tritondive.co:3000/1/api/NotificationLogs/sendGroupSNS?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy&announce='+content+'&url='+url+'&title='+title+'&APNSorGCM='+type+'&ownerId='+user_id+'&mode=go'
    result = requests.post(url)
    if result.status_code==200:
        print('Send push message success')
    else:
        print('Please check with a ming for api')


if __name__ == "__main__":
    # Get
    dict = {}
    #Please input your email account
    result = get_users('test03@test.com')
    dict = result[0]
    user_id = dict['id']

    # Post message to user
    content = 'test message'
    url = 'deepblu://deepblu.link/group?groupId=541'
    title = 'test'
    type = 'APNS' # GCM->android or APNS->ios or All
    send_push_msg(content,url,title,type,user_id)
