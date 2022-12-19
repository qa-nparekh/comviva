import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class WhatsAppbusiness:

    def generateOTP(self, countrycode, mobilenumber):

        global driver

        try:
            desired_caps = {
                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.whatsapp.w4b',
                'appActivity': 'com.whatsapp.Main',
                'autoGrantPermissions': 'true'
                # "app": r"C:\Sapizon\demo\data\apk\demo.apk"
                # 'app': r"c:\python_new_project\demo\brand\app\demo.apk"
            }

            print('WhatsApp Business App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)

            self.dynamicwait(By.ID, 'com.whatsapp.w4b:id/eula_accept').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'com.whatsapp.w4b:id/use_a_different_number').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'com.whatsapp.w4b:id/registration_cc').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'com.whatsapp.w4b:id/registration_cc').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.ID, 'com.whatsapp.w4b:id/registration_phone').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'com.whatsapp.w4b:id/registration_submit').click()
            time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.Button[contains(@text,"CONTINUE")]').click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.Button[@text=\"OK\"]').click()
            time.sleep(5)

            message = ""
            result_message = ""
            substring = "Waiting to automatically detect an SMS sent to"

            try:
                self.dynamicwait(By.ID, 'com.whatsapp.w4b:id/title_toolbar_text')
                time.sleep(5)

                message = driver.find_element(By.ID, 'com.whatsapp.w4b:id/send_code_description').text

                if substring in message:
                    result_message = "OTP generated successfully"
                else:
                    result_message = "Failed to generate OTP"

                driver.quit()
                print('WhatsApp - Execution Completed')

                whatsapp_resultdata = {"message": result_message}
                return whatsapp_resultdata

            except:

                driver.find_element(By.ID, 'verify_with_sms_button').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'com.whatsapp.w4b:id/title_toolbar_text')
                time.sleep(5)

                message = driver.find_element(By.ID, 'com.whatsapp.w4b:id/send_code_description').text

                if substring in message:
                    result_message = "OTP generated successfully"
                else:
                    result_message = "Failed to generate OTP"

                driver.quit()

                print('WhatsApp Business App  - Execution Completed')

                whatsappbusiness_resultdata = {"message": message}
                return whatsappbusiness_resultdata

        except:
            print('WhatsApp Business App - Execution Completed')

            driver.quit()

            whatsappbusiness_resultdata = {"message": "Failed to generate OTP" }
            return whatsappbusiness_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
