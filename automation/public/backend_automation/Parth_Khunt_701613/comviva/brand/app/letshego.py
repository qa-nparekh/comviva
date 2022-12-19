import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Letshego:

    def generateOTP(self, mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.letshego.tz',
                'appActivity': 'com.letshego.tz.view.ViewLoginOption',
                # 'app': config.apk_file_path+letshego.apk,
                'autoGrantPermissions': 'true'
            }

            print('Letshego App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'spinnerTextView').click()
            time.sleep(5)

            driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text,'English')]").click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,"//android.widget.Button[contains(@text,'Link Your Account Now')]").click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.LinearLayout/android.widget.EditText').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'CONTINUE')]").click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, "//android.widget.LinearLayout[2]/android.widget.TextView[2]")
            time.sleep(5)

            driver.quit()

            print('Letshego App - Execution Completed')

            letshego_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}
            return letshego_resultdata

        except:
            print('Letshego App - Execution Completed')

            driver.quit()

            letshego_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}
            return letshego_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
