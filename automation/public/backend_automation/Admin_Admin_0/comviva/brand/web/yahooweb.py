# Yahoo URL
# https://login.yahoo.com/account/create?.lang=en-IN&.intl=in&.src=yhelp
import json
from random import choice

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class YahooWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        fullname = firstname + "143007uvc"
        mobile_no = str(countrycode) + str(mobilenumber)
        password = 'yahooo' + "@1990"
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

            print('Yahoo Web - Execution Started')

            self.dynamicwait(By.NAME,'firstName').send_keys(firstname)
            time.sleep(5)


            driver.find_element(By.ID,'usernamereg-lastName').send_keys(lastname)
            time.sleep(5)


            driver.find_element(By.NAME,'userId').send_keys(fullname)
            time.sleep(5)

            driver.find_element(By.NAME,'password').send_keys(password)
            time.sleep(5)

            driver.find_element(By.NAME,"birthYear").send_keys(year)
            time.sleep(5)

            driver.find_element(By.NAME,'signup').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//select[@name="shortCountryCode"]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//select[@name="shortCountryCode"]//option[contains(.,'+"+str(countrycode)+"')]').click()
            time.sleep(5)

            self.dynamicwait(By.NAME, "phone").send_keys(mobilenumber)
            time.sleep(5)

            self.dynamicwait(By.NAME,"signup").click()
            time.sleep(5)

            try:

                driver.find_element(By.XPATH, "//button[contains(.,'Continue')]")
                print('Yahoo Web - Execution Completed')

                driver.quit()

                yahoo_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                    "Password": password, "year": year, "Message": 'Failed to generated OTP'}

                return yahoo_resultdata

            except:

                print("Captcha not found")



            if self.dynamicwait(By.NAME,'code')is None:

                print('Yahoo Web - Execution Completed')

                driver.quit()

                yahoo_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                    "Password": password, "Year": year, "Message": 'Failed to generated OTP'}

                return yahoo_resultdata

            time.sleep(5)
            driver.quit()

            print('Yahoo Web - Execution Completed')

            yahoo_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "Year": year, "Message": 'OTP generated successfully'}
            return yahoo_resultdata



        except:

            print('Yahoo Web - Execution Completed')

            driver.quit()

            yahoo_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "year": year, "message": 'Failed to generated OTP'}

            return yahoo_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None

