import unittest

import time
from appium import webdriver


class SimpleAndroidTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['udid'] = "4f833c39"
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'OPPO R11s'
        desired_caps['appPackage'] = 'com.buuuk.st'
        desired_caps['appActivity'] = 'com.sph.straitstimes.views.activities.SplashActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def test_01_dail_number(self):
        print 'nothing is here'
        # self.driver.keyevent(15)
        # self.driver.keyevent(12)
        # self.driver.keyevent(10)
        # self.driver.keyevent(10)
        # self.driver.keyevent(8)
        # self.driver.keyevent(12)
        # self.driver.keyevent(7)
        # self.driver.keyevent(16)
        # self.driver.keyevent(5)

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
