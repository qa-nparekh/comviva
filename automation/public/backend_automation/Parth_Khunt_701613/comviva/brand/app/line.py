import time

import phonenumbers
import pycountry
from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config

from phonenumbers.phonenumberutil import (
            region_code_for_number,
        )



class Line:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = '+'+str(countrycode) + str(mobilenumber)


        try:
            desired_caps = {
                'deviceName': config.udid,
                'platformName': 'android',
                'appPackage': 'jp.naver.line.android',
                'appActivity': 'jp.naver.line.android.activity.SplashActivity',
                # "app": config.apk_path+'line.apk'
            }

            print('Line App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)

            self.dynamicwait(By.XPATH, '//android.widget.TextView[4]').click()
            time.sleep(5)

            try:
                self.dynamicwait(By.ID, 'common_dialog_ok_btn').click()
                time.sleep(5)
                print(mobilenumber)
                print(countrycode)

                self.dynamicwait(By.ID,"jp.naver.line.android.registration:id/country_code").click()
                time.sleep(5)

                pn = phonenumbers.parse(mobile_no)
                print('1')

                country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
                print('2')

                countryname = country.name

                print(countryname)
                print("//android.widget.TextView[contains(@text," + str(countryname) + ")]")

                result = False
                print('before')
                while (result != True):
                    print('after')

                    try:
                        result = driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text,'Algeria')]").is_displayed()
                        time.sleep(5)
                        print(result)

                    except:
                        time.sleep(2)
                        print('touch action')
                    # TouchAction(driver).press(x=551, y=978).move_to(x=557, y=710).release().perform()

                    # TouchAction(driver).press(x=514, y=1176).move_to(x=523, y=611).release().perform()
                    # time.sleep(5)
                    actions = TouchAction(driver)
                    actions.press(x=514, y=1176)
                    actions.move_to(x=523, y=611)
                    actions.release()
                    actions.perform()

                    print('after scroll')

                self.dynamicwait(By.XPATH, "//android.widget.TextView[contains(@text,'Algeria')]").click()
                time.sleep(5)

                print('afterb selction')

                # self.dynamicwait(By.ID, 'clear_text').click()
                # time.sleep(5)

                driver.find_element(By.ID, 'edit_text').send_keys(mobilenumber)
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Next"]').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'common_dialog_ok_btn').click()
                time.sleep(5)

                self.dynamicwait(By.XPATH,'//android.view.ViewGroup[@content-desc="Verification code"]/android.widget.LinearLayout/android.widget.EditText[1]').click()
                time.sleep(5)

                driver.quit()

                print('Line App - Execution Started')

                line_resultdata = {"Number": mobile_no, "message": "OTP generated successfully"}
                return line_resultdata

            except:

                self.dynamicwait(By.ID, "jp.naver.line.android.registration:id/country_code").click()
                time.sleep(5)

                pn = phonenumbers.parse(mobile_no)
                print('1')

                country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
                print('2')

                countryname = country.name

                print(countryname)
                print("//android.widget.TextView[contains(@text," + str(countryname) + ")]")
                result = False

                while (result != True):
                    try:
                        result = driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'India')]").is_displayed()
                        time.sleep(5)
                    except:
                        time.sleep(2)

                    # TouchAction(driver).press(x=656, y=1161).move_to(x=626, y=764).release().perform()

                    actions = TouchAction(driver)
                    actions.press(x=514, y=1176)
                    actions.move_to(x=523, y=611)
                    actions.release()
                    actions.perform()

                self.dynamicwait(By.XPATH, "//android.widget.TextView[contains(@text,'India')]").click()
                time.sleep(5)

                # self.dynamicwait(By.ID, 'clear_text').click()
                # time.sleep(5)

                driver.find_element(By.ID, 'edit_text').send_keys(mobilenumber)
                time.sleep(5)

                self.dynamicwait(By.XPATH, '//android.widget.ImageButton[@content-desc="Next"]').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'common_dialog_ok_btn').click()
                time.sleep(5)

                self.dynamicwait(By.XPATH,'//android.view.ViewGroup[@content-desc="Verification code"]/android.widget.LinearLayout/android.widget.EditText[1]').click()
                time.sleep(5)

                driver.quit()

                print('Line App - Execution Completed')

                line_resultdata = {"Number": mobile_no, "message": "OTP generated successfully"}
                return line_resultdata



        except:

            print('Line App - Execution Completed')

            driver.quit()

            line_resultdata = {"Number":mobile_no,"message": "Failed to generate OTP" }
            return line_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
