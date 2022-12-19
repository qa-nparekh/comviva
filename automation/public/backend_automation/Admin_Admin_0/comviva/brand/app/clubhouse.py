import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Clubhouse:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.clubhouse.app',
                'appActivity': 'com.clubhouse.android.ui.ClubhouseActivity',
                # 'app': config.apk_path+'clubhouse.apk',
                'autoGrantPermissions': 'true'
            }

            print('Clubhouse App - Exceution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'welcome_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'rlClickConsumer').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'editText_search').send_keys(countrycode)
            time.sleep(5)

            # self.dynamicwait(By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.TextView[contains(@text,'+"+str(countrycode)+"')]").click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH,"//android.widget.TextView[contains(@text,'+" + str(countrycode) + "')]").click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'phone_number').send_keys(mobilenumber).click()
            time.sleep(5)

            driver.find_element(By.ID, 'next_button').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.view.ViewGroup / android.widget.TextView[1]')
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.view.ViewGroup/android.widget.EditText').click()
            time.sleep(5)

            driver.quit()

            print('Clubhouse App - Exceution Started')

            clubhouse_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return clubhouse_resultdata

        except:

            print('Clubhouse App - Exceution Started')

            driver.quit()

            clubhouse_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return clubhouse_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
