from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def configChecker():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    str1 = driver.capabilities['browserVersion']
    str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    print(str1)
    print(str2)
    print(str1[0:3])
    print(str2[0:3])
    if str1[0:2] != str2[0:2]: 
        return False
    return True
