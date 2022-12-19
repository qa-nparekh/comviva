import time
import datetime

from appium import webdriver as appDriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class SnapChat:

    def generateOTP(self, countrycode, mobilenumber):

        global driver
        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        password = firstname + "@2004"

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.snapchat.android',
                'appActivity': 'com.snap.mushroom.MainActivity',
                'app': r'C:\python_new_project\demo\brand\app\snapchat.apk',
                'autoGrantPermissions': 'true'
            }


            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            driver.find_element(By.ID, 'signup_button_horizontal').click()
            time.sleep(5)

            driver.find_element(By.ID, 'display_name_first_name_field').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.ID, 'display_name_last_name_field').send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"Sign Up & Accept\"]').click()
            time.sleep(5)


            d = datetime.datetime.today() + datetime.timedelta(days=35)
            current_month = d.strftime("%b")

            print("//android.widget.Button[@text='" + current_month + "']")

            self.dynamicwait(By.XPATH, "//android.widget.NumberPicker[1]//android.widget.Button[2]").click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"Continue\"]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//android.widget.TextView[@text=\"Your username\"]')
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"Continue\"]').click()
            time.sleep(25)

            self.dynamicwait(By.ID, 'password_form_field').send_keys(password)
            time.sleep(20)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"Continue\"]').click()
            time.sleep(10)

            try:
                driver.find_element(By.ID, 'com.snapchat.android:id/signup_with_phone_instead').click()
                time.sleep(5)

            except:

                print("Not found - signup_with_phone_instead")

            self.dynamicwait(By.ID, 'top_country_code_display_textview').click()
            time.sleep(5)

            driver.find_element(By.ID, 'input_field_edit_text').send_keys(countrycode)
            time.sleep(5)


            driver.find_element(By.XPATH, "//javaClass[contains(@text," + str(countrycode) + ")]").click()
            time.sleep(5)

            driver.find_element(By.ID, 'bottom_phone_form_field').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'bottom_phone_form_field').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"Continue\"]').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'com.snapchat.android:id/code_field')
            time.sleep(5)

            driver.quit()

            print('PASSED')

            snapchat_resultdata = {"First Name": firstname, "Last Name": lastname, "Password": password,
                                   "Message": 'OTP generated successfully'}

            return snapchat_resultdata

        except:
            print('FAILED')
            driver.quit()

            snapchat_resultdata = {"First Name": firstname, "Last Name": lastname, "Password": password,
                                   "Message": 'Failed to generate OTP'}

            return snapchat_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
