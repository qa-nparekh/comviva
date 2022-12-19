import time

from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Boomplay:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.afmobi.boomplayer',
                'appActivity': 'com.boomplay.ui.main.MainActivity',
                # 'app': config.apk_path+'boomplay.apk',
                'autoGrantPermissions': 'true'
            }

            print('Boomplay App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'bt_ok').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.TextView[@text = "skip"]').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'iv_user_cover').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.TextView[@text = "Log in / Sign up"]').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.afmobi.boomplayer:id/agree_check_box').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text = "Use Phone or Email"]').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'com.afmobi.boomplayer:id/country_code_ll').click()
            time.sleep(5)

            elemnt = driver.find_element(By.ID, 'com.afmobi.boomplayer:id/country_list_view')

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
                    result = driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text,'+" + str(
                        countrycode) + "')]").is_displayed()
                except:
                    time.sleep(2)

                    TouchAction(driver).press(x=locationXStart, y=locationYStart).move_to(x=locationXEnd,
                                                                                          y=loctionYEnd).release().perform()
                    time.sleep(3)

            driver.find_element(By.XPATH,
                                "//android.widget.TextView[contains(@text,'+" + str(countrycode) + "')]").click()
            time.sleep(5)

            driver.find_element(By.ID, 'etPhoneNumber').send_keys(mobilenumber)
            time.sleep(5)

            self.dynamicwait(By.ID, 'tvNextStep').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.afmobi.boomplayer:id/tv_title')
            time.sleep(5)

            driver.quit()

            print('Boomplay App - Execution Completed')



            boomplay_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return boomplay_resultdata

        except:

            print('Boomplay App - Execution Completed')

            driver.quit()

            boomplay_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return boomplay_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
