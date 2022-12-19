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


class Viber:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.viber.voip',
                'appActivity': 'com.viber.voip.WelcomeActivity',
                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Viber App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)


            self.dynamicwait(By.XPATH,'//android.widget.Button[contains(@text,"Start now")]').clear()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.viber.voip:id/registration_code_field').clear()
            time.sleep(5)

            self.dynamicwait(By.ID, 'com.viber.voip:id/registration_code_field').send_keys(countrycode)
            time.sleep(5)


            driver.find_element(By.ID,'com.viber.voip:id/registration_phone_field').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'com.viber.voip:id/btn_continue').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.viber.voip:id/yes_btn').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.viber.voip:id/view_with_description_main_view_id')
            time.sleep(5)

            driver.quit()

            print('Viber App - Execution Completed')

            viber_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return viber_resultdata

        except:

            print('Viber App - Execution Completed')

            driver.quit()

            viber_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return viber_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
