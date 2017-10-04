import unittest

from appium import webdriver

class Arwiz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.1.2'
        desired_caps['deviceName'] = 'GT-I9300'
        desired_caps['appPackage'] = 'com.android.vending'
        desired_caps['appActivity'] = 'com.android.vending.AssetBrowserActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    @classmethod
    # def tearDown(self):
    #     self.driver.quit()

    def test_01_dail_number(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Arwiz)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)