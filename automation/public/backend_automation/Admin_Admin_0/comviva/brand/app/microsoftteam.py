import time

import phonenumbers
import pycountry
from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config

from phonenumbers.phonenumberutil import (
            region_code_for_number,
        )

class Microsoftteam:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.microsoft.teams',
                'appActivity': 'com.microsoft.skype.teams.Launcher',
                # 'app': config.apk_path+'spotify.apk',
                'autoGrantPermissions': 'true'
            }

            print('Microsoftteam App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"No account? Create one for free")]').click()
            # time.sleep(5)

            self.dynamicwait(By.ID,'com.microsoft.teams:id/edit_email').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.Button[contains(@text,"")]').click()
            time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.Button[contains(@text,"Sign in or create account")]').click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH,"//android.widget.Button[contains(@text,'Personal')]").click()
            # time.sleep(5)

            # self.dynamicwait(By.ID,'phoneSwitch').click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[1]/android.view.View").click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.Button[contains(@text,"Use a phone number instead")]').click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Use a phone number instead")]').click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.view.View[contains(@text,"Use a phone number instead")]').click()
            time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.Button[contains(@text,"Individual accoun")]').click()
            # time.sleep(5)

            print(driver.page_source)

            # pn = phonenumbers.parse(mobile_no)
            #
            # country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
            #
            # countryname = country.name
            # print(countryname)
            #
            # self.dynamicwait(By.ID,'com.spotify.music:id/search_src_text').send_keys(countryname)
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+"+str(countrycode)+"')]").click()
            # time.sleep(5)
            #
            # self.dynamicwait(By.ID,'com.spotify.music:id/phone_number').send_keys(mobilenumber)
            # time.sleep(5)
            #
            # driver.find_element(By.ID, 'com.spotify.music:id/request_otp_button').click()
            # time.sleep(5)
            #
            # self.dynamicwait(By.ID,'com.spotify.music:id/otp_input').click()
            # time.sleep(15)

            driver.quit()

            print('Microsoftteam App - Execution Completed')

            microsoftteam_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return microsoftteam_resultdata

        except:

            print('Microsoftteam App - Execution Completed')

            driver.quit()

            microsoftteam_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return microsoftteam_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
