import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Telegram:

    def generateOTP(self, mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'org.telegram.messenger',
                'appActivity': 'org.telegram.messenger.DefaultIcon',
                # 'app': config.apk_file_path+'telegram.apk',
                'autoGrantPermissions': 'true'
            }

            print('Telegram App - Execution Started')


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Start Messaging")]').click()
            time.sleep(5)

            try:

                self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"CONTINUE")]').click()
                time.sleep(5)


                self.dynamicwait(By.XPATH,'//android.widget.EditText[@content-desc="Country code"]').clear()
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="Country code"]').send_keys(countrycode)
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="Phone number"]').clear()
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="Phone number"]').send_keys(mobilenumber)
                time.sleep(5)

                driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="Done"]').click()
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.TextView[contains(@text,"CONTINUE")]').click()
                time.sleep(5)

                # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Enter code")]')
                # time.sleep(5)

                # self.dynamicwait(By.XPATH, '//android.widget.LinearLayout/android.widget.TextView[1]')
                # time.sleep(5)

                self.dynamicwait(By.CLASS_NAME,'android.widget.EditText')
                time.sleep(5)

                driver.quit()

                print('Telegram App - Execution Completed')

                telegram_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}
                return telegram_resultdata

            except:

                self.dynamicwait(By.XPATH, '//android.widget.EditText[@content-desc="Country code"]').clear()
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="Country code"]').send_keys(countrycode)
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="Phone number"]').clear()
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.EditText[@content-desc="Phone number"]').send_keys(mobilenumber)
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Done"]').click()
                time.sleep(5)

                driver.find_element(By.XPATH, '//android.widget.TextView[contains(@text,"CONTINUE")]').click()
                time.sleep(5)

                # self.dynamicwait(By.XPATH, '//android.widget.TextView[contains(@text,"Enter code")]')
                # time.sleep(5)

                # self.dynamicwait(By.XPATH, '//android.widget.LinearLayout/android.widget.TextView[1]')
                # time.sleep(5)

                self.dynamicwait(By.CLASS_NAME, 'android.widget.EditText')
                time.sleep(5)

                driver.quit()

                print('Telegram App - Execution Completed')

                telegram_resultdata = {"Number": mobile_no, "Message": 'OTP generated successfully'}
                return telegram_resultdata


        except:
            print('Telegram App - Execution Completed')

            driver.quit()

            telegram_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}
            return telegram_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
