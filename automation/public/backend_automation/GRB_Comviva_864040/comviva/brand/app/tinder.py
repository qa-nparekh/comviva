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


class Tinder:

    def generateOTP(self, mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.tinder',
                'appActivity': 'com.tinder.activities.LoginActivity',
                # 'app': config.apk_file_path+tinder.apk,
                'autoGrantPermissions': 'true'
            }

            print('Tinder App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"More Options")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.Button[contains(@text,"LOG IN WITH PHONE NUMBER")]').click()
            time.sleep(5)

            self.dynamicwait(By.ID, "countryCodeInputView").click()
            time.sleep(5)

            driver.find_element(By.ID,'countryCodeSearch').send_keys(countrycode)
            time.sleep(5)


            driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text,'+" + str(countrycode) + "')]").click()
            time.sleep(5)

            driver.find_element(By.ID, 'phoneNumberInputView').send_keys(mobilenumber)
            time.sleep(5)


            driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"CONTINUE")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.LinearLayout/android.widget.EditText[1]').click()
            time.sleep(5)

            driver.quit()

            print('Tinder App - Execution Completed')

            tinder_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}
            return tinder_resultdata

        except:
            print('Tinder App - Execution Completed')

            driver.quit()

            tinder_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}
            return tinder_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
