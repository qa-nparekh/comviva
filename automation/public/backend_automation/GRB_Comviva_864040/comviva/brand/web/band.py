# Band URL
# https://auth.band.us/phone_sign_up
from datetime import datetime
from random import choice

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class Band:

    def generateOTP(self, brandurl, mobilenumber, countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        password = firstname + "@123"
        mobile_no = str(countrycode) + str(mobilenumber)
        monthrange = list(range(1, 12))
        month_no = choice(monthrange)
        month_object = datetime.strptime(str(month_no), "%m")
        month = month_object.strftime("%B")
        daterange = list(range(1, 29))
        day = choice(daterange)
        yearrange = list(range(1960, 1999))
        year = choice(yearrange)

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

            print('Band Web - Execution Started')

            self.dynamicwait(By.ID, 'selected_region_code').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.ID, 'input_local_phone_number').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID, 'pw').send_keys(password)
            time.sleep(5)

            driver.find_element(By.ID, 'input_name').send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.ID, 'select_year').send_keys(year)
            time.sleep(5)

            driver.find_element(By.ID, 'select_month').send_keys(month)
            time.sleep(5)

            driver.find_element(By.ID, 'select_day').send_keys(day)
            time.sleep(5)

            driver.find_element(By.ID, 'phone_sign_up_form').click()
            time.sleep(5)

            if self.dynamicwait(By.XPATH, 'verification_code') is None:

                print('Band Web - Execution Completed')

                driver.quit()

                band_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "Confirm Password": password,
                                   "Message": 'Failed to generate OTP'}

                return band_resultdata

            time.sleep(5)

            driver.quit()

            print('Band Web - Execution Completed')

            band_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                               "Password": password,"Confirm Password": password, "Message": 'OTP generated successfully'}
            return band_resultdata

        except:
            print('Band Web - Execution Completed')

            driver.quit()
            band_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                               "Password": password,"Confirm Password": password, "Message": 'Failed to generate OTP'}

            return band_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
