import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Ding:

    def generateOTP(self, countrycode, mobilenumber):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.ezetop.world',
                'appActivity': 'com.ezetop.world.presentation.splash.SplashScreenActivity',
                # 'app': config.apk_path+'ding.apk',
                'autoGrantPermissions': 'true'
            }

            print('Ding App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'textViewFooterLogin').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'footerLink').click()
            time.sleep(15)

            self.dynamicwait(By.ID, 'editEmailOrNumber').click()
            time.sleep(5)

            driver.find_element(By.ID, 'editEmailOrNumber').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.RadioGroup/android.widget.RadioButton[2]').click()
            time.sleep(5)

            driver.find_element(By.ID, 'buttonEmailPhoneNumberAuthNextStep').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'textViewSmsCodeTitle')
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.EditText').click()
            driver.quit()

            print('Ding App - Execution Completed')

            ding_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}
            return ding_resultdata

        except:

            print('Ding App - Execution Completed')

            driver.quit()

            ding_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}
            return ding_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
