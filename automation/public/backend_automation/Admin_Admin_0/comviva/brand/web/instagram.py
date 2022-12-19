#InstagramWeb URL
# https://www.instagram.com/accounts/emailsignup/?hl=en
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


class InstagramWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        fullname = firstname+lastname
        mobile_no = str(countrycode) + str(mobilenumber)
        username = firstname+lastname+"143007uvc"
        password = firstname + "@1990"
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

            print('Instagram Web - Execution Started')

            self.dynamicwait(By.NAME,'emailOrPhone').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.NAME,'fullName').send_keys(fullname)
            time.sleep(5)

            driver.find_element(By.NAME,'username').send_keys(username)
            time.sleep(5)

            driver.find_element(By.NAME,'password').send_keys(password)
            time.sleep(5)

            driver.find_element(By.XPATH,"//button[contains(.,'Sign up')]").click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,"//select[@title='Year:']").send_keys(year)
            time.sleep(5)

            driver.find_element(By.XPATH,"//button[contains(.,'Next')]").click()
            time.sleep(5)

            try:

                driver.find_element(By.XPATH, '//button[@id="modal_ok"][@div=contains(.,"OK")]')

                print('Instagram Web - Execution Completed')

                # driver.quit()

                instagram_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                        "Password": password, "year": year, "message": 'Failed to generated OTP'}

                return instagram_resultdata

            except:

                print("Captcha not found")


            if self.dynamicwait(By.NAME,"confirmationCode") is None:

                print('Instagram Web - Execution Completed')

                # driver.quit()

                instagram_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                        "Password": password, "year": year, "Message": 'Failed to generated OTP'}

                return instagram_resultdata

            time.sleep(5)

            # driver.quit()

            print('Instagram Web - Execution Completed')

            instagram_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "year": year, "Message": 'OTP generated successfully'}

            return instagram_resultdata

        except:

            print('Instagram Web - Execution Completed')

            # driver.quit()
            instagram_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "year": year, "message": 'Failed to generated OTP'}

            return instagram_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
