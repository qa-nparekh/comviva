import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Instagramlite:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.instagram.lite',
                'appActivity': 'com.facebook.lite.MainActivity',
                # 'app': config.apk_path+'instagramlite.apk',
                'autoGrantPermissions': 'true'
            }

            print('InstagramLite App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.View').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.View').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.MultiAutoCompleteTextView[contains(@text,"Search country name or code")]').send_keys(countrycode)
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//androidx.recyclerview.widget.RecyclerView//android.view.View').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.MultiAutoCompleteTextView').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.view.ViewGroup[5]/android.view.View').click()
            time.sleep(5)
            print('hello')

            self.dynamicwait(By.CLASS_NAME, 'android.widget.MultiAutoCompleteTextView').click()
            time.sleep(5)

            driver.quit()

            print('InstagramLite App - Execution Completed')

            instgramlite_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return instgramlite_resultdata

        except:
            print('InstagramLite App - Execution Completed')

            driver.quit()

            instgramlite_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return instgramlite_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
