
import time
import datetime
from random import choice

from appium import webdriver as appDriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Badoo:

    def generateOTP(self, countrycode, mobilenumber):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)
        faker = Faker()
        firstname = faker.first_name_male()
        monthrange = list(range(10, 12))
        month_no = choice(monthrange)
        month_object = datetime.datetime.strptime(str(month_no), "%m")
        month = month_object.strftime("%B")

        daterange = list(range(10, 29))
        day = choice(daterange)


        yearrange = list(range(1960, 1999))
        year = choice(yearrange)

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.badoo.mobile',
                'appActivity': 'com.badoo.mobile.android.BadooActivity',
                # 'app': config.apk_path+'badoo.apk',
                'autoGrantPermissions': 'true'
            }

            print('Badoo App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'landing_button_female').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.FrameLayout/android.widget.EditText').send_keys(firstname)
            time.sleep(15)


            # self.dynamicwait(By.XPATH, '// android.widget.Button[ @ content - desc = "India"]').click()
            # time.sleep(5)

            driver.find_element(By.ID, 'registration_button').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.CheckBox').click()
            time.sleep(5)

            driver.find_element(By.ID, 'apply_button').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.LinearLayout[1] / android.widget.LinearLayout / android.widget.RelativeLayout[1] / android.widget.TextView').click()
            time.sleep(5)

            # self.dynamicwait(By.XPATH,'//android.widget.LinearLayout[1] / android.widget.LinearLayout / android.widget.RelativeLayout[1] / android.widget.TextView').send_keys('0')
            # time.sleep(5)
            #
            # self.dynamicwait(By.XPATH,'//android.widget.LinearLayout[1] / android.widget.LinearLayout / android.widget.RelativeLayout[2] / android.widget.TextView').send_keys('2')
            # time.sleep(5)


            driver.find_element(By.XPATH,'//android.widget.LinearLayout[2] / android.widget.LinearLayout / android.widget.RelativeLayout[1] / android.widget.TextView').click()
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.LinearLayout[2] / android.widget.LinearLayout / android.widget.RelativeLayout[1] / android.widget.TextView').send_keys(1)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.LinearLayout[2] / android.widget.LinearLayout / android.widget.RelativeLayout[2] / android.widget.TextView').send_keys(2)
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.LinearLayout[3] / android.widget.LinearLayout / android.widget.RelativeLayout[1] / android.widget.TextView').click()
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.LinearLayout[3] / android.widget.LinearLayout / android.widget.RelativeLayout[1] / android.widget.TextView').send_keys('1')
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.LinearLayout[3] / android.widget.LinearLayout / android.widget.RelativeLayout[2] / android.widget.TextView').send_keys('9')
            time.sleep(5)

            driver.find_element(By.XPATH, '//android.widget.LinearLayout[3] / android.widget.LinearLayout / android.widget.RelativeLayout[3] / android.widget.TextView').send_keys('9')
            time.sleep(5)

            driver.find_element(By.XPATH,'//android.widget.LinearLayout[3] / android.widget.LinearLayout / android.widget.RelativeLayout[4] / android.widget.TextView').send_keys('8')
            time.sleep(5)

            driver.find_element(By.ID,'registration_button').click()
            time.sleep(5)




            driver.quit()

            print('Badoo App - Execution Completed')

            badoo_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}

            return badoo_resultdata

        except:

            print('Badoo App - Execution Completed')


            driver.quit()

            badoo_resultdata = {"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return badoo_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None

