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


class Yahoo:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.yahoo.mobile.client.android.mail',
                'appActivity': 'com.yahoo.mobile.client.android.mail.activity.MainActivity',
                # 'appActivity': 'com.yahoo.mail.activities.MainPlusPlusActivity',

                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Yahoo App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'com.yahoo.mobile.client.android.mail:id/create_account_link').click()
            time.sleep(30)


            print(driver.page_source)

            print('hi')

            # self.dynamicwait(By.XPATH,'//android.widget.EditText[contains(@text,"91")]').clear()
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text,"Country code")]').send_keys()
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text,"Country code")]').clear()
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text,"Phone number")]').send_keys()
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

            print('Yahoo App - Execution Completed')

            yahoo_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return yahoo_resultdata

        except:

            print('Yahoo App - Execution Completed')

            driver.quit()

            yahoo_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return yahoo_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
