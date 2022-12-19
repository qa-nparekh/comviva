#Skype URL
# https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1661151965&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%26form%3dmicrosoft_registration%26fl%3dphone2&lc=1033&id=293290&mkt=en-US&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFligh&fl=phone2&lic=1&uaid=b3e6be0e33d74e5283b10f2f428a84ab
import json

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class SkypeWeb:

    def generateOTP(self, brandurl, mobilenumber, countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
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

            print('Skeype Web - Execution Started')

            #self.dynamicwait(By.ID,'phoneSwitch').click()
            #time.sleep(5)


            self.dynamicwait(By.NAME,'PhoneCountry').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, "//select/option[contains(.,'+"+str(countrycode)+"')]").click()
            time.sleep(5)

            # driver.find_element(By.NAME, 'PhoneCountry').send_keys('+91')
            # time.sleep(5)

            driver.find_element(By.XPATH,'//input[@id="MemberName"]').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID,'iSignupAction').click()
            time.sleep(5)

            self.dynamicwait(By.NAME,"Password").send_keys(password)
            time.sleep(5)

            driver.find_element(By.ID,'iSignupAction').click()
            time.sleep(5)

            self.dynamicwait(By.NAME,"FirstName").send_keys(firstname)

            driver.find_element(By.NAME,"LastName").send_keys(lastname)
            time.sleep(5)

            driver.find_element(By.ID, 'iSignupAction').click()
            time.sleep(5)

            if self.dynamicwait(By.XPATH, '//input[@id="VerificationCode"]')is None:

                print('Skeype Web - Execution Completed')

                driver.quit()

                skype_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                    "Password": password, "Message": 'Failed to generated OTP'}

                return skype_resultdata

            time.sleep(5)
            driver.quit()

            print('Skeype Web - Execution Completed')

            skype_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "Message": 'OTP generated successfully'}
            return skype_resultdata


        except:

            print('Skeype Web - Execution Completed')

            driver.quit()

            skype_resultdata = {"First Name": firstname, "Last Name": lastname, "Number": mobile_no,
                                   "Password": password, "Message": 'Failed to generated OTP'}

            return skype_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None

