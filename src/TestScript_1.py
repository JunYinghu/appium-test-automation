import os
import sys
import time
from time import sleep

import glob
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


# Returns abs path relative to this file and not cwd
#PATH = lambda p: os.path.abspath(
  #  os.path.join(os.path.dirname(__file__), p)
#)

SLEEPY_TIME = 1

class SimpleAndroidTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Galaxy Note5'
        desired_caps['appPackage'] = 'com.android.chrome'
        desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    @classmethod
        
    def test_00_confirm_terms_accept(self):
        el = self.driver.find_element_by_id('terms_accept')
        el.click()
		
        # el = self.driver.find_element_by_accessibility_id('Arcs')
        # self.assertIsNotNone(el)

        # self.driver.back()

        # el = self.driver.find_element_by_accessibility_id("App")
        # self.assertIsNotNone(el)

        # els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
        # self.assertGreaterEqual(12, len(els))

        # self.driver.find_element_by_android_uiautomator('text("API Demos")')
		
    def test_01_Reject_Register_email(self):
        el = self.driver.find_element_by_id('signin_title')
        self.assertEqual(el.text, "Sign in to Chrome", "failed")
        el = self.driver.find_element_by_id('negative_button')
        el.click()        
    
    def test_02_keyin_search_key(self): 
        el = self.driver.find_element_by_id('search_box_text')
        el.set_value('Search keywords')
                
    def test_03_send_search_key(self):     
        el = self.driver.find_element_by_id('refine_view_id')
        action = TouchAction(self.driver)
        action.press(el, x=-10, y=0).tap().perform()
        self.driver.current_context
        self.driver.contexts        
        #a1 = TouchAction()
        #a1.press(el) \
            #.move_to(x=-30, y=0) \
            #.wait(3000) \
            #.tap(a1).perform()
        #self.driver.implicitly_wait(6000)
        
    def test_04_tearDownClass(cls):
        #end the session
        time.sleep(10)
        cls.driver.quit()       
 
        
#def test_simple_actions(self):
#    el = self.driver.find_element_by_accessibility_id('Graphics')
#    el.click()
#
#    el = self.driver.find_element_by_accessibility_id('Arcs')
#      el.click()

#     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    suite.sortTestMethodsUsing=None
    unittest.TextTestRunner(verbosity=2).run(suite)
