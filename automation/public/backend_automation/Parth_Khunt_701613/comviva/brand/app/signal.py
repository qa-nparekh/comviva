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


class Signal:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'org.thoughtcrime.securesms',
                # 'appActivity': 'org.thoughtcrime.securesms.MainActivity',
                'appActivity': 'org.thoughtcrime.securesms.ShortcutLauncherActivity',

                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Signal App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            # self.dynamicwait(By.ID, 'org.thoughtcrime.securesms:id/progress_indicator').click()
            # time.sleep(5)
            self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"Continue")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.EditText[contains(@text,"91")]').clear()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text,"Country code")]').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText').clear()

            driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text,"Phone number")]').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID,'org.thoughtcrime.securesms:id/progress_indicator').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"OK")]').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'org.thoughtcrime.securesms:id/verify_header')
            time.sleep(5)

            driver.quit()

            print('Signal App - Execution Completed')

            signal_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return signal_resultdata

        except:

            print('Signal App - Execution Completed')

            driver.quit()

            signal_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return signal_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
