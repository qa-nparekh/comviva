import time

from appium import webdriver as appDriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Binance:

    def generateOTP(self,countrycode,mobilenumber):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        password = firstname + "@2004"

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.binance.dev',
                'appActivity': 'com.eaas.launcher.activities.main.MainActivity',
                # 'app': config.apk_path+'binance.apk',
                'autoGrantPermissions': 'true'
            }

            print('Binance App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.Button[@text="Sign up with phone or email"]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.TextView[@text="Phone Number"]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.view.View[1]/android.view.View/android.view.View[3]/android.widget.TextView').click()
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text,'+ " + str(countrycode) + "')]").click()
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText').send_keys(password)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.view.View[1]/android.view.View[2]/android.view.View[4]/android.view.View/android.view.View/android.view.View/android.widget.CheckBox/android.widget.TextView').click()
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.Button[@text="Create Personal Account"]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText').click()
            time.sleep(5)

            driver.quit()

            print('Binance App - Execution Completed')

            binance_resultdata = { "Password": password,"Number":mobile_no,"Message": 'OTP generated successfully'}

            return binance_resultdata

        except:

            print('FAILED')

            driver.quit()

            binance_resultdata = { "Password": password,"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return binance_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
