import time

from appium.webdriver.common.touch_action import TouchAction

section = 'sendmessage'
from GetPath import GetPath


class SendMessageAll(GetPath):
    def __init__(self, driver, config):
        GetPath.__init__(self, driver, config)

    def clickAttBut(self):
        attachButtonId = 'attach'
        attachButton = self.driver.find_element_by_id(self.getPath(section, attachButtonId))
        attachButton.click()

    def selectRecipient(self):
        recipient_id = 'recipient'
        recepient = self.driver.find_element_by_id(self.getPath(section, recipient_id))
        recepient.set_value("85331509")

    def submitMssage(self):
        sentButtonid = 'sendbutton'
        send_button = self.driver.find_element_by_id(self.getPath(section, sentButtonid))
        send_button.click()

    def sendText(self):
        self.selectRecipient()
        textMessageBox = 'sendmessage'
        send_message = self.driver.find_element_by_id(self.getPath(section, textMessageBox))
        send_message.set_value("hello, this is from rabot")

    def sendImage(self):
        # self.selectRecipient()
        self.clickAttBut()
        self.driver.get_screenshot_as_file('sendimage.png')
        self.driver.tap([(108, 1509)])
        moreMenuid = 'moremenu'
        moreMenu = self.driver.find_element_by_id(self.getPath(section, moreMenuid))
        moreMenu.click()
        time.sleep(3)
        self.driver.tap([(188, 986)])
        # canncel select attachment
        time.sleep(3)
        # self.driver.tap([(108, 1669)])

    def takeImage(self):
        # self.selectRecipient()
        time.sleep(5)
        self.clickAttBut()
        # self.driver.get_screenshot_as_file('takeimage.png')
        # self.driver.tap([(228, 1846)])
        cramerbut = 'cramer'
        takeimage = self.driver.find_element_by_xpath(self.getPath(section, cramerbut))
        takeimage.click()

        time.sleep(5)
        takeimagebut = 'takeimage'
        takeimage = self.driver.find_element_by_id(self.getPath(section, takeimagebut))
        takeimage.click()
        time.sleep(5)

    def takeVideo(self):
        # self.selectRecipient()
        time.sleep(5)
        #self.clickAttBut()
        #self.driver.get_screenshot_as_file('record.png')
        #self.driver.tap([(200, 1883)])
        time.sleep(2)
        #cramerbut = 'cramer'
        #takeimage = self.driver.find_element_by_xpath(self.getPath(section, cramerbut))
        #takeimage.click()
        recordstartid = 'record'
        recordstart = self.driver.find_element_by_id(self.getPath(section, recordstartid))
        recordstart.click()
        recordstopid = 'stoprecord'
        recordstop = self.driver.find_element_by_accessibility_id(self.getPath(section, recordstopid))
        time.sleep(3)
        recordstop.click()
        # self.driver.tap([(542, 1757)])
        time.sleep(10)

    def goToContact(self):
        time.sleep(10)
        gobackid = 'arrow'
        section = 'list'
        goback = self.driver.find_element_by_id(self.getPath(section, gobackid))
        goback.click()
        time.sleep(10)

    def goToContact(self):
        time.sleep(2)
        section = 'list'
        gobackid = 'arrow'
        goback = self.driver.find_element_by_id(self.getPath(section, gobackid))
        goback.click()

    def checkList(self):
        section = 'list'
        pageSource = self.driver.page_source
        searchtextbox = 'searchtext'
        searchtextboxinput = self.driver.find_element_by_id(self.getPath(section, searchtextbox))
        # searchtextboxinput.set_value('3')
        action = TouchAction(self.driver)
        action.long_press(x=669, y=445, duration=2000).perform()
        self.driver.tap([(856, 125)])
        time.sleep(2)
        self.driver.tap([(883, 1053)])
        time.sleep(2)