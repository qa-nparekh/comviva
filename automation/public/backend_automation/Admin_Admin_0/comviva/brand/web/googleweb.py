# Google URL
# https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class GoogleWeb:

    def generateOTP(self, brandurl, mobilenumber, countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        username = firstname + "143007uvc"
        password = firstname + "@123"

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

            print('Google Web - Execution Started')

            self.dynamicwait(By.XPATH, '//span[contains(.,"Create account")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, "//span[contains(.,'For my personal use')]").click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'firstName').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.ID, 'lastName').send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.ID, 'username').clear()
            time.sleep(5)

            driver.find_element(By.ID, 'username').send_keys(username)
            time.sleep(5)

            driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys(password)
            time.sleep(5)

            driver.find_element(By.XPATH, '//input[@name="ConfirmPasswd"]').send_keys(password)
            time.sleep(5)

            driver.find_element(By.XPATH, '//span[contains(.,"Next")]').click()
            time.sleep(15)

            self.dynamicwait(By.XPATH, '//div[@jsname="oYxtQd"]').click()
            time.sleep(7)

            driver.find_element(By.XPATH, '//li//span[contains(.,"'"+"+ str(countrycode) +'")]').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//input[@type="tel"]').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, '//span[contains(.,"Next")]').click()
            time.sleep(5)

            if self.dynamicwait(By.NAME, "code") is None:

                print('Google Web - Execution Completed')

                driver.quit()

                google_resultdata = {"First Name": firstname, "Last Name": lastname, "User Name": username,
                                     "Password": password,
                                     "Confirm Password": password, "Message": 'Failed to generate OTP'}

                return google_resultdata

            time.sleep(5)

            driver.quit()

            print('Googler Web - Execution Completed')

            google_resultdata = {"First Name": firstname, "Last Name": lastname, "User Name": username,
                                 "Password": password,
                                 "Confirm Password": password, "Message": 'OTP generated successfully'}
            return google_resultdata

        except:
            print('Google Web - Execution Completed')

            driver.quit()
            google_resultdata = {"First Name": firstname, "Last Name": lastname, "User Name": username,
                                 "Password": password,
                                 "Confirm Password": password, "Message": 'Failed to generate OTP'}

            return google_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
