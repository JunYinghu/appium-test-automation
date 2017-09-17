import time

from appium.webdriver.common.touch_action import TouchAction

from SendMessage import SendMessageAll

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
        searchtextboxinput.set_value('85331509')
        action = TouchAction(self.driver)
        action.press(searchtextboxinput, x=103, y=183),100

        time.sleep(10)
