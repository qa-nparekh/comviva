# Telegram URL
# https://web.telegram.org/k/
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


class TelegramWeb:

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

            print('Telegram Web - Execution Started')

            self.dynamicwait(By.XPATH,"(//div[@class='input-field-input'])[2]").clear()
            time.sleep(5)

            driver.find_element(By.XPATH, "(//div[@class='input-field-input'])[2]").send_keys(mobile_no)
            time.sleep(5)

            driver.find_element(By.XPATH,"//span[contains(.,'Next')]").click()
            time.sleep(5)

            if self.dynamicwait(By.NAME,'//input[@class="input-field-input"]') is None:

                print('Telegram Web - Execution Completed')

                driver.quit()

                twitter_resultdata = {"Number": mobile_no, "message": 'Failed to generated OTP'}

                return twitter_resultdata

            time.sleep(5)

            driver.quit()

            print('Telegram Web - Execution Completed')

            telegram_resultdata = {"Number": mobile_no,"message": 'OTP generated successfully'}
            return  telegram_resultdata

        except:

            print('Telegram Web - Execution Completed')

            driver.quit()

            twitter_resultdata = {"Number": mobile_no,"message": 'Failed to generated OTP'}

            return twitter_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
