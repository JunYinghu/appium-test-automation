import ConfigParser
import unittest

from appium import webdriver

from SendMessage import SendMessageAll


class SimpleAndroidTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigParser.RawConfigParser(allow_no_value=True)
        cls.config.read('config.txt')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Galaxy Note5'
        desired_caps['appPackage'] = 'com.samsung.android.messaging'
        desired_caps['appActivity'] = 'com.android.mms.ui.ConversationComposerClassification'
        # desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')
        # cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.SendMessageAllProv = SendMessageAll(cls.driver, cls.config)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_01_send_message(self):
        self.SendMessageAllProv.sendtext()
        self.SendMessageAllProv.submitmssage()
        self.SendMessageAllProv.sendimage()
        self.SendMessageAllProv.submitmssage()
        self.SendMessageAllProv.takeimage()
        self.SendMessageAllProv.submitmssage()
        self.SendMessageAllProv.takevideo()
        self.SendMessageAllProv.submitmssage()
        self.SendMessageAllProv.gotocontact()
        self.SendMessageAllProv.checklist()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)
