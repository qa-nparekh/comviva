# Wire URL
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class WireWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        mobile_no = str(countrycode) + str(mobilenumber)
        password = firstname + "@1990"
        year = '2010'

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

            print('Wire Web - Execution Started')

            self.dynamicwait(By.XPATH,'//button[@data-uie-name="go-set-account-type"][contains(.,"Create account")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,"//span[@class='css-bym692'][contains(.,'Wire for Free')]").click()
            time.sleep(5)

            driver.quit()

            print('Wire Web - Execution Completed')

            wire_resultdata = {"First Name": firstname, "Last Name": lastname, "Email": mobile_no,
                                   "Password": password, "year": year, "message": 'OTP generated successfully'}
            return wire_resultdata


        except:

            print('Wire Web - Execution Completed')

            driver.quit()

            wire_resultdata = {"First Name": firstname, "Last Name": lastname, "Email": mobile_no,
                                   "Password": password, "year": year, "message": 'Failed to generated OTP'}

            return wire_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
