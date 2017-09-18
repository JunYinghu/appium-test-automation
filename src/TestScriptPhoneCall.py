import time
import unittest

from appium import webdriver


# Open contacts window in samsung android
class SimpleAndroidTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Galaxy Note5'
        desired_caps['appPackage'] = 'com.samsung.android.contacts'
        desired_caps['appActivity'] = 'com.android.dialer.DialtactsActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    # Dail phone number and calick on call button
    def test_01_dail_number(self):
        self.driver.keyevent(15)
        self.driver.keyevent(12)
        self.driver.keyevent(10)
        self.driver.keyevent(10)
        self.driver.keyevent(8)
        self.driver.keyevent(12)
        self.driver.keyevent(7)
        self.driver.keyevent(16)
        self.driver.keyevent(5)

    # wait for 30 seconds, if no response, call will be end and Close contacts window
    def test_03_tearDownClass(self):
        # end the session
        time.sleep(30)
        self.driver.keyevent(6)
        # to get element
        # print dir (self.driver)
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
