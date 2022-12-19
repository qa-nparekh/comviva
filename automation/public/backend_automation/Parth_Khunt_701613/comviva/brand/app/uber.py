import time

from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Uber:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.ubercab',
                'appActivity': 'com.ubercab.presidio.app.core.root.RootActivity',
                # 'app': config.apk_file_path,
                'autoGrantPermissions': 'true'
            }

            print('Uber App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'welcome_screen_continue').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.view.View[2]/android.view.View/android.widget.EditText').send_keys(mobilenumber)
            time.sleep(5)

            print('before1')

            # self.dynamicwait(By.ID,'PHONE_COUNTRY_CODE').click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.view.View[1]/android.widget.Image').click()
            # time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.Image[contains(@text,"open")]').click()
            # time.sleep(5)


            # self.dynamicwait(By.XPATH,'//android.widget.TextView[contains(@text,"🇺🇸"]').click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH,"//android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]").click()
            time.sleep(5)

            print('1')

            result = False

            while (result != True):
                try:
                    # result = driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+" + str(countrycode) + "')]").is_displayed()
                    # time.sleep(5)
                    result = driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text,'+91')]").is_displayed()
                    time.sleep(5)
                except:
                    time.sleep(2)

            # TouchAction(driver).press(x=548, y=972).move_to(x=540, y=1423).release().perform()
                    TouchAction(driver).press(x=548, y=532).move_to(x=557, y=755).release().perform()
            #     TouchAction(driver).press(x=581, y=535).move_to(x=614, y=948).release().perform()
                    time.sleep(2)


            # self.dynamicwait(By.XPATH, "//android.widget.TextView[contains(@text," + str(countrycode) + ")]").click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH, "//android.widget.TextView[contains(@text,'+91')]").click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.view.View[2]/android.view.View/android.widget.EditText').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.view.View/android.view.View/android.widget.Button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'PHONE_SMS_OTP - 0').click()
            time.sleep(5)

            driver.quit()

            print('Uber App - Execution Completed')

            uber_resultdata = {"Message": 'OTP generated successfully'}
            return uber_resultdata

        except:
            print('Uber App - Executed Completed')

            driver.quit()

            uber_resultdata = {"Message": 'Failed to generate OTP'}
            return uber_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
