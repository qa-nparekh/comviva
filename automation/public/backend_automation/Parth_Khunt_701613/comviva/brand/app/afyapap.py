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


class Afyapap:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.baobabcircle.afyapap',
                'appActivity': 'com.baobabcircle.afyapap.ui.activities.NavigationActivity',
                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Afyapap App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'com.baobabcircle.afyapap:id/tv_skip').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.baobabcircle.afyapap:id/btn_confirm_language').click()
            time.sleep(5)

            pn = phonenumbers.parse(mobile_no)

            country = pycountry.countries.get(alpha_2=region_code_for_number(pn))

            countryname = country.name
            print(countryname)

            self.dynamicwait(By.ID,'com.baobabcircle.afyapap:id/atv_spinner_countries').send_keys(countryname)
            time.sleep(5)


            driver.find_element(By.ID,'com.baobabcircle.afyapap:id/et_phone_number').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.Button[@text="REQUEST VERIFICATION CODE"]').click()
            time.sleep(5)

            driver.quit()

            print('Afyapap App - Execution Completed')

            afyapap_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return afyapap_resultdata

        except:

            print('Afyapap App - Execution Completed')

            driver.quit()

            afyapap_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return afyapap_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
