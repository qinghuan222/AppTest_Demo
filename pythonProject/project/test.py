import time
from selenium.webdriver.common.by import By
from appium import webdriver
from pythonProject.project.Login import Login_app
from pythonProject.project.Swip import *


desired_caps = {
            'platformName': 'Android',  # 设备类型；
            'platformVersion': '10',  # 设备的类型的版本号
            'deviceName': '597331de',  # 设备的名称
            'appPackage': 'com.app.huibo',  # 的app包名；
            'appActivity': 'module.main.WelcomeActivity',  #activity名
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
Login_app(driver).login1("15000000033", "a123456")
# l = driver.get_window_size()
# x1 = l['width'] * 0.5
# y1 = l['height'] * 0.75
# y2 = l['height'] * 0.25
# driver.swipe(x1,y1,x1,y2,500)
swipeUp(driver)