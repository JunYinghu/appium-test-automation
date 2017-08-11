# Chrome Android Test Automation Plan


1  This project is designed to make more practice on automation testing.

2  This automation test scripts were written in Python.

##  Case 1 - [Script](../src/TestScript_1.py)

1  The script is doing this:

   - Opens Chrome browser on Android device
   - Search Accept&Continue button via find_element_by_id,
     Click the button going to user email registration page
   - If text matches 'sing in...' then user to escape the page user does not want.
     Clicks 'No Thanks' button to exit
   - Set search keyword in search box on default page (google screen).
     tap on search keyword via action move     
   - Exit from browser,
     Wait 10 second to confirm search result as the above
   
2 Test tools / ENV
   - Pycharm
   - Python
   - Appium   
   
3 Tested device information:
   - Samsung Note 5
   - Version 6.0.1

   
    
##  Case 2 - [Script](../src/TestScript_Phone.py)
   
1  The script is doing this:
   - Launch Contacts window
   - Dail Phone number and make a call
   - If there is no response within 30 seconds, call will be ended.
   - Close Contacts window
   
2 Test tools / ENV
   - Pycharm
   - Python
   - Appium   
   
3 Tested device information:
   - Samsung Note 5
   - Version 6.0.1
   
