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



class Truecaller:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.truecaller',
                'appActivity': 'com.truecaller.ui.TruecallerInit',
                # 'app': config.apk_path+'trucaller.apk',
                'autoGrantPermissions': 'true'
            }

            print('Trucaller App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'nextButton').click()
            time.sleep(5)


            # self.dynamicwait(By.ID,'android:id/button1').click()
            # time.sleep(5)


            # self.dynamicwait(By.XPATH, '// android.widget.Button[ @ content - desc = "India"]').click()
            # time.sleep(5)

            self.dynamicwait(By.ID, 'countrySpinner').click()
            time.sleep(5)

            pn = phonenumbers.parse(mobile_no)

            country = pycountry.countries.get(alpha_2=region_code_for_number(pn))

            countryname = country.name
            print(countryname)

            driver.find_element(By.ID,'searchEditText').send_keys(countryname)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.TextView[contains(@text,' + str(countrycode) + ')]').click()
            time.sleep(5)

            # driver.find_element(By.XPATH, '//android.widget.TextView[contains(@text,' + str(countryname) + ')]').click()
            # time.sleep(5)

            driver.find_element(By.ID, 'numberField').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'nextButton').click()
            time.sleep(5)

            # self.dynamicwait(By.ID,'button1').click()
            # time.sleep(5)

            self.dynamicwait(By.ID,'nextButton').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.TextView[@text="Calling to confirm your number"]')
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.TextView[@text="Please enter your Truecaller confirmation code"]')
            time.sleep(5)
            print('h2')

            self.dynamicwait(By.XPATH,'//android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.Button').click()
            time.sleep(5)

            # self.dynamicwait(By.ID, 'button_text').click()
            # time.sleep(5)

            self.dynamicwait(By.ID, 'confirmation_field')
            time.sleep(5)

            driver.quit()

            print('Trucaller App - Execution Completed')

            truecaller_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return truecaller_resultdata

        except:
            print('Trucaller App - Execution Completed')

            driver.quit()

            truecaller_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return truecaller_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
