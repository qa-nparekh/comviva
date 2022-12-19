# Youtube URL
# https://accounts.google.com/v3/signin/identifier?dsh=S1493259902%3A1662208948274796&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Faccount%26feature%3Dredirect_login&hl=en&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQN2RmXtnIE1v0ZbwzNoe44D-XZQN4Mp704ewJ3rHayaCD-XBg0BibooUnWQYYl1IzQ3dNWI7nNhVQ

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class YoutubeWeb:

    def generateOTP(self, brandurl, mobilenumber, countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        username = firstname + "143007uvc"+'@gmail.com'
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

            print('Youtube Web - Execution Started')

            self.dynamicwait(By.XPATH, '//span[contains(.,"Create account")]').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '//span[contains(.,"For my personal use")]').click()
            time.sleep(5)

            self.dynamicwait(By.ID, 'firstName').send_keys(firstname)
            time.sleep(5)

            driver.find_element(By.ID, 'lastName').send_keys(lastname)
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

            self.dynamicwait(By.XPATH, '//span[contains(.,"Next")]').click()
            time.sleep(5)

            if self.dynamicwait(By.NAME, "code") is None:

                print('Youtube Web - Execution Completed')

                driver.quit()

                youtube_resultdata = {"First Name": firstname, "Last Name": lastname, "User Name": username,
                                      "Password": password,
                                      "Confirm Password": password, "Message": 'Failed to generate OTP'}

                return youtube_resultdata

            time.sleep(5)
            driver.quit()

            print('Youtube Web - Execution Completed')

            youtube_resultdata = {"First Name": firstname, "Last Name": lastname, "User Name": username,
                                 "Password": password,
                                 "Confirm Password": password, "Message": 'OTP generated successfully'}
            return youtube_resultdata

        except:

            print('Youtube Web - Execution Completed')

            driver.quit()

            youtube_resultdata = {"First Name": firstname, "Last Name": lastname, "User Name": username,
                                 "Password": password,
                                 "Confirm Password": password, "Message": 'Failed to generate OTP'}

            return youtube_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
