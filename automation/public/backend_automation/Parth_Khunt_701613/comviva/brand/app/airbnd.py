import time

from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Airbnb:


    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.airbnb.android',
                'appActivity': 'com.airbnb.android.feat.homescreen.HomeActivity',
                # 'app': config.apk_path+'airbnb.apk',
                'autoGrantPermissions': 'true'
            }

            print('Airbnd App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            # self.dynamicwait(By.XPATH, '//android.widget.Spinner/android.view.ViewGroup/android.widget.TextView[2]').click()
            # time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.Spinner/android.view.ViewGroup/android.widget.ImageView').click()
            time.sleep(5)

            print('1')

            # elemnt = self.dynamicwait(By.ID, 'android:id/select_dialog_listview')
            # elemnt = self.dynamicwait(By.CLASS_NAME,'android.widget.ListView')
            elemnt= self.dynamicwait(By.XPATH,'//hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView')
            print('2')

            location = elemnt.location
            size = elemnt.size
            w, h = size['width'], size['height']

            print(location)
            print(size)
            print(w, h)
            height = size['height'] / 2
            width = size['width']

            locationXStart = round(height * 0.90)
            locationXEnd = round(locationXStart / 2)
            loctionYEnd = round(locationXEnd / 2)

            locationYStart = round(width - 200)

            print(locationXStart)

            print(locationXEnd)

            result = False

            while (result != True):
                try:
                    result = driver.find_element(By.XPATH,"//android.widget.CheckedTextView[contains(@text,'+" + str(countrycode) + "')]").is_displayed()
                except:
                    time.sleep(2)

                    TouchAction(driver).press(x=locationXStart, y=locationYStart).move_to(x=locationXEnd,y=loctionYEnd).release().perform()
                    time.sleep(3)

            driver.find_element(By.XPATH,"//android.widget.CheckedTextView[contains(@text,'+" + str(countrycode) + "')]").click()
            time.sleep(5)

            print('found')

            self.dynamicwait(By.XPATH,'//android.widget.EditText[contains(@text,"Phone number")]').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"Continue")').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.RelativeLayout/android.view.ViewGroup/android.widget.EditText[1]').click()
            time.sleep(5)

            driver.quit()

            print('Airbnd App - Execution Completed')

            airbnd_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return airbnd_resultdata

        except:

            print('Airbnd App - Execution Completed')

            driver.quit()

            airbnd_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return airbnd_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None

    def find_element_by_android_uiautomator(self, path):
        pass
