# Linkedin URL
# https://www.linkedin.com/reg/join
import json

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class LinkedinWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        mobile_no = '+'+str(countrycode) + str(mobilenumber)
        password = firstname + "@1990"

        try:

            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

            stealth(driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )

            driver.get(brandurl)
            time.sleep(5)

            print('Linkedin Web - Execution Started')

            self.dynamicwait(By.NAME,'email-or-phone').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.NAME,'password').send_keys(password)
            time.sleep(5)

            driver.find_element(By.ID,'join-form-submit').click()
            time.sleep(5)

            self.dynamicwait(By.NAME,'first-name').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.NAME,"last-name").send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.ID,'join-form-submit').click()
            time.sleep(5)

            try:

                driver.find_element(By.XPATH, "//h2[contains(., 'Verification')]")

                print('Linkedin Web - Execution Completed')

                driver.quit()

                linkedin_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                       "Password": password, "message": 'Failed to generated OTP'}

                return linkedin_resultdata

            except:

                print("Captcha not found")


            if self.dynamicwait(By.XPATH, "//h1[contains(.,'Enter the code that was sent to your mobile phone.')]") is None:

                print('Linkedin Web - Execution Completed')

                driver.quit()

                linkedin_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                       "Password": password, "Message": 'Failed to generated OTP'}

                return linkedin_resultdata

            time.sleep(5)

            driver.quit()

            print('Linkedin Web - Execution Completed')

            linkedin_resultdata = {"First Name": firstname, "Last Name": lastname,"Number":mobile_no,
                                   "Password": password,"Message": 'OTP generated successfully'}
            return linkedin_resultdata

        except:

            print('Linkedin Web - Execution Completed')

            driver.quit()

            linkedin_resultdata = {"First Name": firstname, "Last Name": lastname,"Number":mobile_no,
                                   "Password": password,"Message": 'Failed to generated OTP'}

            return linkedin_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
