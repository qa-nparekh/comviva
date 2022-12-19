#1XBET URL
# https://in.1x001.com/en
import json
import datetime

from random import choice


from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class XBetWeb:

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
            time.sleep(15)

            print('1XBET Web - Execution Started')

            self.dynamicwait(By.XPATH,'//a[@class="btn user-control-panel__item btn--size-m btn--theme-accent btn--rounded"]//span[@class="caption__label"][contains(.,"Registration")]').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, "(//span[contains(.,'By phone')])[2]").click()
            time.sleep(5)

            driver.find_element(By.XPATH,'//span[@class="caption dropdown-phone-codes-container__code caption--size-m"]//span[@class="caption__label"]').clear()
            time.sleep(5)

            driver.find_element(By.XPATH,'//span[@class="caption dropdown-phone-codes-container__code caption--size-m"]//span[@class="caption__label"]').send_keys(countrycode)
            time.sleep(5)

            driver.find_element(By.XPATH,'//input[@name="phone"]').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.XPATH, "//span[@class='caption caption--size-xs']//span[contains(.,'Send SMS')]").click()
            time.sleep(5)

            if self.dynamicwait(By.XPATH,"//h2[contains(.,'Done')]")is None:

                print('1XBET Web - Execution Completed')

                driver.quit()

                xbet_resultdata = {"Number": mobile_no, "message": 'Failed to generated OTP'}

                return xbet_resultdata

            time.sleep(5)

            driver.quit()

            print('1XBET Web - Execution Completed')

            xbet_resultdata = {"Number": mobile_no,"message": 'OTP generated successfully'}
            return  xbet_resultdata

        except:

            print('1XBET Web - Execution Completed')

            driver.quit()
            xbet_resultdata = {"Number": mobile_no,"message": 'Failed to generated OTP'}

            return xbet_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
