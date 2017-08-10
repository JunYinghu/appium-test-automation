
var wd = require('wd'),
    desiredCaps = {
        platformVersion: '6.0.1',
        platformName: 'Android',
        name: 'Sample Test',
		deviceName: 'Galaxy Note5',
		appPackage: 'com.android.chrome',
		appActivity:'com.google.android.apps.chrome.Main',
    },
    driver = wd.remote("http://127.0.0.1:4723/wd/hub");
 
driver.init(desiredCaps, function(error) {
   
    
    if (error) {
        throw new Error('Session did not start properly. Please make sure you sauce credentials are correct');
    }
    //driver.quit();
});
 driver.elementByid('com.android.chrome:id/terms_accept')
//driver.init(desired)






//var button = driver.elementById('com.android.chrome:id/terms_accept');
//button.onclick();