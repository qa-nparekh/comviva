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




class Spotify:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.spotify.music',
                'appActivity': 'com.spotify.music.MainActivity',
                # 'app': config.apk_path+'spotify.apk',
                'autoGrantPermissions': 'true'
            }

            print('Spotify App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"Continue with phone number")]').click()
            time.sleep(5)


            self.dynamicwait(By.ID,'com.spotify.music:id/calling_code').click()
            time.sleep(5)

            pn = phonenumbers.parse(mobile_no)

            country = pycountry.countries.get(alpha_2=region_code_for_number(pn))

            countryname = country.name
            print(countryname)

            self.dynamicwait(By.ID,'com.spotify.music:id/search_src_text').send_keys(countryname)
            time.sleep(5)

            driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+"+str(countrycode)+"')]").click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.spotify.music:id/phone_number').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'com.spotify.music:id/request_otp_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.spotify.music:id/otp_input').click()
            time.sleep(15)

            driver.quit()

            print('Spotify App - Execution Completed')

            spotify_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return spotify_resultdata

        except:

            print('Spotify App - Execution Completed')

            driver.quit()

            spotify_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return spotify_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
