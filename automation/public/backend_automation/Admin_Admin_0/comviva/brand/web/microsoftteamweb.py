#  MicrosoftteamURL
# https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26mkt%3dEN-US%26opid%3dE1C4FAD9D6AF98B4%26opidt%3d1662450211%26uaid%3df7e93e1baf48418bbb681ceb04a62c04%26opignore%3d1&mkt=EN-US&uiflavor=web&lw=1&fl=easi2&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&uaid=f7e93e1baf48418bbb681ceb04a62c04&suc=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&lic=1
import json
from datetime import datetime
from random import choice

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from config.config import chrome_driver_path


class MicrosoftteamWeb:

    def generateOTP(self, brandurl, mobilenumber, countrycode):

        global driver

        faker = Faker()
        firstname = faker.first_name_male()
        lastname = faker.last_name()
        mobile_no = str(countrycode) + str(mobilenumber)
        password = firstname + "@1990"

        monthrange = list(range(1, 12))
        month_no = choice(monthrange)
        month_object = datetime.strptime(str(month_no), "%m")
        month = month_object.strftime("%B")

        daterange = list(range(1, 29))
        day = choice(daterange)

        yearrange = list(range(1960, 1999))
        year = choice(yearrange)

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

            print('MicrosoftTeam Web - Execution Started')

            self.dynamicwait(By.ID,'phoneSwitch').click()
            time.sleep(5)

            driver.find_element(By.NAME, 'PhoneCountry').click()
            time.sleep(5)

            self.dynamicwait(By.XPATH, "//select/option[contains(.,'+"+str(countrycode)+"')]").click()
            time.sleep(5)

            driver.find_element(By.NAME,'MemberName').send_keys(mobilenumber)
            time.sleep(5)

            driver.find_element(By.ID,'iSignupAction').click()
            time.sleep(5)


            self.dynamicwait(By.ID,"PasswordInput").send_keys(password)
            time.sleep(5)


            driver.find_element(By.ID,'iSignupAction').click()
            time.sleep(5)

            #self.dynamicwait(By.NAME,"FirstName").send_keys(firstname)
            #time.sleep(5)

            #driver.find_element(By.NAME,"LastName").send_keys(lastname)
            #time.sleep(10)

            #driver.find_element(By.ID, 'iSignupAction').click()
            #time.sleep(10)

            #self.dynamicwait(By.NAME, 'Country').send_keys('India')
            #driver.quit()

            #driver.find_element(By.ID,'BirthDay').send_keys(day)
            #time.sleep(10)

            #driver.find_element(By.ID, 'BirthMonth').send_keys(month)
            #time.sleep(10)

            #driver.find_element(By.ID, 'BirthYear').send_keys(year)
            #time.sleep(10)

            #driver.find_element(By.ID, 'iSignupAction').click()
            #time.sleep(10)

            if self.dynamicwait(By.ID, 'VerificationCode')is None:

                print('MicrosoftTeam Web - Execution Completed')

                driver.quit()

                # microsoftteam_resultdata = {"First Name": firstname, "Last Name": lastname, "Email": mobile_no,
                #                             "Password": password, "year": year, "message": 'Failed to generated OTP'}
                #
                # return microsoftteam_resultdata

                microsoftteam_resultdata = {"Number": mobile_no, "Password": password,
                                            "Message": 'Failed to generated OTP'}
                return microsoftteam_resultdata

            time.sleep(5)
            driver.quit()

            print('MicrosoftTeam Web - Execution Completed')


            # microsoftteam_resultdata = {"First Name": firstname, "Last Name": lastname, "Email": mobile_no,
            #                        "Password": password, "year": year, "message": 'OTP generated successfully'}
            # return microsoftteam_resultdata

            microsoftteam_resultdata = {"Number": mobile_no, "Password": password,
                                        "Message": 'OTP generated successfully'}
            return microsoftteam_resultdata



        except:

            print('MicrosoftTeam Web - Execution Completed')

            driver.quit()

            # microsoftteam_resultdata = {"First Name": firstname, "Last Name": lastname, "Email": mobile_no,
            #                        "Password": password, "year": year, "message": 'Failed to generated OTP'}
            #
            # return microsoftteam_resultdata

            microsoftteam_resultdata = {"Number": mobile_no, "Password": password,
                                        "message": 'Failed to generated OTP'}
            return microsoftteam_resultdata

    def dynamicwait(self, locatorType=None, locatorName=None):
        try:
            waitfordynamic = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((locatorType, locatorName)))
            return waitfordynamic
        except:
            return None
