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


class Skype:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.skype.raider',
                'appActivity': 'com.skype4life.MainActivity',
                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Skype App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Let")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Sign in or create")]').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'signup').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'phoneSwitch').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'PhoneCountry').click()
            time.sleep(15)

            # self.dynamicwait(By.CLASS_NAME,'android.widget.ListView')




            self.dynamicwait(By.XPATH,'//android.widget.CheckedTextView[contains(@text,"+91")]')
            time.sleep(5)

            driver.find_element(By.ID,'MemberName').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID,'iSignupAction').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'PasswordInput').send_keys()
            time.sleep(5)

            driver.find_element(By.ID,'iSignupAction').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'FirstName').send_keys('arya')
            time.sleep(5)

            self.dynamicwait(By.ID,'LastName').send_keys('runbua')
            time.sleep(5)

            driver.find_element(By.ID, 'iSignupAction').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'Country').click()
            time.sleep(15)

            # / hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.ListView

            self.dynamicwait(By.ID, 'BirthMonth').click()
            time.sleep(5)

            # / hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.ListView

            self.dynamicwait(By.ID, 'BirthDay').click()
            time.sleep(15)

            # / hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.ListView

            self.dynamicwait(By.ID, 'BirthYear').send_keys('1995')
            time.sleep(5)

            self.dynamicwait(By.ID,'VerificationCode')
            time.sleep(5)


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

            print('Skype App - Execution Completed')

            skype_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return skype_resultdata

        except:

            print('Skype App - Execution Completed')

            driver.quit()

            skype_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return skype_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
