import time

from appium.webdriver.common.touch_action import TouchAction

from src.utiliDict.SendMessage import SendMessageAll

section = 'list'


class ContactList(SendMessageAll):
    def __init__(self, driver, config):
        SendMessageAll.__init__(self, driver, config)

    def goToContact(self):
        time.sleep(2)
        gobackid = 'arrow'
        goback = self.driver.find_element_by_id(self.getPath(section, gobackid))
        goback.click()

    def checklist(self):
        pageSource = self.driver.page_source
        searchtextbox = 'searchtext'
        searchtextboxinput = self.driver.find_element_by_id(self.getPath(section, searchtextbox))
        searchtextboxinput.set_value('3')
        action = TouchAction(self.driver)
        action.long_press(x=669, y=500, duration=2000).perform()
        # self.driver.tap([(699, 385)])
        # self.driver.flick(430, 143, 708, 372)

        # phonenumberid = 'phonenumber'
        # selectphone = self.driver.find_element_by_id(self.getPath(section, phonenumberid))
        # action.long_press(selectphone)

        time.sleep(10)
