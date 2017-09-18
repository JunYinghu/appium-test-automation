# Selenium Test Automation  - Android (Samsung Note5)

[TestScriptMsge.py](src/TestScriptMsg.py)

1 This document is designed to show how to test APP on Android Device

2 This script is written in Python
   - From technical , You will see
      - how to instantiate class
      - how to inherit class
      - how to set constructor to initialize an instance of a class
      - Get xpath / id of elements from config file

3  The script is doing:
   - Open Message
      - Set a phone number starting conversation
         - send text message
         - send attachment from Gallery
         - take image via camera and send it
         - take a video via camera and sent it

   - Go back to conversation list
        - look for the phone number and delete conversation
   
   - Exit from message

4 Test tools / ENV
   - PyCharm
   - Python
   - Appium
   
5 Tested information:
   - Android (Smasung Note5)
   - Android version 7.0