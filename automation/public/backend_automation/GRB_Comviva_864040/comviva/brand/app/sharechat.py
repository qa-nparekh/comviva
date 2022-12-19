import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Sharechat:

    def generateOTP(self, countrycode, mobilenumber):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'in.mohalla.sharechat',
                'appActivity': 'in.mohalla.sharechat.home.main.HomeActivity',
                # 'app': config.apk_path+'sharechat.apk',
                'autoGrantPermissions': 'true'
            }

            print('Sharechat App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'sign_up_with_email_or_phone').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'country_code_picker').click()
            time.sleep(15)


            # self.dynamicwait(By.XPATH, '// android.widget.Button[ @ content - desc = "India"]').click()
            # time.sleep(5)

            self.dynamicwait(By.ID, 'search').send_keys(countrycode).click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'').click()
            time.sleep(5)

            driver.find_element(By.ID, 'phone_field').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'phone_field').send_keys(mobilenumber)
            time.sleep(15)

            print('h2')

            self.dynamicwait(By.XPATH,'//android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.Button').click()
            time.sleep(5)

            # self.dynamicwait(By.ID, 'button_text').click()
            # time.sleep(5)

            self.dynamicwait(By.ID, 'confirmation_field').click()
            time.sleep(5)

            driver.quit()

            print('Sharechat App - Execution Completed')

            sharechat_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return sharechat_resultdata

        except:

            print('Sharechat App - Execution Completed')

            driver.quit()

            sharechat_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return sharechat_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
