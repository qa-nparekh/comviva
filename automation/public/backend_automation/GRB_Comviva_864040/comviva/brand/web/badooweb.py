# Badoo URL
# https://badoo.com/signup/
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class BadooWeb:

    def generateOTP(self, brandurl , mobilenumber, countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        mobile_no = '+'+str(countrycode) + str(mobilenumber)
        lastname = faker.last_name()
        password = firstname + lastname

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

            print('Badoo Web - Execution Started')

            self.dynamicwait(By.NAME, 'login').send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
            time.sleep(5)

            driver.find_element(By.NAME,'create_profile').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, '//h1[contains(.,"Verify your number")]')
            time.sleep(5)

            driver.find_element(By.XPATH, '//input[@class="text-field__input js-input"]').click()
            time.sleep(5)

            driver.quit()
            print('Badoo Web - Execution Completed')

            badoo_resultdata = {"Number": mobile_no,"Password": password, "Message": 'OTP generated successfully'}
            return badoo_resultdata

        except:
            print('Badoo Web - Execution Completed')

            driver.quit()
            badoo_resultdata = {"Number": mobile_no,"Password": password, "Message": 'Failed to generate OTP'}

            return badoo_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
