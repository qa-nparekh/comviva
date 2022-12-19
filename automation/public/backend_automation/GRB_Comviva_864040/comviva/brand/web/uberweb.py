# Uber URL -
# drivers.uber.com
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class UberWeb:

    def generateOTP(self, brandurl, mobilenumber, countrycode):

        global driver

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

            print('Uber Web - Execution Started')

            self.dynamicwait(By.ID, 'PHONE_NUMBER_or_EMAIL_ADDRESS').send_keys(mobilenumber)
            time.sleep(5)

            self.dynamicwait(By.XPATH,'//div[@id="PHONE_COUNTRY_CODE"]').click()
            time.sleep(10)

            driver.find_element(By.XPATH,"//li[@role='option']//div[contains(.,'+"+str(countrycode)+"')]").click()
            time.sleep(5)

            # self.dynamicwait(By.ID, 'PHONE_NUMBER_or_EMAIL_ADDRESS').send_keys(mobilenumber)
            # time.sleep(5)

            driver.find_element(By.ID, 'forward-button').click()
            time.sleep(5)

            try:

                driver.find_element(By.XPATH, '//button[@id="modal_ok"][@div=contains(.,"OK")]')
                driver.quit()

                print('Uber Web - Execution Completed')

                uber_resultdata = {"Number": mobile_no, "Message": 'Failed to generate OTP'}
                return uber_resultdata

            except:

                print("Captcha not found")

            if self.dynamicwait(By.ID, 'PHONE_SMS_OTP-0') is None:
                print('Uber Web - Execution Completed')

                driver.quit()
                uber_resultdata = {"Number": mobile_no, "Message": 'Failed to generate OTP'}

                return uber_resultdata

            time.sleep(5)
            driver.quit()

            print('Uber Web - Execution Completed')

            uber_resultdata = {"Number": mobile_no, "Message": 'OTP generated successfully'}
            return uber_resultdata

        except:

            print('Uber Web - Execution Completed')

            driver.quit()

            uber_resultdata = {"Number": mobile_no, "Message": 'Failed to generate OTP'}

            return uber_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
