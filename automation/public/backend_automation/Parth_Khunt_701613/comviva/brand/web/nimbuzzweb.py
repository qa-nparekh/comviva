# Nimbuzz URL
# https://web.nimbuzz.com/register
import json

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class NimbuzzWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        mobile_no = str(countrycode) + str(mobilenumber)
        password = firstname + "@1990"


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

            print('Niumbuzz Web - Execution Started')


            self.dynamicwait(By.NAME,'fullName').send_keys(firstname)
            time.sleep(5)

            # driver.find_element(By.NAME,"country_code").send_keys(countrycode)
            #
            # self.Z

            driver.find_element(By.XPATH,'//input[@placeholder="Enter mobile number"]').send_keys(mobilenumber)
            time.sleep(5)


            driver.find_element(By.XPATH,'//input[@placeholder="Enter password"]').send_keys(password)
            time.sleep(5)


            driver.find_element(By.XPATH,'//input[@placeholder="Enter confirm password"]').send_keys(password)
            time.sleep(5)

            driver.find_element(By.XPATH,'//div[@class="label"][contains(.,"Register")]').click()
            time.sleep(5)

            if self.dynamicwait(By.XPATH, '6 digit code')is None:

                print('Niumbuzz Web - Execution Completed')

                driver.quit()

                niumbuzz_resultdata = {"First Name": firstname, "Number": mobile_no,
                                       "Password": password, "message": 'Failed to generated OTP'}

                return niumbuzz_resultdata

            time.sleep(5)
            driver.quit()

            print('Niumbuzz Web - Execution Completed')

            niumbuzz_resultdata = {"First Name": firstname,"Number": mobile_no,
                                   "Password": password,"message": 'OTP generated successfully'}
            return niumbuzz_resultdata

        except:

            print('Niumbuzz Web - Execution Completed')

            driver.quit()

            niumbuzz_resultdata = {"First Name": firstname,"Number": mobile_no,
                                   "Password": password,"message": 'Failed to generated OTP'}

            return niumbuzz_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
