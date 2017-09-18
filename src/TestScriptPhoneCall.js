
var wd = require('wd'),
    desiredCaps = {
         platformVersion: '6.0.1',
        platformName: 'Android',
        name: 'Sample Test',
		deviceName: 'Galaxy Note5',
		appPackage: 'com.android.contacts',
        appActivity:'com.android.dialer.DialtactsActivity'
    },
    driver = wd.remote("http://127.0.0.1:4723/wd/hub");
 
driver.init(desiredCaps, function(error) {


    if (error) {
        throw new Error('Session did not start properly. Please make sure you sauce credentials are correct');
    }
    //driver.quit();
});

driver.elementById('com.android.contacts:id/one');




//driver.init(desired)

//element(By.id("com.android.contacts:id/one")).click();
