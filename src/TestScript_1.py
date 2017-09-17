import time
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#  os.path.join(os.path.dirname(__file__), p)
# )

SLEEPY_TIME = 1


# Launch chrome browser in Samsung Android
class SimpleAndroidTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Galaxy Note5'
        desired_caps['appPackage'] = 'com.android.chrome'
        desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    # accept terms
    def test_00_confirm_terms_accept(self):
        print self.driver.current_activity
        el = self.driver.find_element_by_id('terms_accept')
        el.click()
        # el = self.driver.find_element_by_accessibility_id('Arcs')
        # self.assertIsNotNone(el)
        # self.driver.back()
        # self.assertIsNotNone(el)
        # els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
        # self.assertGreaterEqual(12, len(els))
        # self.driver.find_element_by_android_uiautomator('text("API Demos")')

    # Ingore email register screen
    def test_01_Reject_Register_email(self):
        print self.driver.current_activity
        el = self.driver.find_element_by_id('signin_title')
        self.assertEqual(el.text, "Sign in to Chrome", "failed")
        el = self.driver.find_element_by_id('negative_button')
        el.click()

        # Key in search keywords

    def test_02_keyin_search_key(self):
        print self.driver.current_activity
        el = self.driver.find_element_by_id('search_box_text')
        el.set_value('Search keywords')
        # press enter to submit keywords.
        # self.driver.keyevent(66)

    # using touch_action to get context keywords
    def test_03_send_search_key(self):
        el = self.driver.find_element_by_id('refine_view_id')
        action = TouchAction(self.driver)
        action.press(el, x=-10, y=0).tap().perform()

    # Close chromme
    def test_04_tearDownClass(self):
        # end the session
        # self.driver.keyevent(4)
        time.sleep(8)
        # print dir (self.driver)  - to get element
        self.driver.quit()

    #    def test_simple_actions(self):


# el = self.driver.find_elemesnt_by_accessibility_id('Graphics')
#    el.click()
#    el = self.driver.find_element_by_accessibility_id('Arcs')
#      el.click()
#     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
