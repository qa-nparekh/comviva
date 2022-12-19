import time

from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from comviva.config import config


class Airbnd:


    def generateOTP(self):

        global driver

        mobile_no = "9016255333"

        desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.airbnb.android',
                'appActivity': 'com.airbnb.android.feat.homescreen.HomeActivity',
                'autoGrantPermissions': 'true'
            }

        print('Airbnd App - Execution Started')

        driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

        driver.find_element(By.XPATH, '//android.widget.Spinner/android.view.ViewGroup/android.widget.TextView[2]').click()
        time.sleep(5)


        # el1 = driver.find_element(By.XPATH,
        #                                "//android.widget.CheckedTextView[contains(@text,'United States')]")
        #

            # self.dynamicwait(By.XPATH,"//android.widget.CheckedTextView[contains(@text," + str(countrycode) + ")]").click()
            # time.sleep(5)

            # element = self.dynamicwait(By.XPATH,"//android.widget.CheckedTextView[contains(@text," + str(mobilenumber) + ")]").click()
            # time.sleep(5)
            # #
            # actions = ActionChains(driver)
            # actions.move_to_element(element).click()

            # self.driver.find_element_by_android_uiautomator(
            #     "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("+ str(mobilenumber) + ").instance(0));")

        # driver.find_element(By.XPATH,'//android.widget.EditText[contains(@text,"Phone number")').send_keys(mobile_no)
        # time.sleep(15)
        #
        # driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"Continue")').click()
        # time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.RelativeLayout/android.view.ViewGroup/android.widget.EditText[1]').click()
        time.sleep(5)

        driver.quit()

        print('Airbnd App - Execution Completed')

        airbnd_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

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

otpRunner = Airbnd()
otpRunner.generateOTP()
