# Ding URL
# https://www.ding.com/register
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class DingWeb:

    def generateOTP(self, brandurl, mobilenumber,countrycode):

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

            print('Ding Web - Execution Started')

            try:

                self.dynamicwait(By.XPATH, "//button[contains(.,'Accept Cookies')]").click()
                time.sleep(5)

                self.dynamicwait(By.XPATH,'//button[@data-testid="button-login-register-phone"]').click()
                time.sleep(5)

                self.dynamicwait(By.XPATH, '//input[@data-testid="phone-widget-input"]').clear()
                time.sleep(5)

                # driver.find_element(By.XPATH, '//div[@class="sc-eKBdFk bGfJJM"]').click()
                # time.sleep(5)

                # driver.find_element(By.XPATH,'//input[@data-testid="phone-widget-input"]').send_keys("+255")
                # time.sleep(5)
                #
                # driver.find_element(By.XPATH, '//div[@class="sc-eKBdFk bGfJJM"]').click()
                # time.sleep(5)

                # driver.find_element(By.XPATH, "//div[@data-element='dropdownlist']//div[contains(@text='255']").click()
                # time.sleep(5)

                driver.find_element(By.XPATH, '//input[@data-testid="phone-widget-input"]').send_keys(mobile_no)
                time.sleep(5)

                driver.find_element(By.XPATH,'//div[@data-testid="right"]').click()
                time.sleep(5)

                driver.find_element(By.XPATH,"//section[contains(.,'Confirm phone number')]").click()
                time.sleep(5)

                if self.dynamicwait(By.XPATH,'//input[@data-testid="sms-0-element"]') is None:

                    print('Ding Web - Execution Completed')

                    driver.quit()

                    ding_resultdata = {"Number": mobile_no, "Message": 'Failed to generated OTP'}

                    return ding_resultdata

                time.sleep(5)

                print('Ding Web - Execution Completed')

                driver.quit()

                ding_resultdata = {"Number":mobile_no,"Message": 'OTP generated successfully'}
                return ding_resultdata

            except:

                self.dynamicwait(By.XPATH, '//button[@data-testid="button-login-register-phone"]').click()
                time.sleep(5)

                self.dynamicwait(By.XPATH, '//input[@data-testid="phone-widget-input"]').clear()
                time.sleep(5)

                driver.find_element(By.XPATH, '//input[@data-testid="phone-widget-input"]').send_keys(mobile_no)
                time.sleep(5)

                driver.find_element(By.XPATH, '//div[@data-testid="right"]').click()
                time.sleep(5)

                driver.find_element(By.XPATH, "//section[contains(.,'Confirm phone number')]").click()
                time.sleep(5)

                if self.dynamicwait(By.XPATH, '//input[@data-testid="sms-0-element"]') is None:

                    print('Ding Web - Execution Completed')

                    driver.quit()

                    ding_resultdata = {"Number": mobile_no, "Message": 'Failed to generated OTP'}

                    return ding_resultdata

                time.sleep(5)

                print('Ding Web - Execution Completed')

                driver.quit()

                ding_resultdata = {"Number": mobile_no, "Message": 'OTP generated successfully'}
                return ding_resultdata

        except:

            print('Ding Web - Execution Completed')

            driver.quit()

            ding_resultdata = {"Number":mobile_no,"Message": 'Failed to generated OTP'}

            return ding_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None

