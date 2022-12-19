import json
import time

from comviva.config import config

from appium import webdriver as appDriver


class Runner:

    def executeRequest(self):
        desired_caps = {

            'udid': config.udid,
            'platformName': 'android',

            # 'appPackage': 'com.facebook.katana',
            # 'appActivity': 'com.facebook.account.login.activity.SimpleLoginActivity',

            # 'appPackage': 'com.coinbase.android', - Locator Issue
            # 'appActivity': 'com.coinbase.android.MainActivity',

            #'appPackage': ' org.telegram.messenger', - Try by giving path of Apk
            #'appActivity':'org.telegram.messenger.DefaultIcon',

            'appPackage': 'com.snapchat.android',
            'appActivity': 'com.snap.mushroom.MainActivity',
            # 'app': r'C:\comviva\project_comviva\comviva\data\apk\facebook.apk',
            'autoGrantPermissions': 'true'
        }

        # adb shell dumpsys window | find "mCurrentFocus"

        print('App - Execution Started')

        driver = appDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

otpRunner = Runner()
otpRunner.executeRequest()
