# -*- coding: utf-8 -*-
# @Time    : 2017/3/10 下午3:16
# @Author  : Yuhsuan
# @File    : remove_facebook_connect.py
# @Software: PyCharm Community Edition

import pymongo
from datetime import datetime


global current_time
current_time = datetime.now().strftime("%Y%m%d%H%M%S")


# rename the email from AAA@AAA.com to AAAYYYYMMDDHHMMSS@AAA.com
def rm_email(email):
    # now = datetime.now().strftime("%Y%m%d%H%M%S")
    tmp = email.split("@")
    # new_mail = tmp[0]+now+'@'+tmp[1]
    # new_mail = ('Removed_via_QA_'+now+'@'+tmp[1])
    # new_mail = ('Removed_via_QA_'+now)
    new_mail = ('Removed_via_QA_'+current_time)


# update to mongodb
    client = pymongo.MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        db.user.update_one({"email": email}, {"$set": {"status": 'block'}})
        db.user.update_one({"email": email}, {"$set": {"email": new_mail}})
        if db.user.find_one({"email": email}):
            print("Please check DB, the email can't be changed")
        else:
            print("The email already modify to "+new_mail)
    else:
        print("The mail "+email+" can't be found.")
    client.close()


# rename Facebook connection
def rm_fb(email):
    client = pymongo.MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu
    # now = datetime.now().strftime("%Y%m%d%H%M%S")
    tmp = email.split("@")
    # new_mail = ('qa_removed_'+now+'@'+tmp[1])
    # new_mail = ('Removed_via_QA_'+now)
    new_mail = ('Removed_via_QA_'+current_time)

    if db.socialId.find_one({"email": email}):
        # db.socialId.delete_one({"email": email})
        db.socialId.update_one({"email": email}, {"$set": {"email": new_mail}})
        if db.socialId.find_one({"email": email}):
            print("Please check DB, the fb can't be changed")
        else:
            print("The FaceBook account was change to " + new_mail)
    else:
        print("The FaceBook account "+email+" can't be found.")

    client.close()


def mo_email(oemail, nemail):
    tmp = oemail.split("@")

# update to mongodb
    client = pymongo.MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": oemail}):
        db.user.update_one({"email": oemail}, {"$set": {"email": nemail}})
        if db.user.find_one({"email": oemail}):
            print("Please check DB, the email can't be changed")
        else:
            print("The email already modify to "+nemail)
    else:
        print("The mail "+oemail+" can't be found.")

    if db.socialId.find_one({"email": oemail}):
        # db.socialId.delete_one({"email": email})
        db.socialId.update_one({"email": oemail}, {"$set": {"email": nemail}})
        if db.socialId.find_one({"email": oemail}):
            print("Please check DB, the fb can't be changed")
        else:
            print("The FaceBook account was change to " + nemail)
    else:
        print("The FaceBook account "+oemail+" can't be found.")

    client.close()


if __name__ == "__main__":
    oemail = 'jesse+201703171730@deepblu.com'
    nemail = 'je@dp.com'
    mo_email(oemail, nemail)
    # rm_email("jesse+201703171730@deepblu.com")
    # rm_fb("jesse+201703171730@deepblu.com")
