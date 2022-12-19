# Twitter URL
# https://twitter.com/
import json
import datetime

from random import choice


from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class TwitterWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        mobile_no = '+'+str(countrycode) + str(mobilenumber)
        monthrange = list(range(1,12))
        month_no = choice(monthrange)
        month_object = datetime.datetime.strptime(str(month_no), "%m")
        month = month_object.strftime("%B")
        daterange = list(range(1,29))
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
            time.sleep(15)

            print('Twitter Web - Execution Started')

            self.dynamicwait(By.XPATH,"//a[@role='link']").click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//input[@name="name"]').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.NAME,'phone_number').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.ID,'SELECTOR_1').send_keys(month)
            time.sleep(5)

            driver.find_element(By.ID,'SELECTOR_2').send_keys(day)
            time.sleep(5)

            driver.find_element(By.ID,"SELECTOR_3").send_keys(year)
            time.sleep(5)

            driver.find_element(By.XPATH,'(//span[contains(.,"Next")])[2]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '(//span[contains(.,"Next")])[2]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '(//span[contains(.,"Sign up")])[2]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '(//span[contains(.,"OK")])[2]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,"(//span[contains(.,'Enter it below to verify ')])[2]")
            time.sleep(5)



            try:

                driver.find_element(By.XPATH, "// button[contains(.,'Authenticate')]")

                print('Twitter Web - Execution Completed')

                driver.quit()

                twitter_resultdata = {"First Name": firstname, "Number": mobile_no,
                                      "Year": year, "Message": 'Failed to generated OTP'}

                return twitter_resultdata


            except:

                print("Captcha not found")


            if driver.find_element(By.NAME, "verfication_code")is None:

                print('Twitter Web - Execution Completed')

                driver.quit()

                twitter_resultdata = {"First Name": firstname, "Number": mobile_no,
                                      "Year": year, "Message": 'Failed to generated OTP'}

                return twitter_resultdata

            time.sleep(5)
            driver.quit()

            print('Twitter Web - Execution Completed')

            twitter_resultdata = {"First Name": firstname, "Number": mobile_no,
                                       "Year": year ,"Message": 'OTP generated successfully'}
            return  twitter_resultdata

        except:

            print('Twitter Web - Execution Completed')

            driver.quit()
            twitter_resultdata = {"First Name": firstname, "Number": mobile_no,
                                   "Year": year, "Message": 'Failed to generated OTP'}

            return twitter_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
