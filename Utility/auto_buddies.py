# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 上午10:36
# @Author  : Yuhsuan
# @File    : auto_buddies.py
# @Software: PyCharm Community Edition
# 自動建立帳號
# 自動增加好友
import requests
import datetime

server = "http://test.tritondive.co:8000/"
server2 = "http://test.tritondive.co:3000/"
server3 = "https://test.tritondive.co/"

# server = "http://dev.tritondive.co:8000/"
# server2 = "http://dev.tritondive.co:3000/"
# server3 = "https://dev.tritondive.co/"

headers = {"accept-language":"en"}

now = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')

def checkEmail(email):
    check_body = {"email": email}
    res = requests.post(server + "apis/user/v0/checkEmail", headers=headers, data=check_body)
    if res.status_code == 200:
        print(res.text)
        if "duplicate" in res.json()["result"]:
            if res.json()['result']['duplicate'] == "n":
                return False
            else:
                return True
        else:
            return False
    else:
        return False

def get_verify_code(email):
    url = server2+"1/api/users?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy&filter={\"where\":{\"email\":\"" + email + "\"}}"
    result = requests.get(url)
    #print(result.text)
    if result.status_code == 200:
        if len(result.json()) == 1:
            code = result.json()[0]['code']
            link = server3+"apis/user/v0/activeAccount?ownerId=" + result.json()[0]['id'] + "&code=" + code
            dict = {"code": code, "link": link}
            #print(dict)
            return dict
        else:
            return {}

# 檢查是否已存在帳號，如果不是就建立
def register(email,pwd=None):
    if not checkEmail(email.lower()):
        if pwd==None:
            pwd = "123456"
        userName = email[:email.find("@")]
        register_body={"email":email.lower(),"password":pwd,"userName":userName,"deviceId": ""}
        res = requests.post(server+"apis/user/v0/register",headers=headers,data=register_body)
        if res.status_code==200:
            #time.sleep(5)
            #print(get_verify_code(email.lower()))
            url = get_verify_code(email.lower())
            url = url['link']
            res = requests.get(url, headers={"accept-language": "en"})
            print("註冊成功")
        else:
            #print(res.status_code)
            print("註冊失敗")
    else:
        print("重複email")

def login(email,pwd=None):
    if pwd == None:
        pwd = "123456"
    login_data={"email": email,"password": pwd,"deviceId": "string"}
    res = requests.post(server+"apis/user/v0/login",headers=headers,data=login_data)
    if res.status_code==200:
        result = [email,res.json()["result"]["accessToken"],res.json()["result"]["userInfo"]["ownerId"]]
    else:
        result=[email,"",""]
    return result

def buddy_request(list):
    headers["authorization"] = list[0][1]
    buddy_data = {"buddyUserId":list[1][2]}
    res = requests.post(server+"apis/buddy/v0/request",headers=headers,data=buddy_data)
    print(res.text)

def buddy_approve(list):
    headers["authorization"] = list[1][1]
    buddy_data = {"buddyUserId": list[0][2]}
    res = requests.put(server + "apis/buddy/v0/approve", headers=headers, data=buddy_data)
    print(res.text)

def buddies(group):
    for i in range(0,len(group)-1):
        for j in  range(i+1,len(group)):
            buddy_request([group[i],group[j]])
            buddy_approve([group[i], group[j]])

def change_password(email,oldpwd,newpwd):
    info = login(email,oldpwd)
    headers["authorization"]=info[1]
    pwd={"oldPassword": oldpwd,"newPassword": newpwd}
    res = requests.post(server+"apis/user/v0/changePassword",headers=headers,data=pwd)

    print(res.text)
if __name__=="__main__":

    buddy = ["yuhsuan@deepblu.com"]
    # buddy.append('test01@test.com')
    # buddy.append('test02@test.com')
    # buddy.append('test03@test.com')
    # buddy.append('test04@test.com')
    # buddy.append('test05@test.com')
    # buddy.append('test06@test.com')
    # buddy.append("wtfgmt@gmail.com")
    # buddy.append("user@test.com")
    # buddy.append("regular@test.com")
    # buddy.append("pro@test.com")
    # buddy.append("ambassador@test.com")
    # buddy.append("res@test.com")
    # buddy.append("reg_pro@test.com")
    # buddy.append("reg_amb@test.com")
    # buddy.append("reg_res@test.com")
    # buddy.append("pro_amb@test.com")
    # buddy.append("pro_res@test.com")
    # buddy.append("buddies@test.com")
    # buddy.append("Tara@test.com")
    # buddy.append("Tarie@test.com")
    # buddy.append("Tary@test.com")
    # buddy.append("Node-Tar@test.com")
    # buddy.append("madlen@deepblu.com")

    group=[]
    for i in buddy:
        register(i)
        group.append(login(i))

    print(group)
    buddies(group)