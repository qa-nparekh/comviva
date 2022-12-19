# Airbnd URL
# https://www.airbnb.co.in/

import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth

import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class AirbnbWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

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

            print('Airbnb Web - Execution Started')

            self.dynamicwait(By.XPATH,'//button[@data-testid="cypress-headernav-profile"]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH,"//div[@id='simple-header-profile-menu']//div/a[contains(.,'Sign up')]").click()
            time.sleep(5)

            self.dynamicwait(By.ID,'country').click()
            time.sleep(5)

            driver.find_element(By.XPATH,"//select/option[contains(.,'+"+str(countrycode)+"')]").click()
            time.sleep(5)

            driver.find_element(By.ID,'phoneInputphoneNumber').send_keys(mobilenumber)
            time.sleep(5)


            driver.find_element(By.CLASS_NAME,'_kaq6tx').click()
            time.sleep(5)

            if self.dynamicwait(By.ID,"phone-verification-code-form__code-input") is None:

                print('Airbnb Web - Execution Completed')

                driver.quit()
                airbnb_resultdata = {"Number": mobile_no, "Message": 'Failed to generated OTP'}

                return airbnb_resultdata

            time.sleep(5)
            driver.quit()

            print('Airbnb Web - Execution Completed')

            airbnb_resultdata = {"Number": mobile_no,"Message": 'OTP generated successfully'}
            return airbnb_resultdata


        except:

            print('Airbnb Web - Execution Completed')

            driver.quit()
            airbnb_resultdata = {"Number": mobile_no,"Message": 'Failed to generated OTP'}

            return airbnb_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None


