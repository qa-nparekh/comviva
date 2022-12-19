# Commsease URL
# https://id.commsease.com/register?h=media&t=media&from=commsease%7Chttps%3A%2F%2Fdoc.commsease.com%2Fen%2Fmessaging%2Fdocs%2FDQ3Nzk1MTY&clueFrom=overseas&locale=en_US&i18nEnable=true&referrer=https%3A%2F%2Fconsole.commsease.com
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class CommseaseWeb:

    def generateOTP(self, brandurl, mobilenumber, countrycode):

        global driver

        mobile_no = str(countrycode) + str(mobilenumber)

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

            print('Commsease Web - Execution Started')

            self.dynamicwait(By.XPATH, "//div[@class='m-select-value  phone-select']").send_keys()
            time.sleep(5)

            driver.find_element(By.XPATH, "//input[@class='m-input m-input-large phone m-phone-input']").click()
            time.sleep(5)

            driver.find_element(By.XPATH, "//span[contains(.,'Click the button to verify')]").click()
            time.sleep(5)

            if self.dynamicwait(By.XPATH, "//input[@class='m-input m-input-large sms']") is None:

                print('Commsease Web- Execution Completed')

                driver.quit()

                commsease_resultdata = {"Number": mobile_no, "Message": 'Failed to generate OTP'}

                return commsease_resultdata

            time.sleep(5)
            driver.quit()

            print('Commsease Web - Execution Completed')

            commsease_resultdata = {"Number": mobile_no,"Message": 'OTP generated successfully'}
            return commsease_resultdata

        except:
            print('Commsease Web- Execution Completed')

            driver.quit()
            commsease_resultdata = {"Number": mobile_no,"Message": 'Failed to generate OTP'}

            return commsease_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
