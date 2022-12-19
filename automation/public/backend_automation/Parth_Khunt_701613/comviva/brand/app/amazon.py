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


class Amazon:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'in.amazon.mShop.android.shopping',
                'appActivity': 'com.amazon.mShop.home.HomeActivity',
                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Amazon App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.ImageView[@content-desc="Select English"]').click()
            time.sleep(5)


            driver.find_element(By.ID,'in.amazon.mShop.android.shopping:id/continue_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'in.amazon.mShop.android.shopping:id/new_user').click()
            time.sleep(35)

            # self.dynamicwait(By.ID,'ap_customer_name').send_keys('manoj patel')
            # time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.EditText[contains(@text,"91")]').clear()
            # time.sleep(5)

            self.dynamicwait(By.ID, 'ap_phone_number').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'ap_password').send_keys('Zala@12345')
            time.sleep(5)

            driver.find_element(By.ID, 'continue').click()
            time.sleep(5)

            # driver.find_element(By.ID,'org.thoughtcrime.securesms:id/progress_indicator').click()
            # time.sleep(5)
            #
            # self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"OK")]').click()
            # time.sleep(5)
            #+

            # self.dynamicwait(By.ID,'org.thoughtcrime.securesms:id/verify_header')
            # time.sleep(5)

            # self.dynamicwait(By.ID,'com.amazon.mShop.android.shopping:id/new_user').click()

            driver.quit()

            print('Amazon App - Execution Completed')

            amazon_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return amazon_resultdata
        except:

            print('Amazon App - Execution Completed')

            driver.quit()

            amazon_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return amazon_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
