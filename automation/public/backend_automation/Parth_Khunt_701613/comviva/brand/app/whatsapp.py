import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class WhatsApp:

    def generateOTP(self, countrycode, mobilenumber):

        global driver

        try:
            desired_caps = {
                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.whatsapp',
                'appActivity': 'com.whatsapp.Main',
                'autoGrantPermissions': 'true'
                # "app": config.apk_path+'whatsapp.apk'
                # 'app': r"c:\python_new_project\demo\brand\app\demo.apk"
            }

            print('WhatsApp - Execution Started')

            driver = appDriver.Remote('http://localhost:4724/wd/hub', desired_caps)

            self.dynamicwait(By.ID, 'eula_accept').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'registration_cc').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'registration_cc').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.ID, 'registration_phone').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'registration_submit').click()

            self.dynamicwait(By.XPATH, '//android.widget.Button[@text=\"OK\"]').click()
            time.sleep(5)

            message = ""
            result_message = ""
            substring = "Waiting to automatically detect an SMS sent to"

            try:
                self.dynamicwait(By.ID, 'title_toolbar_text')
                time.sleep(5)

                message = driver.find_element(By.ID, 'com.whatsapp:id/send_code_description').text

                if substring in message:
                    result_message = "OTP generated successfully"
                else:
                    result_message = "Failed to generate OTP"

                driver.quit()
                print('WhatsApp - Execution Completed')

                whatsapp_resultdata = {"message": result_message}
                return whatsapp_resultdata

            except:

                self.dynamicwait(By.ID, 'verify_with_sms_button').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'title_toolbar_text')
                time.sleep(5)

                message = driver.find_element(By.ID, 'com.whatsapp:id/send_code_description').text

                if substring in message:
                    result_message = "OTP generated successfully"
                else:
                    result_message = "Failed to generate OTP"

                driver.quit()

                print('WhatsApp - Execution Completed')

                whatsapp_resultdata = {"message": message}
                return whatsapp_resultdata

        except:
            print('WhatsApp - Execution Completed')

            driver.quit()

            whatsapp_resultdata = {"message": "Failed to generate OTP" }
            return whatsapp_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
