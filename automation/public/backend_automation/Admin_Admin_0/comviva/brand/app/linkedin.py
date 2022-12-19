import time

from appium import webdriver as appDriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class Linkedin:

    def generateOTP(self,mobilenumber, countrycode):

        global driver

        mobile_no = '+'+str(countrycode)+str(mobilenumber)

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        password = firstname + "@2004"

        try:
            desired_caps = {

                'udid': config.udid,
                'platformName': 'android',
                'appPackage': 'com.linkedin.android',
                'appActivity': 'com.linkedin.android.authenticator.LaunchActivity',
                # 'app': config.apk_path+'linkedin.apk',
                'autoGrantPermissions': 'true'
            }

            print('Linkedin App - Execution Started')

            driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(5)

            self.dynamicwait(By.ID, 'growth_prereg_fragment_join_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'growth_join_split_form_first_name').send_keys(firstname)
            time.sleep(15)

            driver.find_element(By.ID, 'growth_join_split_form_last_name').send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.ID, 'growth_join_split_form_join_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'growth_join_split_form_email_address').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.ID, 'growth_join_split_form_join_button').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'growth_join_split_form_password').send_keys(password)
            time.sleep(5)

            driver.find_element(By.ID, 'growth_join_split_form_join_button').click()
            time.sleep(15)

            # self.dynamicwait(By.ID, 'input__phone_verification_pin')
            # time.sleep(5)

            self.dynamicwait(By.XPATH,'//android.widget.TextView[contains(@text,"Enter the code that was sent to your mobile phone.")]')
            time.sleep(5)

            driver.quit()

            print('Linkedin App - Execution Completed')

            linkedin_resultdata = {"First Name": firstname, "Last Name": lastname, "Password": password,"Number":mobile_no,"Message": 'OTP generated successfully'}

            return linkedin_resultdata

        except:

            print('Linkedin App - Execution Completed')

            driver.quit()

            linkedin_resultdata = {"First Name": firstname, "Last Name": lastname, "Password": password,"Number":mobile_no, "Message": 'Failed to generate OTP'}

            return linkedin_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
