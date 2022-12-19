import time

import phonenumbers
import pycountry
from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config

from phonenumbers.phonenumberutil import (
            region_code_for_number,
        )


class Gmail:

    def generateOTP(self,mobilenumber, countrycode ):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.google.android.gm',
                'appActivity': 'com.google.android.gm.welcome.WelcomeTourActivity',
                # 'app': config.apk_path+'afyapap.apk',
                'autoGrantPermissions': 'true'
            }

            print('Gmail App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            # print(driver.page_source)

            self.dynamicwait(By.ID, 'com.google.android.gm:id/welcome_tour_skip').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.google.android.gm:id/setup_addresses_add_another').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.google.android.gm:id/account_setup_label')

            self.dynamicwait(By.XPATH,'//android.view.View[contains(@text,"Create account")]').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.view.MenuItem[contains(@text,"For myself")]').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'firstName').send_keys()
            time.sleep(5)

            driver.find_element(By.ID, 'lastName').send_keys()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"Next")]').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'month').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.CheckedTextView[contains(@text,"February")]').click()
            time.sleep(5)

            driver.find_element(By.ID, 'day').send_keys()
            time.sleep(5)

            driver.find_element(By.ID, 'year').send_keys()
            time.sleep(5)

            driver.find_element(By.ID, 'gender').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.CheckedTextView[contains(@text,"Female")]').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"Next")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"Use mobile")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.Button[contains(@text,"Yes, use number")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.view.View/android.widget.Spinner').click()
            time.sleep(5)

            elemnt = self.dynamicwait(By.CLASS_NAME, 'android.widget.ListView')
            # elemnt = self.dynamicwait(By.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.ListView')

            print('2')

            location = elemnt.location
            size = elemnt.size
            w, h = size['width'], size['height']

            print(location)
            print(size)
            print(w, h)
            height = size['height'] / 2
            width = size['width']

            locationXStart = round(height * 0.90)
            locationXEnd = round(locationXStart / 2)
            loctionYEnd = round(locationXEnd / 2)

            locationYStart = round(width - 200)

            print(locationXStart)

            print(locationXEnd)

            result = False

            while (result != True):
                try:
                    result = driver.find_element(By.XPATH, "//android.view.View[contains(@text,'+" + str(countrycode) + "')]").is_displayed()
                except:
                    time.sleep(2)

                    TouchAction(driver).press(x=locationXStart, y=locationYStart).move_to(x=locationXEnd,
                                                                                          y=loctionYEnd).release().perform()
                    time.sleep(3)

            driver.find_element(By.XPATH,"//android.view.View[contains(@text,'+" + str(countrycode) + "')]").click()
            time.sleep(5)

            print('found')

            driver.find_element(By.ID,'phoneNumberId').clear()
            time.sleep()

            driver.find_element(By.ID, 'phoneNumberId').send_keys(mobilenumber)
            time.sleep()

            driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"Get code")]').click()
            time.sleep(5)

            # self.dynamicwait(By.CLASS_NAME,'android.widget.EditText')
            # time.sleep(5)

            self.dynamicwait(By.ID,'code')
            time.sleep(5)

            # pn = phonenumbers.parse(mobile_no)
            #
            # country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
            #
            # countryname = country.name
            # print(countryname)

            driver.quit()

            print('Gmail App - Execution Completed')

            gmail_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return gmail_resultdata

        except:

            print('Gmail App - Execution Completed')

            driver.quit()

            gmail_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return gmail_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
