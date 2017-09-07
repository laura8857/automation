# -- coding: utf-8 --

from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import time
import datetime
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class action:
    def __init__(self):
        pass

    def setup(self):
        '''edge driver test'''
        '''self.driver = webdriver.Remote('http://172.16.203.152:4444/wd/hub',webdriver.DesiredCapabilities.EDGE.copy())'''
        ''',executable_path='C:\\Users\\IEUser\\Downloads\\MicrosoftWebDriver.exe')'''

        # self.driver = webdriver.Firefox(executable_path=r'/Users/huweiting/Desktop/auto_test/automation/Social_Web/geckodriver_v0_17_0')

        self.driver = webdriver.Chrome(
             executable_path=r'/Users/huweiting/Desktop/auto_test/automation/Social_Web/chromedriver_2_29')
        # self.driver = webdriver.Safari(executable_path=r'/usr/bin/safaridriver')

        self.baseURL = "https://test.deepblu.com"

        # root.withdraw()
        screen_width = tk.Tk().winfo_screenwidth()
        screen_height = tk.Tk().winfo_screenheight()
        print(screen_width, screen_height)

        self.driver.set_window_size(screen_width, screen_height)
        self.driver.set_window_position(0, 0)

        print(self.driver.get_window_size())
        print("setup\n")

    # 這邊都是為了 sign up 驗證做的
    def get_verify_code(self, email):
        url = "http://test.tritondive.co:3000/1/api/users?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy&filter={\"where\":{\"email\":\"" + email + "\"}}"
        result = requests.get(url)
        if result.status_code == 200:
            print(len(result.json()))

            print(url)
            if result.json():
                code = result.json()[0]['code']
                link = "https://test.tritondive.co/apis/user/v0/activeAccount?ownerId=" + result.json()[0][
                    'id'] + "&code=" + code
                dict = {"code": code, "link": link}
                return dict
            else:
                return {}

    def verify_by_link(self, url):
        json = {"accept-language": "en"}
        res = requests.get(url, headers=json)

    def signup_exist_email(self):
        self.driver.get(self.baseURL + "/discover/live")
        self.waitElement(5, (By.CSS_SELECTOR, 'button.styles__sign-up___3_fnX'))
        self.driver.find_element_by_css_selector("button.styles__sign-up___3_fnX").click()
        self.waitElement(5, (By.XPATH, '//div[@data-db-toolbox="dialog"]'))  # 等 dialog 跳出來
        self.driver.find_element_by_name('email').send_keys('user1@deepblu.com')

        # 驗證有重複電郵的提示訊息
        # self.VerifiedElement(By.XPATH, '//div[text()="此電郵已重複輸入。"]') 不知道為什麼不能用，先跳過
        self.VerifiedElement(By.XPATH, '/html/body/div[13]/div/div[2]/section/form/div/div[3]')

    # 我快不行了，不同語言的 xpath 居然不同．此處以中文為主
    def signUpEmail(self, next_step):
        self.driver.get(self.baseURL + "/discover/live")

        account = 'iris' + time.strftime("%y%m%d%H%M%S")
        email = account + '@deepblu.com'
        print(email)
        #確定網站load 成功，抓'馬上註冊'的元件
        self.waitElement(5, (By.CSS_SELECTOR, 'button.styles__sign-up___3_fnX'))
        self.driver.find_element_by_css_selector("button.styles__sign-up___3_fnX").click()
        self.waitElement(5, (By.XPATH, '//div[@data-db-toolbox="dialog"]'))  # 等 dialog 跳出來
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('password').send_keys('a123456')

        self.waitElementClickable(6, (By.XPATH, '//button[text()="註冊"]'))
        self.driver.find_element_by_xpath('//button[text()="註冊"]').click()

        self.VerifiedElement(By.XPATH, '//div[@data-db-toolbox="dialog"]')

        if next_step == 'verify':
            print(email)
            # {"code":"1234","link":"http:XXXXXXXXX"} 
            url = {}
            url = self.get_verify_code(email)
            self.sleep(5)
            self.verify_by_link(url['link'])

            self.waitElement(15, (By.XPATH, '//button[text()="稍候再做"]'))
            self.driver.find_element_by_xpath('//button[text()="稍候再做"]').click()
        elif next_step == 'verify_edit_profile':
            url = {}
            url = self.get_verify_code(email)
            self.sleep(5)
            self.verify_by_link(url['link'])

            self.waitElement(15, (By.XPATH, '//button[text()="編輯個人檔案"]'))
            self.driver.find_element_by_xpath('//button[text()="編輯個人檔案"]').click()
            self.VerifiedElement(By.XPATH, '//span[@data-db-toolbox="list-item-text"][text()="編輯個人檔案"]')
        elif next_step == 'resend':
            self.waitElement(5, (By.XPATH, '//a[text()="重發Email"]'))
            self.driver.find_element_by_xpath('//a[text()="重發Email"]').click()
            self.sleep(2)
            #重寄視窗
            self.VerifiedElement(By.ID, 'swal2-title')
            # self.driver.find_element_by_xpath('//button[text()="OK"]').click()
        elif next_step == 'changeEmail':
            self.waitElement(5, (By.XPATH, '//a[text()="更改Email"]'))
            self.driver.find_element_by_xpath('//a[text()="更改Email"]').click()
            new_email = 'iris' + time.strftime("%y%m%d%H%M%S") + '@deepblu.com'
            self.driver.find_element_by_name('email').send_keys(new_email)
            self.waitElementClickable(6, (By.XPATH, '//button[text()="送出"]'))
            self.driver.find_element_by_xpath('//button[text()="送出"]').click()

            # 更改 email 後試試看認證是否會成功
            url = self.get_verify_code(new_email)
            self.sleep(5)
            self.verify_by_link(url['link'])
            print('ok before')
            self.driver.find_element_by_xpath('//button[text()="OK"]').click()
            print('bg before')
            # self.VerifiedElement(By.XPATH,'//div[@class="bg"]')
            # print('bg after')

        elif next_step == 'notNow':
            self.waitElement(5, (By.XPATH, '//button[text()="稍候再做"]'))
            self.driver.find_element_by_xpath('//button[text()="稍候再做"]').click()
            self.driver.get(self.driver.current_url)  # reload page
            self.VerifiedElement(By.XPATH, '//div[@data-db-toolbox="dialog"]')

    def login(self):
        self.driver.get(self.baseURL + "/discover/live")
        self.waitElementClickable(30, (By.CSS_SELECTOR, 'button.styles__login___2Xloe'))
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.styles__login___2Xloe')))

        print("login" + str(self.driver.find_element_by_css_selector('button.styles__login___2Xloe').is_enabled()))
        # self.sleep(2)
        # print('click')
        self.driver.find_element_by_css_selector("button.styles__login___2Xloe").click()

        print('click-after')
        self.waitElement(8, (By.CSS_SELECTOR,
                             'body > div:nth-child(22) > div > div.theme__dialog___3pej6.styles__dialog___3pFYp.theme__normal___1Fuy1.theme__active___2gTq9.styles__system-dialog___1c3wz > section'))
        self.driver.find_element_by_name("email").click()
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("iris+2@deepblu.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.theme__button___Ewr9O:nth-child(8)')))

        self.driver.find_element_by_css_selector("button.theme__button___Ewr9O:nth-child(8)").click()

        print("login\n")

    def logout(self):
        self.driver.find_element_by_link_text("登出").click()
        print(self.baseURL + "/logout")

    def doesWebElementExist(self, By, element):
        try:
            self.driver.find_element(By, element)
            return True
        except Exception as e:
            print(e)
            return False

    def sleep(self, second):
        time.sleep(second)

    def waitElement(self, second, selector):
        try:
            WebDriverWait(self.driver, second).until(EC.visibility_of_element_located(selector))
        except Exception as e:
            print("waitNoElement" + str(selector))

    def waitElementClickable(self, second, selector):
        try:
            WebDriverWait(self.driver, second).until(EC.element_to_be_clickable(selector))
        except Exception as e:
            print('Element unclickable')

    def waitUntilInvisibility(self, second, selector):
        WebDriverWait(self.driver, second).until(EC.invisibility_of_element_located(selector))

    def dropdown(self):
        self.waitElement(5, (
            By.CSS_SELECTOR, "div.styles__triangle___3lyre"))
        self.driver.find_element_by_css_selector("div.styles__triangle___3lyre").click()

    def SwichFrame(self):
        self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="toolbox-content"]/span/iframe'))

    def goFeaturedPage(self):
        self.driver.get(self.baseURL + "/discover/trending")

    def goTermsConditions(self):
        self.driver.get(self.baseURL + "/terms-of-condition")

    def goGuidelines(self):
        self.driver.get(self.baseURL + "/guidelines")
        print(self.baseURL + "/guidelines")

    def goProfileTimeline(self):
        self.waitElement(9, (By.CSS_SELECTOR, ".styles__user___14AnR"))
        self.sleep(3)
        self.driver.find_element_by_css_selector('.styles__user___14AnR').click()
        print('Timeline')

    def postText(self):
        self.waitElement(5, (By.NAME, 'content'))
        self.driver.find_element_by_name('content').send_keys(
            '[AutoTest]\n測試訊息' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.waitElementClickable(10, (By.XPATH, '//button[@type="submit"]'))
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        # 等確定 post 出去才能 logout
        if (self.driver.find_element_by_xpath('//button[@type="submit"]').text != 'POST'):
            self.sleep(3)

    # 不能用喔哭哭，因為但難判斷上傳完了沒
    def postPhoto(self):
        self.driver.find_element_by_xpath('//button/i[@class="dbi-image styles__ibtn___1oNE4"]').click()
        self.waitElement(3, (By.XPATH, '(//input[@type="file"])[2]'))
        self.driver.find_element_by_xpath('(//input[@type="file"])[2]').send_keys(
            u'/Users/iris/Desktop/測試資料/pic/71.jpg')
        self.sleep(5)  # 為了等上傳圖 load 完
        self.driver.find_element_by_name('content').send_keys(
            '[AutoTest]\n測試發圖' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        if (self.driver.find_element_by_xpath('//button[@type="submit"]').text != 'POST'):
            self.sleep(3)

    def postVideo(self):
        self.driver.find_element_by_xpath('//button/i[@class="dbi-video styles__ibtn___1oNE4"]').click()
        self.waitElement(3, (By.XPATH, '(//input[@type="file"])[1]'))
        self.driver.find_element_by_xpath('(//input[@type="file"])[1]').send_keys(
            '/Users/iris/Desktop/測試資料/影片/安心亞《別再撐了》官方完整版Official Music Video.mp4')

        self.waitUntilInvisibility(70, (By.XPATH,
                                        '//*[@id="toolbox-content"]/div/div/div[2]/div[2]/div/ul/div/div[1]/form/div/div[3]/div/div/div/div/div[2]'))
        self.driver.find_element_by_name('content').send_keys(
            '[AutoTest]\n測試影片' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        if (self.driver.find_element_by_xpath('//button[@type="submit"]').text != 'POST'):
            self.sleep(3)


            # //*[@id="toolbox-content"]/div/div/div[2]/div[2]/div/ul/div/div[1]/form/div/div[3]/div/div/div/div/div[1]/div/div video上傳％數

    def goAllGroupsPage(self):
        self.driver.get(self.baseURL + "/community/groups/all")
        print(self.baseURL + "/community/groups/all")
        print("All group\n")

    def goYourGroupPage(self):
        self.driver.get(self.baseURL + "/community/groups/your")
        print(self.baseURL + "/community/groups/your")
        print("Your group\n")

    def ChangeGroupPhoto(self):
        print('ChangeGroupPhoto')
        self.driver.find_element_by_css_selector("div.styles---img---M7Mt9 > input[type=\"file\"]").clear()
        self.driver.find_element_by_css_selector("div.styles---img---M7Mt9 > input[type=\"file\"]").send_keys(
            "/Users/iris/Desktop/中文.jpg")
        self.driver.find_element_by_css_selector("button.styles---edit---QaO8m").click()
        self.waitUntilInvisibility(10, (By.XPATH, "//*[@id='app']/div/div/div/div[1]/div/div"))

        self.waitUntilInvisibility(10, (By.XPATH, "//*[@id='vue-app']/div/div[2]/img"))
        # print(self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[4]/div[1]/div[1]/div").is_displayed())

        # self.sleep(10)
        self.getScreenShot('ChangeGroupPhoto')
        '''
        #將圖片換回原本的
        self.ClickGroupSetting()
        self.driver.find_element_by_css_selector("div.styles---img---M7Mt9 > input[type=\"file\"]").clear()
        self.driver.find_element_by_css_selector("div.styles---img---M7Mt9 > input[type=\"file\"]").send_keys(
            "/Users/iris/Desktop/測試資料/pic/640_6a8156aa5112b39c6183d039af97ea25.jpg")
        self.driver.find_element_by_css_selector("button.styles---edit---QaO8m").click()
        self.waitUntilInvisibility(5, (By.XPATH, "//*[@id='app']/div/div/div/div[1]/div/div"))'''

        '''#以下是用上傳圖片的網址作為判斷依據
        photo_address=str(self.driver.find_element_by_css_selector("#app > div > div > div > div.styles---group---2qvNC > div.styles---leftPanel---3J95h > div.styles---groupImg---1Q5wG > div").get_attribute("style"))
        photo_address=photo_address.split('.')
        #由於陣列頭一個元素索引為0,因此倒數第二個應該 -2, 如果要用上傳時間做驗證可以啟用這塊
        photo_address=photo_address[len(photo_address) - 2].split('/')
        print(photo_address)
        print(str(datetime.datetime.now()).split('-'))'''

    def goUserOwnGroup(self):
        self.waitElement(4, (By.XPATH, "//*[contains(text(), '新建群組測試')]/.."))
        self.driver.find_element_by_xpath("//*[contains(text(), '新建群組測試')]/..").click()

    def ClickGroupSetting(self):
        self.scrollPageToTop()
        self.waitElement(4, (By.XPATH, "//*[contains(text(), 'Setting')]/../div[1]"))
        self.driver.find_element_by_xpath("//*[contains(text(), 'Setting')]/../div[1]").click()

    def getScreenShot(self, filename):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        currentPath = "/Users/iris/Desktop/AutoTestScreenshot/" + date

        try:
            self.driver.get_screenshot_as_file(currentPath + filename + ".jpg")
            print("save snapshot path is " + currentPath)
        except Exception as e:
            print("Can't save screenshot")

    def goNewTab(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def goMainTab(self):
        self.driver.switch_to_window(self.driver.window_handles[0])

    def scrollPage(self):
        # print(self.driver.find_element_by_xpath('/html/body').size)
        # print(self.driver.find_element_by_xpath('//*[@id="content-block"]/div/div').size)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # print(self.VerifiedElement(By.TAG_NAME,'iframe'))

        self.waitElement(5, (By.TAG_NAME, 'iframe'))
        self.driver.find_element_by_tag_name('iframe').send_keys(Keys.CONTROL + Keys.END)

        '''if(self.doesWebElementExist(By.TAG_NAME,'iframe')):
            print('存在')
            self.driver.find_element_by_tag_name('iframe').send_keys(Keys.CONTROL + Keys.END)
        else:
            print("不存在")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")'''

        print('scrolldown')

    def scrollPageToTop(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def VerifiedElement(self, By, element):
        try:
            self.driver.find_element(By, element)
            print('[VerifiedElement] verified ok ' + str(By) + str(element))
            return "pass"
        except Exception as e:
            print('[VerifiedElement] assert failed ' + str(By) + str(element))
            return "assert failed."

    def quit_exit(self):
        self.driver.quit()
