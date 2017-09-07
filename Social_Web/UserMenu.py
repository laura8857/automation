# -- coding: utf-8 --

from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import tkinter as tk

from Social_Web.LittleFunction import *

class UserMenu:
    action = action()
    def __init__(self):
        pass

    #靜態頁面系列
    def ShowTermAndCondition(self):
        self.action.setup()
        self.action.goTermsConditions()
        self.action.sleep(5)
        self.action.goNewTab()
        self.action.getScreenShot("goTermsConditionsTop")
        self.action.scrollPage()
        self.action.getScreenShot("goTermsConditionsBottom")
        self.action.quit_exit()

    def ShowGuidelines(self):
        self.action.setup()
        self.action.goGuidelines()
        #self.action.SwichFrame()
        self.action.getScreenShot("ShowGuidelinesTop")
        self.action.sleep(2)
        self.action.scrollPage()
        self.action.getScreenShot("ShowGuidelinesBottom")
        self.action.quit_exit()


    #sign up 系列
    # nextstep (verify | resend | changeEmail | notNow)
    def Signup_email(self):
        self.action.setup()
        self.action.signUpEmail('verify')
        self.action.dropdown()
        self.action.logout()
        self.action.quit_exit()

    def Signup_notNow(self):
        self.action.setup()
        self.action.signUpEmail('notNow')
        self.action.quit_exit()

    def Signup_reSend(self):
        self.action.setup()
        self.action.signUpEmail('resend')
        self.action.quit_exit()

    def Signup_changeEmail(self):
        self.action.setup()
        self.action.signUpEmail('changeEmail')
        self.action.quit_exit()

    def Signup_existEmail(self):
        self.action.setup()
        self.action.signup_exist_email()
        self.action.quit_exit()

    def Signup_editProfile(self):
        self.action.setup()
        self.action.signUpEmail('verify_edit_profile')
        self.action.quit_exit()

    #post 系列
    def PostText(self):
        self.action.setup()
        self.action.login()
        self.action.goProfileTimeline()
        self.action.sleep(2)
        self.action.postText()
        self.action.dropdown()
        self.action.logout()
        self.action.quit_exit()

    def PostPhoto(self):
        self.action.setup()
        self.action.login()
        self.action.goProfileTimeline()
        self.action.sleep(2)
        self.action.postPhoto()
        self.action.dropdown()
        self.action.logout()
        self.action.quit_exit()

    def PostVideo(self):
        self.action.setup()
        self.action.login()
        self.action.goProfileTimeline()
        self.action.sleep(2)
        self.action.postVideo()
        self.action.dropdown()
        self.action.logout()
        self.action.quit_exit()

    def ChangeGroupAvatar(self):
        self.action.setup()
        self.action.login()
        self.action.goYourGroupPage()
        self.action.goUserOwnGroup()
        self.action.ClickGroupSetting()
        self.action.ChangeGroupPhoto()
        self.action.dropdown()
        self.action.logout()
        self.action.driver.quit()