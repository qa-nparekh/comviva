import time
from random import choice

import phonenumbers
import pycountry
from appium import webdriver as appDriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config

from phonenumbers.phonenumberutil import (
            region_code_for_number,
        )

class Coinbase:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        email = firstname+ "143007uvc"+"gmail.com"
        password = firstname + "@1990"

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.coinbase.android',
                'appActivity': 'com.coinbase.android.MainActivity',
                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Coinbase App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Sign up")]').click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Get")]').click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Create")]').click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH,"//android.widget.EditText[contains(@text,'First Name')]").send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text,'Last Name')]").send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text,'Email address')]").send_keys(email)
            time.sleep(5)

            driver.back()

            self.dynamicwait(By.XPATH, "//android.widget.EditText[contains(@text,'Minimum 8 characters')]").send_keys(password)
            time.sleep(5)

            print('hello')

            driver.find_element(By.ID, 'acceptUserAgreement').click()
            time.sleep(5)

            print('2')

            print(driver.page_source)

            # self.dynamicwait(By.ID,'com.baobabcircle.afyapap:id/btn_confirm_language').click()
            # time.sleep(5)
            #
            # pn = phonenumbers.parse(mobile_no)
            #
            # country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
            #
            # countryname = country.name
            # print(countryname)
            #
            # self.dynamicwait(By.ID,'com.baobabcircle.afyapap:id/atv_spinner_countries').send_keys(countryname)
            # time.sleep(5)
            #
            #
            # driver.find_element(By.ID,'com.baobabcircle.afyapap:id/et_phone_number').send_keys(mobilenumber)
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH,'//android.widget.Button[@text="REQUEST VERIFICATION CODE"]').click()
            # time.sleep(5)

            driver.quit()

            print('Coinbase App - Execution Completed')

            coinbase_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return coinbase_resultdata

        except:

            print('Coinbase App - Execution Completed')

            driver.quit()

            coinbase_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return coinbase_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
