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


class Bolt:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'ee.mtakso.client',
                # 'appActivity': 'org.thoughtcrime.securesms.MainActivity',
                'appActivity': 'ee.mtakso.client.activity.SplashHomeActivity',

                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Bolt App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID,'ee.mtakso.client:id/phoneInputField').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'ee.mtakso.client:id/phonePrefixFlag').click()
            time.sleep(5)

            # self.dynamicwait(By.ID,'ee.mtakso.client:id/hint').send_keys(countrycode)
            # time.sleep(5)
            # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Search for a country")]')
            # time.sleep(5)
            # print('hi')

            pn = phonenumbers.parse(mobile_no)

            country = pycountry.countries.get(alpha_2=region_code_for_number(pn))

            countryname = country.name
            print(countryname)

            self.dynamicwait(By.XPATH,'//android.widget.TextView[contains(@text,"Search for a country")]').send_keys(countryname)
            time.sleep(5)

            print('h3')

            driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+" + str(countrycode) + "')]")
            time.sleep(5)

            print(driver.page_source)

            # self.dynamicwait(By.ID, 'org.thoughtcrime.securesms:id/progress_indicator').click()
            # time.sleep(5)
            # self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"Continue")]').click()
            # time.sleep(5)
            #
            # self.dynamicwait(By.XPATH,'//android.widget.EditText[contains(@text,"91")]').clear()
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text,"Country code")]').send_keys(countrycode)
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH,'//android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText').clear()
            #
            # driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text,"Phone number")]').send_keys(mobilenumber)
            # time.sleep(5)
            #
            # driver.find_element(By.ID,'org.thoughtcrime.securesms:id/progress_indicator').click()
            # time.sleep(5)
            #
            # self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"OK")]').click()
            # time.sleep(5)
            #
            # self.dynamicwait(By.ID,'org.thoughtcrime.securesms:id/verify_header')
            # time.sleep(5)

            driver.quit()

            print('Bolt App - Execution Completed')

            bolt_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return bolt_resultdata

        except:

            print('Bolt App - Execution Completed')

            driver.quit()

            bolt_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return bolt_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
