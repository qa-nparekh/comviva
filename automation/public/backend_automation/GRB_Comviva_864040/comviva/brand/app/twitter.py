import time
from random import choice

from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Twitter:

    def generateOTP(self, mobilenumber, countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        mobile_no = str(countrycode) + str(mobilenumber)
        yearrange = list(range(1960, 1999))
        year = choice(yearrange)

        try:
            desired_caps = {

                'deviceName': config.udid,
                'platformName': 'android',
                'appPackage': 'com.twitter.android',
                'appActivity': 'com.twitter.android.StartActivity',
                # 'app': config.apk_path+'twitter.apk',
                'autoGrantPermissions': 'true'

            }

            print('Twitter App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.view.ViewGroup[2]/android.widget.Button').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.EditText[contains(@text,"Name")]').send_keys(firstname)
            time.sleep(5)

            self.dynamicwait(By.XPATH,"//android.widget.EditText[contains(@text,'Phone number or email address')]").send_keys('+919099807114')
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.EditText[contains(@text,"Date of birth")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, "//android.widget.NumberPicker[1]//android.widget.Button[2]").click()
            time.sleep(5)

            print('1')

            self.dynamicwait(By.XPATH,'//android.widget.NumberPicker[2]/android.widget.Button[1]').click()
            time.sleep(5)

            print('2')

            self.dynamicwait(By.XPATH,'//android.widget.NumberPicker[3]/android.widget.Button').click()
            time.sleep(5)

            print('3')

            self.dynamicwait(By.XPATH,'//android.widget.EditText[contains(@text,"2021")]').send_keys('1995')
            time.sleep(5)

            print('hello')

            driver.find_element(By.XPATH, '//android.view.View/android.widget.Button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'cta_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'cta_button').click()
            time.sleep(5)

            # self.dynamicwait(By.ID, 'button1').click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.LinearLayout/android.widget.Button[2]').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'textinput_placeholder').click()

            driver.quit()

            print('Twitter App - Execution Completed')

            twitter_resultdata = {"First Name": firstname, "Number": mobile_no, "Message": 'OTP generated successfully'}

            return twitter_resultdata

        except:

            print('Twitter App - Execution Completed')

            driver.quit()

            twitter_resultdata = {"First Name": firstname, "Number": mobile_no, "Message": 'Failed to generate OTP'}

            return twitter_resultdata


    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
