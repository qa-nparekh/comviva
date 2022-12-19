
# android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View[3]
# android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View[5]
# android.view.ViewGroup/android.view.ViewGroup[3]
# android.view.ViewGroup[2]/android.view.View[2]
# android.view.ViewGroup[1]/android.widget.MultiAutoCompleteTextView
# /android.view.ViewGroup[1]/android.view.ViewGroup[2]
# android.view.ViewGroup[4]/android.view.ViewGroup[7]
# android.view.ViewGroup[4]/android.view.ViewGroup[2]
# android.view.ViewGroup[4]/android.view.View[4]
# android.view.ViewGroup[4]/android.widget.MultiAutoCompleteTextView

import time

from appium import webdriver as appDriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class SnapChat:

    def generateOTP(self, countrycode, mobilenumber):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        password = firstname + "@2004"

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.facebook.lite',
                'appActivity': 'com.facebook.lite.MainActivity',
                # 'app': config.apk_path+'facebooklite.apk',
                'autoGrantPermissions': 'true'
            }

            print('FacebookLite App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, 'android.view.ViewGroup[1]/android.view.ViewGroup[4]').click()
            time.sleep(5)


            self.dynamicwait(By.XPATH, 'android.view.ViewGroup[3]/android.view.ViewGroup[2]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, 'android.view.ViewGroup[1]/android.widget.MultiAutoCompleteTextView[1]').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.XPATH, 'android.view.ViewGroup[1]/android.widget.MultiAutoCompleteTextView[2]').send_keys(lastname)
            time.sleep(5)

            self.dynamicwait(By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[2]").click()


            self.dynamicwait(By.XPATH, 'android.view.ViewGroup[3]/android.widget.MultiAutoCompleteTextView').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, 'android.view.ViewGroup[3]/android.view.ViewGroup[2]').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, 'android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View[1]').click()
            time.sleep(25)

            self.dynamicwait(By.ID, 'password_form_field').send_keys(password)
            time.sleep(20)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"Continue\"]').click()
            time.sleep(10)

            try:
                driver.find_element(By.ID, 'com.snapchat.android:id/signup_with_phone_instead').click()
                time.sleep(5)

            except:

                print("Not found - signup_with_phone_instead")

            self.dynamicwait(By.ID, 'top_country_code_display_textview').click()
            time.sleep(5)

            driver.find_element(By.ID, 'input_field_edit_text').send_keys(countrycode)
            time.sleep(5)


            driver.find_element(By.XPATH, "//javaClass[contains(@text," + str(countrycode) + ")]").click()
            time.sleep(5)

            driver.find_element(By.ID, 'bottom_phone_form_field').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'bottom_phone_form_field').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"Continue\"]').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.snapchat.android:id/code_field')
            time.sleep(5)

            driver.quit()

            print('PASSED')

            instagramlite_resultdata = {"First Name": firstname, "Last Name": lastname, "Password": password,
                                   "Message": 'OTP generated successfully'}

            return instagramlite_resultdata

        except:

            print('FacebookLite App - Execution Completed')

            driver.quit()

            instagramlite_resultdata = {"First Name": firstname, "Last Name": lastname, "Password": password,
                                   "Message": 'Failed to generate OTP'}

            return instagramlite_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
