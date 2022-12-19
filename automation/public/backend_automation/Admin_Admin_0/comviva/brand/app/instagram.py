import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Instagram:

    def generateOTP(self, mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.instagram.android',
                'appActivity': 'com.instagram.mainactivity.MainActivity',
                # 'app': config.apk_path+'instagram.apk',
                'autoGrantPermissions': 'true'
            }

            print('Instagram App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'sign_up_with_email_or_phone').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'country_code_picker').click()
            time.sleep(5)

            driver.find_element(By.ID, 'search').send_keys(countrycode).click()
            time.sleep(5)

            driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,"+str(countrycode)+")]").click()
            time.sleep(5)

            driver.find_element(By.ID, 'phone_field').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'phone_field').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.Button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'confirmation_field').click()
            time.sleep(5)

            driver.quit()

            print('Instagram App - Execution Completed')

            instgram_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}
            return instgram_resultdata

        except:
            print('Instagram App - Execution Completed')

            driver.quit()

            instgram_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}
            return instgram_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
