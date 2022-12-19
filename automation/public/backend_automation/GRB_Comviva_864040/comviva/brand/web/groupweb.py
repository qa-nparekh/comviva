#GRoup URL
# https://web.groupme.com/signup
import json

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class GroupWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        mobile_no = str(countrycode) + str(mobilenumber)
        email= firstname+'official'+'@gmail.com'
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


            print('Group Web - Execution Started')


            driver.get(brandurl)
            time.sleep(5)


            self.dynamicwait(By.ID,'profileNameInput').send_keys(email)
            time.sleep(5)

            driver.find_element(By.XPATH,'//button[@type="submit"][contains(.,"Continue")]').click()
            time.sleep(10)

            self.dynamicwait(By.ID,'signupNameInput').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.ID,'signupPhoneCountryOrRegionCode').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.ID,'signupPhoneInput').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID,'signupPasswordInput').send_keys(password)

            driver.find_element(By.ID,"signupSubmit").click()
            time.sleep(5)

            if self.dynamicwait(By.XPATH,'//input[@placeholder="Enter PIN"]') is None:

                print('Group Web - Execution Completed')

                driver.quit()

                group_resultdata = {"First Name": firstname, "Email": email, "Number": mobile_no,
                                    "Password": password, "message": 'Failed to generated OTP'}

                return group_resultdata

            driver.quit()

            print('Group Web - Execution Completed')

            group_resultdata = {"First Name": firstname,"Email": email,"Number": mobile_no,
                                   "Password": password,"message": 'OTP generated successfully'}
            return group_resultdata


        except:

            print('Group Web - Execution Completed')
            driver.quit()

            group_resultdata = {"First Name": firstname,"Email": email,"Number": mobile_no,
                                   "Password": password,"message": 'Failed to generated OTP'}

            return group_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic

        except:
            return None
