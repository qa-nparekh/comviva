import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Imo:

    def generateOTP(self, mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.imo.android.imoim',
                'appActivity': 'com.imo.android.imoim.activities.Home',
                # 'app': config.apk_path+'imo.apk',
                'autoGrantPermissions': 'true'
            }

            print('Imo App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            driver.back()

            self.dynamicwait(By.ID, 'country_code').click()
            time.sleep(5)

            driver.find_element(By.ID, 'country_code').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'country_code').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.ID, 'phone').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'get_started_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'btn_positive').click()
            time.sleep(5)

            try:
                self.dynamicwait(By.ID, 'btn_positive').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'new_sms_code_input').click()
                time.sleep(5)

                driver.quit()

                print('Imo App - Execution Completed')

                imo_resultdata = {"Number": mobile_no, "Message": 'OTP generated successfully'}
                return imo_resultdata


            except:

                self.dynamicwait(By.ID, 'new_sms_code_input').click()
                time.sleep(5)

            # self.dynamicwait(By.ID, 'et_flash_call').click()
            # time.sleep(5)

            driver.quit()

            print('Imo App - Execution Completed')

            imo_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}
            return imo_resultdata

        except:
            print('Imo App - Execution Completed')

            driver.quit()

            imo_resultdata = {"Number":mobile_no,"Message": 'Failed to generate OTP'}
            return imo_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
