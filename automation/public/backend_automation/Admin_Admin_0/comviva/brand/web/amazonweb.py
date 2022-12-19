# Amzon URL
# https://www.amazon.com

import json

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class AmazonWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        password = firstname + "@1990"
        mobile_no = '+'+str(countrycode) + str(mobilenumber)


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

            print('Amazon Web - Execution Started')


            self.dynamicwait(By.ID,'nav-link-accountList').click()
            time.sleep(5)

            self.dynamicwait(By.ID,'createAccountSubmit').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//input[@name=\"customerName\"]').send_keys(firstname)
            time.sleep(5)

            # driver.find_element(By.XPATH, '//input[@name=\"email\"]').send_keys(mobilenumber)
            # time.sleep(5)

            # driver.find_element(By.XPATH,'//span[@class="country-display-text"]').click()
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH,"//li[@class='a-dropdown-item']//a[contains(.,+"+str(countrycode)+")]").click()
            # time.sleep(5)
            #
            driver.find_element(By.XPATH,'//input[@name=\"email\"]').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.XPATH,'//input[@name=\"password\"]').send_keys(password)
            time.sleep(5)

            driver.find_element(By.XPATH,'//input[@name=\"passwordCheck\"]').send_keys(password)
            time.sleep(5)

            driver.find_element(By.XPATH,'//input[@id=\"continue\"]').click()
            time.sleep(5)

            try:

                driver.find_element(By.XPATH, "// span[contains(., 'Solve this puzzle to protect your account')]")

                driver.quit()

                print('Amazon Web - Execution Completed')

                amazon_resultdata = {"First Name": firstname, "Email": mobilenumber,
                                     "Password": password, "Message": 'Failed to generate OTP'}
                return amazon_resultdata

            except:

                print("Captcha not found")


            if self.dynamicwait(By.XPATH, '//input[@name = "code"]') is None:
                driver.quit()

                print('Amazon Web - Execution Completed')

                amazon_resultdata = {"First Name": firstname, "Email": mobilenumber,
                                     "Password": password, "Message": 'Failed to generate OTP'}
                return amazon_resultdata

            time.sleep(5)
            driver.quit()

            print('Amazon Web - Execution Completed')

            amazon_resultdata = {"First Name": firstname,"Email": mobilenumber,
                                   "Password": password,"Message": 'OTP generated successfully'}
            return amazon_resultdata


        except:
            driver.quit()

            print('Amazon Web - Execution Completed')

            amazon_resultdata = {"First Name": firstname,"Email": mobilenumber,
                                       "Password": password,"Message": 'Failed to generate OTP'}
            return  amazon_resultdata


    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None

