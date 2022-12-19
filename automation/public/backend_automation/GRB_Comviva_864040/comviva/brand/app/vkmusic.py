import time

from appium import webdriver as appDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config

class VKMusic:

    def generateOTP(self, countrycode, mobilenumber):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)


        try:
            desired_caps = {
                'deviceName': config.udid,
                'platformName': 'android',
                'appPackage': 'com.vkontakte.android',
                'appActivity': 'com.vkontakte.android.MainActivity',
                # "app": config.apk_path+'vkmusic.apk'
                # 'app': r"c:\python_new_project\demo\brand\app\demo.apk"
            }

            print('VK music messenger App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)

            driver.back()

            self.dynamicwait(By.ID, 'sign_up_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'com.vkontakte.android:id/phone_code').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.vkontakte.android:id/msv_bg_left_part').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+"+str(countrycode)+"')]").click()
            time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.view.ViewGroup[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]Attribute').send_keys(countrycode)
            # time.sleep(5)

            # self.dynamicwait(By.ID,'msv_bg_left_part').send_keys(countrycode)
            # time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
            # time.sleep(5)
            #
            # self.dynamicwait(By.XPATH,'//android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').send_keys(countrycode)
            # time.sleep(5)

            # self.dynamicwait(By.XPATH,"//android.widget.TextView[contains(@text,'+"+str(countrycode)+"')]").click()
            # time.sleep(5)

            driver.find_element(By.ID, 'phone_code').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'continue_btn').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.LinearLayout/android.widget.EditText').click()
            time.sleep(5)

            driver.find_element(By.ID,'button1').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'code_edit_text')
            time.sleep(5)

            print('VK music messenger App - Execution Completed')

            driver.quit()

            vk_resultdata = {"message": "OTP generated successfully"}

            return vk_resultdata


        except:

            print('VK music messenger App - Execution Completed')

            driver.quit()

            vk_resultdata = {"message": "Failed to generate OTP" }
            return vk_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
