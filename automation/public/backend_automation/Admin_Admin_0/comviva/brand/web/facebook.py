# Facebook URL
# https://www.facebook.com

import json
from random import choice

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class FaceBookWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        mobile_no = str(countrycode) + str(mobilenumber)
        password = firstname + "@1990"
        year = '1990'

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

            print('Facebook Web - Execution Started')


            self.dynamicwait(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
            time.sleep(5)

            self.dynamicwait(By.NAME,'firstname').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.NAME,'lastname').send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.NAME,'reg_email__').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.NAME,'reg_passwd__').send_keys(password)
            time.sleep(5)

            ddelement = Select(driver.find_element(By.ID,'year'))
            ddelement.select_by_visible_text(year)

            driver.find_element(By.XPATH,"//input[@name='sex'][@value=2]").click()
            time.sleep(5)

            self.dynamicwait(By.NAME,'websubmit').click()
            time.sleep(60)

            try:

                self.dynamicwait(By.XPATH,"//span[contains(.,'Continue')]/../../div").click()
                time.sleep(10)
                driver.switch_to.frame(0)
                time.sleep(5)
                driver.switch_to.frame(0)
                driver.find_element(By.XPATH,"//*[@id='recaptcha-anchor']/div").click()
                time.sleep(10)
                driver.switch_to.default_content()
                self.dynamicwait(By.XPATH,"//span[contains(.,'Continue')]/../../div").click()
                time.sleep(10)
                self.dynamicwait(By.NAME,"contactpoint").send_keys(mobilenumber)
                time.sleep(5)
                driver.find_element(By.XPATH,"//span[contains(., 'Send Login Code')] /../../ div").click()
                time.sleep(10)
                driver.quit()

                print('Facebook Web - Execution Completed')

                facebook_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                       "Password": password, "year": year ,"Message": 'OTP generated successfully'}
                return  facebook_resultdata

            except:

                self.dynamicwait(By.XPATH, "//input[@name='code']").click()
                time.sleep(10)

                driver.quit()

                print('Facebook Web - Execution Completed')

                facebook_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                       "Password": password, "year": year, "Message": 'OTP generated successfully'}

                return facebook_resultdata

        except:

            print('Facebook Web - Execution Completed')

            driver.quit()

            print("Failed to generate OTP for Facebook !!! ")
            facebook_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "year": year, "message": 'Failed to generated OTP'}

            return facebook_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
