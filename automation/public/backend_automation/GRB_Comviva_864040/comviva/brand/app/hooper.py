import time

import faker.generator
from appium import webdriver as appDriver
from appium.webdriver.common.touch_action import TouchAction
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk


from config import config


class Hopper:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)



        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.hopper.mountainview.play',
                'appActivity': 'com.hopper.mountainview.activities.LaunchPage',
                # 'app': config.apk_path+'hooper.apk',
                'autoGrantPermissions': 'true'
            }

            print('Hopper App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            try:
                self.dynamicwait(By.ID, 'onboarding_dismiss_cta').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'headerSettingsIcon').click()
                time.sleep(15)

                self.dynamicwait(By.ID, 'login_button').click()
                time.sleep(5)

                self.dynamicwait(By.XPATH,
                                 '//android.widget.LinearLayout/InputField[1]/android.widget.FrameLayout/android.widget.EditText').click()
                time.sleep(5)

                elemnt = driver.find_element(By.ID, 'com.hopper.mountainview.play:id/countryList')

                location = elemnt.location
                size = elemnt.size
                w, h = size['width'], size['height']

                print(location)
                print(size)
                print(w, h)
                height = size['height']/2
                width = size['width']

                locationXStart = round(height * 0.90)
                locationXEnd = round(locationXStart/2)
                loctionYEnd = round(locationXEnd/2)

                locationYStart = round(width-200)

                print(locationXStart)

                print(locationXEnd)

                result = False

                while (result != True):
                    print(result)
                    try:

                        result = driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+"+str(countrycode)+"')]").is_displayed()
                        time.sleep(2)
                        print("try result ", result)

                    except:
                        time.sleep(2)
                        print('before')
                        TouchAction(driver).press(x=locationXStart, y=locationYStart).move_to(x=locationXEnd, y=loctionYEnd).release().perform()


                driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+"+str(countrycode)+"')]").click()
                time.sleep(5)

                driver.find_element(By.XPATH, '//InputField[2]/android.widget.FrameLayout[1]/android.widget.EditText').send_keys('5555551234')
                time.sleep(5)

                self.dynamicwait(By.ID, 'com.hopper.mountainview.play:id/primarySignInButton').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'com.hopper.mountainview.play:id/paragraph')
                time.sleep(5)

                driver.quit()

                print('Hopper App - Execution Started')

                hopper_resultdata = {"Number": mobile_no, "Message": 'OTP generated successfully'}

                return hopper_resultdata



            except:

                self.dynamicwait(By.ID,'headerSettingsIcon').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'login_button').click()
                time.sleep(5)

                self.dynamicwait(By.XPATH, '//android.widget.LinearLayout/InputField[1]/android.widget.FrameLayout/android.widget.EditText').click()
                time.sleep(5)

                elemnt = driver.find_element(By.ID, 'com.hopper.mountainview.play:id/countryList')

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
                    print(result)
                    try:
                        # result = driver.find_element(By.XPATH,"//com.hopper.mountainview.play:id/listText[contains(@text,'India')]").is_displayed()

                        result = driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text,'+" + str(
                            countrycode) + "')]").is_displayed()
                        time.sleep(2)
                        print("try result ", result)

                    except:
                        time.sleep(2)
                        print('before')
                        TouchAction(driver).press(x=locationXStart, y=locationYStart).move_to(x=locationXEnd,
                                                                                              y=loctionYEnd).release().perform()

                driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'+" + str(countrycode) + "')]").click()
                time.sleep(5)

                driver.find_element(By.ID, 'phoneNumberField').send_keys(mobilenumber)
                time.sleep(5)

                self.dynamicwait(By.ID,'signInButton').click()
                time.sleep(5)

                self.dynamicwait(By.ID, 'paragraph').click()
                time.sleep(5)

                driver.quit()

                print('Hopper App - Execution Started')

                hopper_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

                return hopper_resultdata

        except:
            print('Hopper App - Execution Started')

            driver.quit()

            hopper_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return hopper_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
